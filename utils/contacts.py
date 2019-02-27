
from driver import (
    db_msg,
)


contacts_map = dict()


def load_contacts():
    for doc in db_msg.contact_cleansed.find({}, {'NickName': 1}):
        contacts_map[doc['_id']] = doc['NickName']


def get_nickname(username):
    if username not in contacts_map:
        load_contacts()

    return contacts_map.get(username, username)


if __name__ == '__main__':
    # load_contacts()
    print(get_nickname('@9b5e4f9b9ba78e43764f4bf4b332bb47'))
