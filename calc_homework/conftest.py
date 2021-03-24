import pytest
import allure
import yaml
from calc_homework.calc_case import Calc

#创建fix方法
@pytest.fixture(scope="module")  #将fixture作用域设置为module级别
def get_calc():
    #执行测试用例前打印【开始计算】
    print("计算开始")
    calc = Calc()
    yield calc
    #执行完测试用例后打印【结束计算】
    print("结束计算")

#健在yaml文件，对里边的值分别赋值给变量
with open('calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add_value']
    add_ids = datas['add_myids']
    sub_data = datas['sub_value']
    sub_ids = datas['sub_myids']
    mul_data = datas['mul_value']
    mul_ids = datas['mul_myids']
    div_data = datas['div_value']
    div_ids = datas['div_myids']

#获取加法数据，并返回
@pytest.fixture(params=add_data,ids=add_ids)
def get_add_data(request):
    data = request.param
    return data

#获取减法数据。并返回
@pytest.fixture(params=sub_data,ids=sub_ids)
def get_sub_data(request):
    data = request.param
    return data

#获取乘法数据，并返回
@pytest.fixture(params=mul_data,ids=mul_ids)
def get_mul_data(request):
    data = request.param
    return data

#获取除法数据，并返回
@pytest.fixture(params=div_data,ids=div_ids)
def get_div_data(request):
    data = request.param
    return data
