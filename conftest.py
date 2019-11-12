import pytest
import sys, os

'''


'''
import pytest
import re
import os
urlPath =os.path.join( os.path.dirname(os.path.abspath(__file__))+"\\configProperties.ini")
dbPath =os.path.join( os.path.dirname(os.path.abspath(__file__))+"\\dbconfig.ini")
@pytest.fixture(scope='function',params=[urlPath,dbPath])
def iniFileDemo(request):#去掉配置文件开头的BOM字节
    param=request.param
    print("parm",param)
    yield param
    print("yield param:",param)
    return request.param
    # content = open(parm,encoding='utf-8').read()
    # content = re.sub(r"\xfe\xff","", content)
    # content = re.sub(r"\xff\xfe","", content)
    # content = re.sub(r"\xef\xbb\xbf","", content)
    # open(config_path, 'w').write(content)
    # return remove_BOM(config_path)


# @pytest.fixture(scope="module",params=['test1','test2'])
# def modarg(request):
#     param = request.param
#     print ("  设置 modarg %s" % param)
#     yield param
#     print ("  拆卸 modarg %s" % param)
#
# @pytest.fixture(scope="function", params=[1,2])
# def otherarg(request):
#     param = request.param
#
#     print ("  设置 otherarg %d" % param)
#     yield param
#     print ("  拆卸 otherarg %d" % param)
#
# # def test_0(otherarg):
# #     print ("  用 otherarg %s 运行 test0" % otherarg)
# def test_1(modarg):
#     print ("  用 modarg %s 运行 test1" % modarg)








# print(os.path.abspath(os.path.join(os.path.dirname(__file__), './')))
# sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), './'))))
@pytest.fixture()
def execute_conftest():
    print("-------------------execute_conftest开始执行-------------------")

@pytest.fixture(scope='module')
def demoFunction():
    print("open file")


# @pytest.fixture(scope="module")
# def connect_database():
#     pass
#
# @pytest.fixture(scope='function')
# def init_database():
#     pass
    # # Create the database and the database table
    # db.create_all()
    #
    # # Insert user data
    # user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    # user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    # db.session.add(user1)
    # db.session.add(user2)
    #
    # # Commit the changes for the users
    # db.session.commit()
    #
    # yield db  # this is where the testing happens!
    #
    # db.drop_all()
