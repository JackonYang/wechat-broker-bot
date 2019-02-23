import os

REPO_ROOT = os.path.dirname(
    os.path.abspath(
        __file__
    )
)

MONGO_HOST_MSG = '192.168.1.66'
MONGO_DBNAME_MSG = 'wechat_msg_personal'


if __name__ == '__main__':
    print(REPO_ROOT)
