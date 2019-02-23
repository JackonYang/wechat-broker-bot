# Wechat Broker Bot

存储、转发个人微信号收到的消息。


## 应用场景：

#### 1. 微信和 bot engine 之间的 Message Queue

每次登录 wechat bot 时，需要扫描二维码，且，登录过于频繁容易触发微信的 anti-bot 机制。

将 wechat 登录器和 bot engine 解耦，
既能增加安全性，又可以专注于业务逻辑的开发。

#### 2. 微信消息备份器

将收到的微信消息全部写入 MongoDB 保存，并定期备份至云存储 (如 OSS)。

持续积累对话语料，方便后续 bot 功能增强、复现历史数据等。

#### 3. 避免触发微信安全机制

尽可能拟人化的操作序列控制，增加账号的安全性、稳定性。

比如：

在接收消息和回复之间，增加一个相对合理的随机间隔时间。

控制加群、加好友等操作的频率。


## Usage

开发、测试均使用 python3.


#### 安装依赖

```bash
$ pip3 install -r requirements.txt
# or using shortcut
$ make install
```


#### 交互式命令行 DEBUG 工具

```bash
$ python3 broker_bot.py
# or using shortcut
$ make debug
```


#### 正常运行

```bash
$ python3 main.py
# or using shortcut
$ make run
```