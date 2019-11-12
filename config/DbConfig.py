import  pytest
import pymysql
import pymssql
import redis
import os
import re
import configparser
'''

mssql创建连接
mysql创建连接
redis创建连接

'''
prePath=os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
urlPath =os.path.join(prePath+ "\\config\\DbConfig.ini")
class dbConfig():
    def __init__(self):
        #调用remove_bom删除ini文件中BOM信息
        # content = open(urlPath, encoding='utf-8').read()
        # content = re.sub(r"\xfe\xff", "", content)
        # content = re.sub(r"\xff\xfe", "", content)
        # content = re.sub(r"\xef\xbb\xbf", "", content)
        # open(urlPath, 'w').write(content)
        # self.config = configparser.ConfigParser()
        # self.config.read(urlPath)
        pass
    def get_mssql(self,iniFile):
        print(iniFile)
        pass
    def get_mysql(self):
        pass
    def get_redis(self):
        pass

class Mssql():
    def __init__(self):
        pass
    def mssql_select(self):
        pass

    def mssql_insert(self):
        pass

    def mssql_update(self):
        pass

    def mssql_delete(self):
        pass
class Mysql():
    def __init__(self):
        pass
    def mysql_select(self):
        pass

    def mysql_insert(self):
        pass

    def mysql_update(self):
        pass

    def mysql_delete(self):
        pass
class Redis():
    def __init__(self):
        pass
    def redis_get(self):
        pass

    def redis_select(self):
        pass

    def redis_delete(self):
        pass

    def redis_init(self):
        #redis初始化
        pass

if __name__=="__main__":
    dbConfig().get_mssql(iniFile=iniFile)
    pass