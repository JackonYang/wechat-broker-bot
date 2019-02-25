import csv
import os

from driver import (
    db_msg,
)

from config import (
    MESSAGE_EXPORT_PATH,
)


EXPORT_HEADERS = {
    'Sharing': [
        'FromUserName',
        'ActualNickName',
        'Text',
        # 'Content',
        # 'CreateTime',
        # 'NewMsgId',
        # 'MsgId',
        'ImgStatus',
        'AppMsgType',
        'MsgType',
        'Status',
        'ActualUserName',
        'AppInfo',
        'Url',
        'ToUserName',
        'FileName',
        'EncryFileName',
    ],
}


def dump_messages(day):
    collname = 'received_msg_raw_%s' % day.replace('-', '')

    for cate in EXPORT_HEADERS.keys():
        data = dict()
        nicknames = dict()
        for i in db_msg[collname].find({'msg.Type': cate}):
            puid = i['puid']
            nickname = i['myself_name']
            if puid not in data:
                data[puid] = []
                nicknames[puid] = nickname
            data[puid].append(i['msg'])

        for puid, data in data.items():
            dump_category(
                nicknames[puid],
                cate,
                data,
                day,
            )


def dump_category(owner, name, data, day):

    # # dump all the headers to pick up valueable ones.
    # headers = set()
    # for i in data:
    #     headers.update(i.keys())
    headers = EXPORT_HEADERS[name]

    filename = os.path.join(
        MESSAGE_EXPORT_PATH,
        '%s-%s-%s.csv' % (name, day, owner)
    )

    if not os.path.exists(MESSAGE_EXPORT_PATH):
        os.makedirs(MESSAGE_EXPORT_PATH)

    with open(filename, 'w', encoding='utf-8') as f_csv:

        dict_writer = csv.DictWriter(f_csv, headers, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == '__main__':
    dump_messages('20190225')
