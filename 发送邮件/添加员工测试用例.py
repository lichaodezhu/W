import unittest
from crm自动化测试.员工新增.发送邮件 import 自动生成测试数据
#HTMLTestRunner用来生成HTML格式的测试报告
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
class DL():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/crm/')
    driver.maximize_window()
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/'
                                         'tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input').send_keys('admin')
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/'
                                         'tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input').send_keys('123456')
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/'
                                         'tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/div/input').click()
    time.sleep(1)

class Crmxz(unittest.TestCase,DL):
    def setUp(self) -> None:
        print('测试开始《《《《《《《《《《《《《《《《《')
    def tearDown(self) -> None:
        text=DL.driver.switch_to.alert.text
        print(text)
        print('测试结束》》》》》》》》》》》》》》》》》')

    def test_xz1(self):
        driver=DL.driver
        driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[1])  # 切换表单
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/'
                                     'tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]').click()  # 点击管理员
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/'
                                     'tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()  # 点击添加员工
        driver.switch_to.default_content()  # 切换至默认表单
        time.sleep(1)
        driver.switch_to.frame('mainFrame')  # 切换至新增员工表单
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[2]/input').send_keys(自动生成测试数据.A)  # 输入姓名
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[2]/input').send_keys(自动生成测试数据.B)  # 输入年龄
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[2]/select').click()  # 输入性别
        se = driver.find_element_by_name('userSex')
        Select(se).select_by_value(自动生成测试数据.C)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[5]/td[2]/select').click()  # 点击学历
        time.sleep(1)
        se = driver.find_element_by_name('userDiploma')
        Select(se).select_by_index(自动生成测试数据.D)  # 学历
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[6]/td[2]/select').click()  # 点击部门
        time.sleep(1)
        se1 = driver.find_element_by_name('departmentId')
        time.sleep(1)
        Select(se1).select_by_value(自动生成测试数据.E)  # 部门
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[2]/input').send_keys(自动生成测试数据.F)  # 座机号填写
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[2]/input').send_keys('1325')  # 工资卡号填写
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[2]/input[1]').send_keys(
            自动生成测试数据.H)  # 身份证号填写
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[10]/td[2]/input').send_keys(自动生成测试数据.I)  # 添加入填写
        driver.find_element_by_name('userNum').send_keys(自动生成测试数据.J)  # 账号填写
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[4]/input').send_keys(自动生成测试数据.K)  # 密码填写
        driver.find_element_by_name('userNation').send_keys('123')  # 民族填写
        driver.find_element_by_name('isMarried').click()  # 婚姻状况
        time.sleep(1)
        se2 = driver.find_element_by_name('isMarried')  # 婚姻状况
        Select(se2).select_by_index(自动生成测试数据.L)
        driver.find_element_by_name('roleId').click()  # 管理员
        time.sleep(1)
        se3 = driver.find_element_by_name('roleId')
        time.sleep(1)
        Select(se3).select_by_value(自动生成测试数据.M)
        driver.find_element_by_name('userIntest').send_keys('32132')  # 爱好
        time.sleep(1)
        driver.find_element_by_name('userMobile').send_keys(自动生成测试数据.N)  # 手机
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[4]/input').send_keys('2134')  # 地址
        driver.find_element_by_name('userEmail').send_keys(自动生成测试数据.O)  # 邮箱
        driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()
        driver.switch_to.alert.accept()
        time.sleep(1)
        DL.driver.quit()


    def test_xz2(self):
        driver=DL.driver
        driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[1])  # 切换表单
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/'
                                     'tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]').click()  # 点击管理员
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/'
                                    'tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()  # 点击添加员工
        driver.switch_to.default_content()  # 切换至默认表单
        time.sleep(1)
        driver.switch_to.frame('mainFrame')  # 切换至新增员工表单
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[2]/input').send_keys(自动生成测试数据.A)  # 输入姓名
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[2]/input').send_keys(自动生成测试数据.B)  # 输入年龄
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[2]/select').click()  # 输入性别
        se = driver.find_element_by_name('userSex')
        Select(se).select_by_value(自动生成测试数据.C)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[5]/td[2]/select').click()  # 点击学历
        time.sleep(1)
        se = driver.find_element_by_name('userDiploma')
        Select(se).select_by_index(自动生成测试数据.D)  # 学历
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[6]/td[2]/select').click()  # 点击部门
        time.sleep(1)
        se1 = driver.find_element_by_name('departmentId')
        time.sleep(1)
        Select(se1).select_by_value(自动生成测试数据.E)  # 部门
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[2]/input').send_keys(自动生成测试数据.F)  # 座机号填写
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[2]/input').send_keys('1325')  # 工资卡号填写
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[2]/input[1]').send_keys(
            自动生成测试数据.H)  # 身份证号填写
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[10]/td[2]/input').send_keys(自动生成测试数据.I)  # 添加入填写
        driver.find_element_by_name('userNum').send_keys(自动生成测试数据.J)  # 账号填写
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[4]/input').send_keys(自动生成测试数据.K)  # 密码填写
        driver.find_element_by_name('userNation').send_keys('123')  # 民族填写
        driver.find_element_by_name('isMarried').click()  # 婚姻状况
        time.sleep(1)
        se2 = driver.find_element_by_name('isMarried')  # 婚姻状况
        Select(se2).select_by_index(自动生成测试数据.L)
        driver.find_element_by_name('roleId').click()  # 管理员
        time.sleep(1)
        se3 = driver.find_element_by_name('roleId')
        time.sleep(1)
        Select(se3).select_by_value(自动生成测试数据.M)
        driver.find_element_by_name('userIntest').send_keys('32132')  # 爱好
        time.sleep(1)
        # driver.find_element_by_name('userMobile').send_keys(自动生成测试数据.N)  # 手机
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[4]/input').send_keys('2134')  # 地址
        driver.find_element_by_name('userEmail').send_keys(自动生成测试数据.O)  # 邮箱
        driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()





if __name__ == '__main__':
    unittest.main()
    # time.sleep(4)
    # #测试套件，构建测试集
    # suite=unittest.TestSuite()
    # suite.addTest(Crmxz('test_xz1'))
    # # dir='./'
    # # discover=unittest.defaultTestLoader.discover(dir,pattern='test_search')
    # #我们要新建一个用于保存我们测试结果的文件，html
    # now=time.strftime("%Y-%m-%d-%H-%M-%S")
    # print(now)
    # #定义文件的名字
    # filename=r'D:/pythonProject/venv/7.13/'+now+"_result.html"
    # print(filename)
    # file = open(filename, "wb")
    # #执行我们的报告写入
    #
    # runner=HTMLTestRunner(stream=file,title="添加员工测试报告",description="用例执行情况:")
    # #stream：是指定测试报告文件
    # #title：指定报告的标题
    # #description:指定报告的副标题
    # #执行我们测试用例
    # runner.run(suite)
    # time.sleep(3)
    # print(file.closed)
    # # 要进行关闭
    # file.close()
    # print(file.closed)