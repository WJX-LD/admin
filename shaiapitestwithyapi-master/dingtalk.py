# -*- coding: utf-8 -*-

import requests
import json


def dingTalk_text(msg: str, dtoken):
    """
    发送钉钉消息
    :param msg:消息正文
    :param dtoken:钉钉token
    """

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "atMobiles": [
                ""
            ],
            "isAtAll": False
        }
    }

    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token=' + dtoken,
        data=json_data, headers=headers)


if __name__ == '__main__':
    print(dingTalk_text('1'))
