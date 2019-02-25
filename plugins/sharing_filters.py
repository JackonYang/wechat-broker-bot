
from utils.contacts import get_nickname


sharing_info_fields = [
    'FromUserName',
    'ToUserName',
    'ActualUserName',
    'ActualNickName',
    'AppMsgType',
    'Text',
]

SHARING_TYPE = 'Sharing'


def filter_sharing(msg_wrapper):
    msg = msg_wrapper['msg']

    if msg.get('Type') == SHARING_TYPE:
        info = {
            k: msg.get(k) for k in sharing_info_fields
        }

        info['FromNickName'] = get_nickname(msg['FromUserName'])
        info['ToNicknNme'] = get_nickname(msg['ToUserName'])

        print(info)
        # content = msg.get('Content')
