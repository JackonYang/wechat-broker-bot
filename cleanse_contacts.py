import csv
import os

from driver import (
    db_msg,
)

from config import (
    CONTACT_EXPORT_PATH,
)


EXPORT_HEADERS = {
    'groups': [
        'UserName',  # starting with @@
        'NickName',
        'MemberCount',
        # 'self',
        # 'MemberList',
        # Flags
        'HeadImgUpdateFlag',
        'ContactFlag',
        'ContactType',
        'VerifyFlag',
        'AttrStatus',
        'SnsFlag',
        'Uin',
        'Statues',
        'HeadImgUrl',
        # Owner related
        'IsOwner',
        'ChatRoomOwner',
        'EncryChatRoomId',
        'PYQuanPin',
        'PYInitial',
    ],
    'friends': [
        'UserName',  # starting with @
        'NickName',
        'RemarkName',
        'KeyWord',
        'Sex',
        'Province',
        'City',
        'Signature',
        # Flags
        'Uin',
        'HeadImgFlag',
        'ContactFlag',
        'ContactType',
        'VerifyFlag',
        'AttrStatus',
        'WebWxPluginSwitch',
        'StarFriend',
        'SnsFlag',
        'HeadImgUrl',
        'PYQuanPin',
        'PYInitial',
        'RemarkPYInitial',
        'RemarkPYQuanPin',
    ],
    'mps': [
        'UserName',  # starting with @
        'NickName',
        'Province',
        'City',
        'KeyWord',
        'Signature',
        # Flags
        'Uin',
        'HeadImgFlag',
        'ContactFlag',
        'VerifyFlag',
        'AttrStatus',
        'HeadImgUrl',
        'PYQuanPin',
        'PYInitial',
    ],
}


def dump_contacts():
    for doc in db_msg.contacts.find():
        for cate in EXPORT_HEADERS.keys():
            dump_category(
                doc['myself_name'],
                cate,
                doc['data'][cate],
                doc['day'],
            )


def dump_category(owner, name, data, day):

    # # dump all the headers to pick up valueable ones.
    # headers = set()
    # for i in data:
    #     headers.update(i.keys())
    headers = EXPORT_HEADERS[name]

    filename = os.path.join(
        CONTACT_EXPORT_PATH,
        '%s-%s-%s.csv' % (owner, name, day)
    )

    if not os.path.exists(CONTACT_EXPORT_PATH):
        os.makedirs(CONTACT_EXPORT_PATH)

    with open(filename, 'w', encoding='utf-8') as f_csv:

        dict_writer = csv.DictWriter(f_csv, headers, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == '__main__':
    dump_contacts()
