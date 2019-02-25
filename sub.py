import json

from driver import r
from config import REDIS_CHANNEL


p = r.pubsub()
p.subscribe(REDIS_CHANNEL)

jobs = []


def display_on_console(msg):
    if isinstance(msg, dict):
        print(msg.keys())


def start():
    for r_msg in p.listen():
        try:
            msg = json.loads(r_msg['data'])
        except TypeError:
            pass
        else:
            for job in jobs:
                job(msg)


if __name__ == '__main__':
    jobs.append(display_on_console)
    start()
