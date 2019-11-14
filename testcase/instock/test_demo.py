import pytest

@pytest.fixture(scope="module",params=['test1','test2'])
def modarg(request):
    param = request.param
    print ("  设置 modarg %s" % param)
    yield param
    print ("  拆卸 modarg %s" % param)

@pytest.fixture(scope="function", params=[1,2])
def otherarg(request):
    param = request.param

    print ("  设置 otherarg %d" % param)
    yield param
    print ("  拆卸 otherarg %d" % param)

# def test_0(otherarg):
#     print ("  用 otherarg %s 运行 test0" % otherarg)
def test_1(iniFileDemo):

    print("%% %s"%iniFileDemo)
    # print ("  用 modarg %s 运行 test1" % iniFileDemo)
# def test_2(otherarg, modarg):
#     print ("  用 otherarg %s 和 modarg %s 运行 test2" % (otherarg, modarg))

test_user_data=["admin1","admin2"]
@pytest.fixture(scope="module")
def login(request):
    user=request.param
    print("lgoin account:%s"%user)
    return user

@pytest.mark.parametrize("login",test_user_data)
def test_login(login):
    '''登录用例'''
    a=login
    print("测试用例中a是%s"%a)









if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', 'C:/work/Report/report/xml'])
    pytest.main(['-s','test_demo.py'])
    # pytest .main(''- s    test_module.py)