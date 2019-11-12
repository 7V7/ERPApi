# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: zhangfen
@file: file_utils.py
@time: 11/8/19 14:57
@description：url接口请求配置文件
"""

import os
import codecs
import configparser
import re

urlPath =os.path.join( os.path.dirname(os.path.abspath(__file__))+"\\configProperties.ini")
class urlConfig():
    def __init__(self):
        #调用remove_bom删除ini文件中BOM信息
        content = open(urlPath, encoding='utf-8').read()
        content = re.sub(r"\xfe\xff", "", content)
        content = re.sub(r"\xff\xfe", "", content)
        content = re.sub(r"\xef\xbb\xbf", "", content)
        open(urlPath, 'w').write(content)
        self.config = configparser.ConfigParser()
        self.config.read(urlPath)

    def requestUrl(self,name):
        url = self.config.get('host', 'baseUrl')+ self.config.get('path', name)
        return url

# if __name__=='__main__':
#     baseUrl = returnUrl().requestUrl("getStock")
