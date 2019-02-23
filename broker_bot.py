import time
import socket

from wxpy import (
    Bot,
    # Message,
    # SYSTEM,
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
login_at = time.time()

# store login logs in MongoDB
db_msg.login_log.insert_one({
    'puid': myself.puid,
    'device_hostname': device_hostname,
    'account_info': myself.raw,
    'login_at': login_at,
})


@bot.register()
def msg_receiver(msg):
    # store message in MongoDB
    db_msg.received_msg_raw.insert_one({
        'puid': myself.puid,
        'myself_name': myself_name,
        'device_hostname': device_hostname,
        'login_at': login_at,
        'received_at': time.time(),
        'msg': msg.raw,
    })


if __name__ == '__main__':
    # go to interactive command line, easy to debug
    from wxpy import embed

    embed()
