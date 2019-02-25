import socket
import schedule
import threading
import time


from wxpy import (
    Bot,
    # Message,
    # SYSTEM,
)

from iutil.datestr import (
    today,
    readable_now,
)

import config

from driver import (
    db_msg,
)


bot = Bot(console_qr=True, cache_path=True)
bot.enable_puid()

# wechat account used to login
myself = bot.self
myself_name = myself.name

# environment info the login
device_hostname = socket.gethostname()
login_at = readable_now()

# store login logs in MongoDB
db_msg.login_log.insert_one({
    'puid': myself.puid,
    'device_hostname': device_hostname,
    'myself_name': myself_name,
    'account_info': myself.raw,
    'login_at': login_at,
})


contact_categories = {
    'groups': bot.groups,
    'mps': bot.mps,
    'friends': bot.friends,
}


def fetch_contacts(bot, update=True):
    res = {}
    for cate, meth in contact_categories.items():
        rsp = meth(update=update)
        data = [r.raw for r in rsp]
        res[cate] = data
    return res


def dump(bot):
    data = fetch_contacts(bot)

    # store contacts info in MongoDB
    db_msg.contacts.insert_one({
        'puid': myself.puid,
        'device_hostname': device_hostname,
        'account_info': myself.raw,
        'myself_name': myself_name,
        'login_at': login_at,
        'fetched_at': readable_now(),
        "scheme_version": "1.0",
        'data': data,
    })


def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


@bot.register(except_self=False, run_async=True)
def msg_receiver(msg):
    try:
        bucket = today()
        # store message in MongoDB
        coll_name = 'received_msg_raw_%s' % bucket.replace('-', '')

        callable_keys = [
            'Text',
        ]
        for key in callable_keys:
            if callable(msg.raw.get(key)):
                msg.raw[key] = msg.raw[key]()

        db_msg[coll_name].insert_one({
            'puid': myself.puid,
            'myself_name': myself_name,
            'device_hostname': device_hostname,
            'login_at': login_at,
            'received_at': readable_now(),
            "scheme_version": "1.0",
            'msg': msg.raw,
        })
    except Exception as e:
        db_msg.errors.insert_one({
            'puid': myself.puid,
            'myself_name': myself_name,
            'device_hostname': device_hostname,
            'login_at': login_at,
            'received_at': readable_now(),
            'error': str(e),
        })


schedule.every().day.at(config.DAILY_DUMP_CONTACT_AT).do(dump, bot)

schedule_thread = run_continuously()


if __name__ == '__main__':
    # go to interactive command line, easy to debug
    from wxpy import embed

    embed()
