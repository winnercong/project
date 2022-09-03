import allure
import pytest
import yaml

from python_code.calc import Calculator


# with open('./datas/calc.yaml') as f:
#     datas = yaml.safe_load(f)['add']
#     add_datas = datas['datas']
#     print(add_datas)
#     myid = datas['myid']
#     print(myid)
#
# @pytest.fixture(params=add_datas,ids=myid)
# def get_add_datas(request):
#     print("开始计算")
#     data = request.param
#     print(f"request.param 里面的测试数据是：{data}")
#     yield  data
#     print("计算结束")

@allure.feature("测试计算器")
class TestCalc:

    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器类
    #     self.calc = Calculator()
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize("a,b,expect",
    #                          add_datas,ids=myid
    #                          )

    @pytest.mark.add
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            # 实例化计算器类
            # calc = Calculator()
            # 调用add方法
            with allure.step("计算两个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断result是浮点数，作为保留2为小数处理
            if isinstance(result, float):
                result = round(result, 2)
            # 得到结果之后，需要写断言
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")
