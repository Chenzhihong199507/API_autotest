# -*- coding:utf-8 -*-
import unittest
import os
import time
from common import HTMLTestRunner
from config.setting import TEST_CONFIG,SOURCE_FILE,TARGET_FILE,TEST_REPORT,TEST_CASE

# 用例路径
# case_path = os.path.join(os.getcwd())
#print(os.getcwd())
# 报告存放路径
# report_path = os.path.join(os.getcwd(), 'report')
#print(report_path)

def all_case():
    discover = unittest.defaultTestLoader.discover(TEST_CASE, pattern="test*.py", top_level_dir=None)

    # print(discover)
    return discover

if __name__ == '__main__':
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 2、html报告文件路径
    report_abspath = os.path.join(TEST_REPORT, "result_"+now+".html")

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 4、调用add_case函数返回值
    runner.run(all_case())
    fp.close()