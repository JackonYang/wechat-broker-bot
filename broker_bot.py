import socket

from wxpy import (
    Bot,
    # Message,
    # SYSTEM,
)

from iutil.datestr import (
    today,
    readable_now,
)

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
    'account_info': myself.raw,
    'login_at': login_at,
})


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
            'msg': msg.raw,
        })
    except Exception as e:
        db_msg.errors.insert_one({
            'puid': myself.puid,
            'myself_name': myself_name,
            'device_hostname': device_hostname,
            'login_at': login_at,
            'received_at': readable_now(),
        })


if __name__ == '__main__':
    # go to interactive command line, easy to debug
    from wxpy import embed

    embed()
