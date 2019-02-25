import os

REPO_ROOT = os.path.dirname(
    os.path.abspath(
        __file__
    )
)

MONGO_HOST_MSG = '192.168.1.66'
MONGO_DBNAME_MSG = 'wechat_msg_personal'

REDIS_HOST_MSG = '192.168.1.66'
REDIS_DB = 9
REDIS_CHANNEL = 'wechat-broker'

DAILY_DUMP_CONTACT_AT = '01:00'
CONTACT_EXPORT_PATH = os.path.join(REPO_ROOT, 'data/contacts')
MESSAGE_EXPORT_PATH = os.path.join(REPO_ROOT, 'data/messages')


if __name__ == '__main__':
    print(REPO_ROOT)
