# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   run_server.py
 
@Time    :   2020/9/19 9:50 上午
 
@Desc    :   启动服务  使用sanic
 
"""

# -*- coding: utf-8 -*-
import json
import logging
import datetime
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from sanic import Sanic, response
from sanic.response import text, HTTPResponse
from sanic.request import Request
from sanic_cors import cross_origin

from model.predict import ChatBot
from bert4keras.tokenizers import Tokenizer
from model.config import Config

from model.utils.LogUtils import Logger

logger = logging.getLogger(__name__)

app = Sanic(__name__)

cf = Config()

tokenizer = Tokenizer(cf.dict_path, do_lower_case=True)

chatbot = ChatBot(start_id=None, end_id=tokenizer._token_end_id, maxlen=32)

@app.route("/")
async def test(request):
    return text('Hello World!')


@app.post('api/chichat')
async def robot(request: Request) -> HTTPResponse:
    """
    机器人会话接口，

    :param sender: 会话id
    :param message: 用户query
    :return:
    """
    localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        senderId = request.json['sender']
        query = request.json['message']

        result = chatbot.response([query])  # 请求技能分发

        res_dic = {
            "result": result,
            "time": localtime

        }
        return response.json(res_dic)

    except Exception as e:
        logger.info('Error is {}'.format(e))
        res_dic = {
            "result": 'Failure',
            "time": localtime
        }

        return response.json(res_dic)


if __name__ == '__main__':
    app.run(host='172.18.86.21', port=9012, auto_reload=True)