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
#通过yaml文件读取数据
# wryaml = WRYaml()
# ym = wryaml.read_yaml('D:\\Projects\\PycharmProjects\\unittest\\datas\\CaseInfo.yaml')
#读取配置文件
# rc = ReadConfigFile()
# host = rc.read_config()[0]

#通过excel文件读取数据
# excel = ExcelHandler('./datas/cases.xlsx')
# case_data = excel.read_excel('Sheet3')
# case_data1 = excel.read_excel('Sheet4')
# case_data2 = excel.read_excel('Sheet5')
# case_data3 = excel.read_excel('Sheet6')

# 2、继承自unittest.TestCase类
@ddt
class TestLawInfo(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作
    def setUp(self):
        #print('\ncases before')
        pass

    # 4、定义测试用例，名字以“test”开头
    @file_data("D:\\Projects\\PycharmProjects\\unittest\\datas\\Cases.yaml")
    def test_Cases(self,**kwargs):
        """案例查询结果接口"""
        caseName = kwargs.get("caseName")
        payloads = kwargs.get("payloads")
        expectResult =kwargs.get("expectResult")
        expectResult2 = kwargs.get("expectResult2")

        print(caseName)
        url = "https://wszs-api.huiwei.tech/library/cases"

        headers = {
            'Content-Type': 'application/json'
        }
        response = ad.do_post(url,json.dumps(payloads),headers=headers)
        res = response.json()
        print("期望返回1:" + str(expectResult) + "\n" + "实际返回1:" + str(res["totalResults"]))
        print("期望返回2:" + str(expectResult2) + "\n" + "实际返回2:" + str(len(res["data"])))
        self.assertEqual(res["totalResults"], expectResult)
        self.assertEqual(len(res["data"]), expectResult2)


    @file_data("D:\\Projects\\PycharmProjects\\unittest\\datas\\CaseInfo.yaml")
    def test_CaseInfo(self,**kwargs):
        """案例详情接口"""
        caseName = kwargs.get("caseName")
        payloads = kwargs.get("payloads")
        expectResult =kwargs.get("expectResult")

        print(caseName)
        url = "https://wszs-api.huiwei.tech/library/case/info"

        headers = {
            'Content-Type': 'application/json'
        }
        response = ad.do_post(url,json.dumps(payloads),headers=headers)
        res = response.json()["data"]["schema"]["anchors"]
        print("期望返回:" + str(expectResult) + "\n" + "实际返回:" + str(res))
        self.assertEqual(res, expectResult)

    # @ddt.data(*case_data2)
    # def test_laws(self, items):
    #     '''法规搜索结果接口'''
    #     print(items["caseNo"] + "___" + items["caseName"])
    #     url = host +items["url"]
    #
    #     headers = {
    #         'Content-Type': 'application/json'
    #     }
    #     # response = requests.request("POST", url, headers=headers, data=payload)
    #     response = ad.do_post(url, items['payload'].encode('utf-8'),headers=headers)
    #     res = response.json()["data"]
    #     print("期望返回:" + str(items['expected']) + "\n" + "实际返回:" + str(len(res)))
    #     self.assertEqual(len(res), items['expected'])

    # 6、清理环境
    def tearDown(self):
        #print('case after')
        pass


# 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
if __name__ == '__main__':
    unittest.main()