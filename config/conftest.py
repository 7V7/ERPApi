import pytest
import re
import os
urlPath =os.path.join( os.path.dirname(os.path.abspath(__file__))+"\\configProperties.ini")
dbPath =os.path.join( os.path.dirname(os.path.abspath(__file__))+"\\dbconfig.ini")
# @pytest.fixture(scope='function',params=[urlPath,dbPath])
# def iniFile(request):#去掉配置文件开头的BOM字节
#     param=request.param
#     print("parm",param)
#     yield param
#     print("yield param:",param)
#     content = open(param,encoding='utf-8').read()
#     content = re.sub(r"\xfe\xff","", content)
#     content = re.sub(r"\xff\xfe","", content)
#     content = re.sub(r"\xef\xbb\xbf","", content)
#     open(param, 'w').write(content)
#     return iniFile(param)


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

# def test_0(otherarg):
#     print ("  用 otherarg %s 运行 test0" % otherarg)




