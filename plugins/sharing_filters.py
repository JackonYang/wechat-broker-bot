from bs4 import BeautifulSoup

from utils.contacts import get_nickname

from driver import (
    db_parser,
)

sharing_info_fields = [
    'FromUserName',
    'ToUserName',
    'ActualUserName',
    'ActualNickName',
    'AppMsgType',
    'Text',
]

article1_fields = {
    'title': 'title',
    'des': 'desc',
    'url': 'url',
    'thumburl': 'thumburl',
    'sourcedisplayname': 'mp',
}

article2_fields = {
    'title': 'title',
    'digest': 'desc',
    'url': 'url',
    'cover': 'thumburl',
    'name': 'mp',
}

SHARING_TYPE = 'Sharing'


skip_user = {
    '@5b2ccf8aafa57b0ae643f9748730c8f1',  # 公众平台安全助手
    '@4b222c74b983ad6f59282d132769837d',  # 微信广告助手
}

skip_content = {
    'This type of message is not supported on WeChat for Web. View it on your phone.',
}


def filter_sharing(msg_wrapper):
    msg = msg_wrapper['msg']

    if msg.get('Type') != SHARING_TYPE:
        return

    content = msg.get('Content')
    if not content or content in skip_content:
        return

    if msg['FromUserName'] in skip_user:
        return

    info = {
        k: msg.get(k) for k in sharing_info_fields
    }

    info['FromNickName'] = get_nickname(msg['FromUserName'])
    info['ToNicknNme'] = get_nickname(msg['ToUserName'])

    soup = BeautifulSoup(content, 'xml')

    try:
        if soup.find('mmreader'):  # mp push
            items = soup.find_all('item')
            articles = [
                {key2: item.find(key1) for key1, key2 in article2_fields.items()}
                for item in items
            ]
        else:
            articles = [{key2: soup.find(key1) for key1, key2 in article1_fields.items()}]
    except Exception:
        print(msg_wrapper)
        print(soup)
        raise

    info['articles'] = [
        {k: v and v.text for a in articles for k, v in a.items()}
    ]
    info['received_at'] = msg_wrapper['received_at']

    db_parser.sharing.insert_one(info)
