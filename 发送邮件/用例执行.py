import time
import unittest
from 添加员工测试用例 import Crmxz
from HTMLTestRunner import HTMLTestRunner
class Ylzx():
    def ylzx(self,*args):
        time.sleep(4)
        # 测试套件，构建测试集
        suite = unittest.TestSuite()
        # suite.addTest(Crmxz('test_xz1'))
        suite.addTest(*args)
        # dir=r'D:/pythonProject/venv/crm自动化测试/员工新增/发送邮件'
        # discover=unittest.defaultTestLoader.discover(dir,pattern='添加员工测试用例.py')
        # runner=unittest.TextTestRunner()
        # runner.run(discover)
        # dir='./'
        # discover=unittest.defaultTestLoader.discover(dir,pattern='test_search')
        # 我们要新建一个用于保存我们测试结果的文件，html
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        print(now)
        # 定义文件的名字
        filename = r'D:/pythonProject/venv/7.13/' + now + "_result.html"
        print(filename)
        file = open(filename, "wb")
        # 执行报告写入
        runner = HTMLTestRunner(stream=file, title="添加员工测试报告", description="用例执行情况:")
        # stream：是指定测试报告文件
        # title：指定报告的标题
        # description:指定报告的副标题
        # 执行测试用例
        runner.run(suite)
        time.sleep(3)
        print(file.closed)
        # 进行文件关闭
        file.close()
        print(file.closed)
A=Ylzx()
A.ylzx(Crmxz('test_xz1'))
