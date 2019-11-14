# -*- coding: utf-8 -*-
import os
import codecs
import configparser
import re
import json
import requests
import pytest
import logging
import allure
import config.urlconfig as config

class TestGetStock(object):

    # def setUp(self):
    # @allure.feature("测试用例1")
    # def test_getstock_case1(self):
    #     """
    #     获取仓库信息
    #     :return:
    #     """
    #     url =config.returnUrl().requestUrl('getStock')
    #     print(url)
    #     logging.info("***********获取仓库信息***********")
    #     param={'json':'{"OrganizationSysNo":1 }'}
    #     h=requests.post(url,param)
    #     # print(h.text)
    #     assert ('"State":1') in h.text
    #     assert 1==1
    #
    #
    # @allure.feature("测试用例2")
    # def test_case2(self):
    #     """
    #     测试用例2
    #     :return:
    #     """
    #     assert 0==0
    #
    # @allure.feature("测试用例3")
    # def test_case3(self):
    #     """
    #     测试用例2
    #     :return:
    #     """
    #     assert 1==1

    @allure.feature("测试用例4")
    def test_case4(iniFile):
        print ("  用 modarg %s 运行 test1" % iniFile)
        assert 1==1

if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', 'C:/work/Report/report/xml'])
    pytest.main('-s test_getstock.py')