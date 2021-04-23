# -*- coding: utf-8 -*-
#计算器作业
import pytest
import allure

@allure.feature("测试计算器算法")
class TestCalc():  #闯将计算测试类

    @allure.story("加法算法测试")
    @pytest.mark.run(order=1)  #控制加法测试用例为顺序第一个
    def test_add(self,get_calc,get_add_data):  #定义测试加法用例，并实例话加法
        result = get_calc.add(get_add_data[0],get_add_data[1])
        #断言result的数据类型，如果为浮点型，则强制保留小数后两位
        if isinstance(result,float):
            result = round(result,2)
        #断言结果是否相等，如果相等则通过，如果不相等则失败
        assert result == get_add_data[2]

    @allure.story("除法算法")
    @pytest.mark.run(order=4)  #控制除法测试用例为顺序第四个
    def test_div(self,get_calc,get_div_data):  #定义除法测试用例，并实例话除法
        result = get_calc.add(get_div_data[0],get_div_data[1])
        #断言result的数据类型，如果为浮点型，则强制保留小数后两位
        if isinstance(result,float):
            result = round(result,2)
        #断言结果是否相等，相等则通过，不相等则失败
        assert result == get_div_data[2]

    @allure.story("减法算法")
    @pytest.mark.run(order=2)  #控制减法测试用例为顺序第四个
    def test_sub(self,get_calc,get_sub_data):  #定义减法测试用例，并实例话减法
        result = get_calc.add(get_sub_data[0],get_sub_data[1])
        #断言result的数据类型，如果为浮点型，则前置保留小数后两位
        if isinstance(result,float):
            result = round(result,2)
        #断言结果是否相等，如果相等则通过，不相等则失败
        assert result == get_sub_data[2]

    @allure.story("乘法算法")
    @pytest.mark.run(order=3)  #控制乘法测试用例为顺序第三个
    def test_mul(self,get_calc,get_mul_data):  #定义乘法测试用例，并实例化乘法
        result = get_calc.add(get_mul_data[0],get_mul_data[1])
        #断言result的数据类型，如果为浮点型，则强制保留小数点后两位
        if isinstance(result,float):
            result = round(result,2)
        #断言结果是否相等，如果相等则通过，如果不相等则失败
        assert result == get_mul_data[2]