#-*-coding:utf-8-*-
import unittest
import requests
from common.my_log import mylog
import json

class webrequests(unittest.TestCase):

    logger = mylog('test').getlog()

    def get(self, url, params=None, headers=None, files=None):
        '''封装get方法，return响应码和响应内容'''
        try:
            r = requests.get(url, params=params, headers=headers, files=files)
            self.logger.info("请求的内容：%s" % params)
            status_code = r.status_code  # 获取返回的状态码
            self.logger.info("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            # print(type(response_json))
            # print(json.dumps(response_json, indent=2))
            self.logger.info("响应内容：%s" % json.dumps(response_json, indent=2, ensure_ascii=False))
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            self.logger.error("请求失败！", exc_info=1)


