from bson import json_util

from driver import r
from config import REDIS_CHANNEL

from driver import (
    db_msg,
)


def publish(msg):
    data = json_util.dumps(msg)
    r.publish(REDIS_CHANNEL, data)


def simulate():
    coll = 'received_msg_raw_20190225'

    for i in db_msg[coll].find():
        publish(i)


if __name__ == '__main__':
    simulate()
