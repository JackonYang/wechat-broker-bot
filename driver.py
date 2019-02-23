from pymongo import MongoClient

import config


db_msg = MongoClient(config.MONGO_HOST_MSG)[config.MONGO_DBNAME_MSG]


if __name__ == '__main__':
    print(db_msg)
