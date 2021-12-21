# -*- coding:utf-8 -*-
# 单个用例执行
# 1、导入模块
import unittest
import requests
import json
import ddt
from ddt import ddt, data, file_data, unpack
from common.excel_handler import ExcelHandler
from common.request import APIdemo
from common.readConfig import ReadConfigFile
from common.readYaml import WRYaml

ad = APIdemo()

# 2、继承自unittest.TestCase类
@ddt
class TestLawInfo(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作
    def setUp(self):
        #print('\ncases before')
        pass

    # 4、定义测试用例，名字以“test”开头
    @file_data("D:\\Projects\\PycharmProjects\\unittest\\datas\\anhaoDetect.yaml")
    def test_anhao(self,**kwargs):
        """anhaoDetect"""
        caseName = kwargs.get("caseName")
        payloads = kwargs.get("payloads")
        expectResult =kwargs.get("expectResult")

        print(caseName)
        url = "https://wszs-api.huiwei.tech/Judgements/ErrorDetect"

        headers = {
            'Content-Type': 'application/json'
        }
        response = ad.do_post(url,json.dumps(payloads),headers=headers)
        try:
            res = response.json()["detections"][0]["corrections"][0]
            print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
            self.assertEqual(res, expectResult)

        except:
            res = response.json()["detections"]
            print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
            self.assertEqual(res, expectResult)


    # 6、清理环境
    def tearDown(self):
        #print('case after')
        pass


# 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
if __name__ == '__main__':
    unittest.main()