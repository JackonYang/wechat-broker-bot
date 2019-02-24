# MongoDB Data Scheme

## Version 1.0

- puid: string, 登录账号的 puid (wxpy 提供的 unique user id)
- myself_name: string, 登录账号的微信昵称
- device_hostname: string, 登录设备（电脑）的 hostname
- login_at: timestamp string, 微信账号登录时间，格式：%Y-%m-%d %H:%M:%S
- received_at: timestamp string, 微信消息接收时间，格式：%Y-%m-%d %H:%M:%S
- msg: json dict, 微信消息原始内容，由 wxpy 提供


Example:

```javascript
{
    "_id" : ObjectId("5c717ec8e576d052ac5fcacd"),
    "puid" : "1469xxxx",
    "myself_name" : "Jackon",
    "device_hostname" : "jackon-ubuntu18",
    "login_at" : "2019-02-24 01:00:31",
    "received_at" : "2019-02-24 01:11:36",
    "scheme_version": "1.0",
    "msg" : {
        "MsgId" : "849991329582499xxxx",
        "FromUserName" : "@@1d2d1d13af8aac87eae93ebd216ae522b929e614dbeff08f6a1249cddb3bxxxx",
        "ToUserName" : "@f2343db94a6e7b9fc32dadb3164d3c19b59ee95c14d9e6d7d0b8dee61469xxxx",
        "MsgType" : 1,
        "Content" : "可惜我的焦糖和小鬼王不是英短",
        "Status" : 3,
        "ImgStatus" : 1,
        "CreateTime" : 1550941894,
        "VoiceLength" : 0,
        "PlayLength" : 0,
        "FileName" : "",
        "FileSize" : "",
        "MediaId" : "",
        "Url" : "",
        "AppMsgType" : 0,
        "StatusNotifyCode" : 0,
        "StatusNotifyUserName" : "",
        "RecommendInfo" : {
            "UserName" : "",
            "NickName" : "",
            "QQNum" : 0,
            "Province" : "",
            "City" : "",
            "Content" : "",
            "Signature" : "",
            "Alias" : "",
            "Scene" : 0,
            "VerifyFlag" : 0,
            "AttrStatus" : 0,
            "Sex" : 0,
            "Ticket" : "",
            "OpCode" : 0
        },
        "ForwardFlag" : 0,
        "AppInfo" : {
            "AppID" : "",
            "Type" : 0
        },
        "HasProductId" : 0,
        "Ticket" : "",
        "ImgHeight" : 0,
        "ImgWidth" : 0,
        "SubMsgType" : 0,
        "NewMsgId" : NumberLong(849991329582499xxxx),
        "OriContent" : "",
        "EncryFileName" : "",
        "ActualUserName" : "@52f10513eee65e72602c99ad2fda6f5bd8028c2575d9b83772974709f1f3xxxx",
        "ActualNickName" : "只是一个可爱的小仙女而已",
        "isAt" : false,
        "Type" : "Text",
        "Text" : "可惜我的焦糖和小鬼王不是英短"
    }
}
```
