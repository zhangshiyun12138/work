# -*- coding: utf-8 -*-
import pytest
import allure

@allure.feature("测试计算器算法")
#定义算法类
class TestCalc:
    @allure.story("加法算法测试")
    @pytest.mark.run(order=1)  #控制加法测试用例顺序第一个执行
    def test_add(self,get_calc,get_add_data): #定义测试加法用例，实例化加法
        result = get_calc.add(get_add_data[0],get_add_data[1])
        if isinstance(result,float):  #判断result数据类型，如果是浮点型，result强制保留小数后两位
            result = round(result,2)
        #断言是否相等，相等则通过，不相等则失败
        assert result == get_add_data[2]

    @pytest.mark.run(order=3)  #控制乘法测试用例顺序第三个执行
    def test_mul(self,get_calc,get_mul_data): #定义测试乘法用例，实例化乘法
        result = get_calc.add(get_mul_data[0],get_mul_data[1])
        if isinstance(result,float):  #判断result诗句类型，如果是浮点型，result强制保留小数后两位
            result =round(result,2)
        #断言结果是否相等，相等则通过，不相等则失败
        assert result == get_mul_data[2]

    @pytest.mark.run(order=4) #控制除法测试用例顺序第三个执行
    def test_div(self,get_calc,get_div_data): #定义除法测试用例，实例化除法
        result = get_calc.add(get_div_data[0],get_div_data[1])
        if isinstance(result,float):  #判断result数据类型，如果是浮点型，result强制保留小数后两位
            result = round(result,2)
        #断言结果是否相等，相等则通过，不相等则失败
        assert result == get_div_data[2]

    @pytest.mark.run(order=2) #减法测试用例顺序第二个执行
    def test_sub(self,get_calc,get_sub_data): #定义减法测试用例，实例化减法
        result = get_calc.add(get_sub_data[0],get_sub_data[1])
        if isinstance(result,float):  #判断result数据类型，如果是浮点型，result强制保留小数后两位
            result = round(result,2)
        #断言结果是否相等，相等则通过，不相等则失败
        assert result == get_sub_data[2]