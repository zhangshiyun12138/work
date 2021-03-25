import pytest
import yaml
import allure
from calc_homework.calc_case import Calc

#创建fixture方法
@pytest.fixture(scope="module")  #将fixture方法的作用域为module级别
def get_calc():
    print("开始计算")   #用例执行前打印【开始计算】
    calc = Calc()
    yield calc
    print("结束计算")   #用例执行完后打印【结束计算】

#获取yaml文件，并对里边的数据赋值给变量，给后续测试方法想要参数化
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

@pytest.fixture(params=add_data,ids=add_ids)  #获取加法数据，并返回
def get_add_data(request):
    data = request.param
    return data

@pytest.fixture(params=sub_data,ids=sub_ids)  #获取加法数据，并返回
def get_sub_data(request):
    data = request.param
    return data

@pytest.fixture(params=mul_data,ids=mul_ids)  #获取乘法数据，并返回
def get_mul_data(request):
    data = request.param
    return data

@pytest.fixture(params=div_data,ids=div_ids)  #获取除法数据，并返回
def get_div_data(request):
    data = request.param
    return data