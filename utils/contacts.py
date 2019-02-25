
from driver import (
    db_msg,
)


contacts_map = dict()


def load_contacts():
    for doc in db_msg.contacts.find():
        for cate, data in doc['data'].items():
            for record in data:
                contacts_map[record['UserName']] = record['NickName']


def get_nickname(username):
    if len(contacts_map) == 0:
        load_contacts()

    return contacts_map.get(username, username)


if __name__ == '__main__':
    load_contacts()
