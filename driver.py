from pymongo import MongoClient
import redis

import config


db_msg = MongoClient(config.MONGO_HOST_MSG)[config.MONGO_DBNAME_MSG]

r = redis.StrictRedis(host=config.REDIS_HOST_MSG, port=6379, db=config.REDIS_DB)


if __name__ == '__main__':
    print(db_msg)
