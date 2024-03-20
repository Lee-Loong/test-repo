import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import os
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
path1 = sys.path
path1.append(path)
from SEDLogin import SEDLogin
from SetWeiBaoGongDan import SetWeiBaoGongDan


class SED_sbzx_sbgl_sbwb_wbgd(unittest.TestCase):
    '''维保工单测试'''
    def setUp(self):
        self.ll = SEDLogin()
        self.driver = webdriver.Edge()
        self.ll.login(self.driver)
        self.ll.taochong(self.driver)
        self.wbgd = SetWeiBaoGongDan()
        self.wbgd.wbtiaozhuan(self.driver)

    def test_001_xinzeng_01(self):
        '''新增维保工单正向测试'''
        # 点击新增临时维保按钮，弹出新增弹窗
        ele = WebDriverWait(self.driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//span[text()="新增临时维保"]')), "找不到元素")
        if ele:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        # self.driver.find_element('xpath', '//span[text()="新增临时维保"]').click()
        # 选择最终验收人
        ele = WebDriverWait(self.driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请选择最终验收人"]')), "找不到元素")
        if ele:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        # self.driver.find_element('xpath', '//input[@placeholder="请选择最终验收人"]').click()
        self.driver.find_element('xpath', '//span[text()="设备班长"]').click()
        # 选择设备名称
        self.driver.find_element('xpath', '//input[@placeholder="请选择设备名称"]').click()
        time.sleep(1)
        self.driver.find_element('xpath', '//span[text()="一期3#提升潜污泵"]').click()
        # 选择维保要素
        element = self.driver.find_element('xpath', '//input[@placeholder="请选择维保要素"]')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element('xpath', '//span[text()="[整机]wx-维保名称-002"]').click()
        # self.driver.find_element('xpath','//input[@placeholder="请选择维保要素"]').click()
        self.driver.find_element('xpath', '//label[text()="维保内容"]').click()
        #输入维保内容，用作断言
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.driver.find_element('xpath', '//input[@placeholder="请填写维保内容"]').clear()
        self.driver.find_element('xpath', '//input[@placeholder="请填写维保内容"]').send_keys(now)
        # 输入标准工时
        self.driver.find_element('xpath', '//input[@placeholder="请填写标准工时"]').clear()
        self.driver.find_element('xpath', '//input[@placeholder="请填写标准工时"]').send_keys("8")
        # 选择计划开始日期
        self.driver.find_element('xpath', '//input[@placeholder="请选择计划开始日期"]').click()
        ele = WebDriverWait(self.driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"此刻")]')), "找不到元素")
        if ele:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        # self.driver.find_element('xpath', '//span[contains(text(),"此刻")]').click()
        # 获取维保内容文本框内的值，作为断言的预期结果
        expectValue = self.driver.find_element('xpath', '//input[@placeholder="请填写维保内容"]').get_attribute("value")
        # 点击保存提交按钮，提交数据
        self.driver.find_element('xpath', '//span[text()="保存提交"]').click()
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保内容
        self.driver.find_element('xpath', '//div[text()=" 维保内容 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言
        actualValue = self.driver.find_element('xpath', '//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def test_002_xiafa_01(self):
        '''下发维保工单正向测试'''
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 点击下发按钮
        ele = WebDriverWait(self.driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '(//span[text()="下发"])[1]')), "找不到元素")
        if ele:
            # self.driver.execute_script("arguments[0].click();", ele)
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        # xiafa = self.driver.find_element('xpath', '(//span[text()="下发"])[1]')
        # self.driver.execute_script("arguments[0].click();", xiafa)
        # 选择执行人
        self.driver.find_element('xpath', '//input[@placeholder="请选择执行人"]').click()
        time.sleep(1)
        self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="朱成成"]').click()
        # 选择协助人
        xxz = self.driver.find_element('xpath', '//input[@placeholder="请选择协助人"]')
        self.driver.execute_script("arguments[0].click();", xxz)
        time.sleep(1)
        xzr = self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="朱成成"]')
        self.driver.execute_script("arguments[0].click();", xzr)
        # ActionChains(self.driver).move_to_element(xzr).perform()
        self.driver.find_element('xpath', '//label[text()="协助人"]').click()
        # 获取判断值pd
        pd = self.driver.find_element('xpath', '//span[text()="工单编号"]/following-sibling::span').text
        # 点击保存提交按钮
        self.driver.find_element('xpath', '//button[@data-v-2770f681]').click()
        # 初始化查询
        self.wbgd.chaxun(self.driver)
        # 输入判断值pd的工单进行查询
        self.driver.find_element('xpath', '(//input[@placeholder="请输入内容"])[1]').send_keys(pd)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保状态
        self.driver.find_element('xpath', '//div[text()=" 状态 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言

        expectValue = "待维保"
        actualValue = self.driver.find_element('xpath', '//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def test_003_weibao_01(self):
        '''维保维保工单正向测试'''
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 点击维保按钮
        xiafa = self.driver.find_element('xpath', '(//span[text()="维保"])[1]')
        self.driver.execute_script("arguments[0].click();", xiafa)
        # 选择是否执行
        self.driver.find_element('xpath', '//input[@placeholder="请选择是否执行"]').click()
        self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="是"]').click()
        # 填写维保记录
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写维保记录"]').send_keys("已经维保完毕！")
        # 选择协助人
        xxz = self.driver.find_element('xpath', '//input[@placeholder="请选择协助人"]')
        self.driver.execute_script("arguments[0].click();", xxz)
        time.sleep(1)
        self.driver.find_element('xpath', '//div[@x-placement="top-start"]//span[text()="朱成成"]').click()
        # xzr = self.driver.find_element('xpath','//div[@x-placement="bottom-start"]//span[text()="朱成成"]')
        # self.driver.execute_script("arguments[0].click();", xzr)
        # ActionChains(self.driver).move_to_element(xzr).perform()
        self.driver.find_element('xpath', '//label[text()="协助人"]').click()
        # 填写实际工时
        self.driver.find_element('xpath', '//input[@placeholder="请填写实际工时"]').send_keys("6")
        # 填写总费用
        self.driver.find_element('xpath', '//input[@placeholder="请填写总费用(元)"]').send_keys("6000")
        # 填写材料消耗
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写材料消耗"]').send_keys("铝合金止逆阀")
        # 填写检测参数
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写检测参数"]').send_keys("速率=100M^3/H")
        # 获取判断值pd
        pd = self.driver.find_element('xpath', '(//span[text()="工单编号"]/following-sibling::span)[1]').text
        # 点击保存提交按钮
        self.driver.find_element('xpath', '//span[text()="保存提交"]//parent::button').click()
        # 初始化查询
        self.wbgd.chaxun(self.driver)
        # 输入判断值pd的工单进行查询
        self.driver.find_element('xpath', '(//input[@placeholder="请输入内容"])[1]').send_keys(pd)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保状态
        self.driver.find_element('xpath', '//div[text()=" 状态 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言
        expectValue = "待维修班长验收"
        actualValue = self.driver.find_element('xpath','//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def test_004_bzyanshou_01(self):
        '''维修班长验收维保工单正向测试'''
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 点击维修班长验收按钮
        bzys = self.driver.find_element('xpath', '(//span[text()="维修班长验收"])[1]')
        self.driver.execute_script("arguments[0].click();", bzys)
        # 选择验收意见
        self.driver.find_element('xpath', '//input[@placeholder="请选择验收意见"]').click()
        self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="通过"]').click()
        # 填写验收描述
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写验收描述"]').send_keys("已经验收完毕！")
        # 获取判断值pd
        pd = self.driver.find_element('xpath', '(//span[text()="工单编号"]/following-sibling::span)[1]').text
        # 点击保存提交按钮
        self.driver.find_element('xpath', '//span[text()="保存提交"]//parent::button').click()
        # 初始化查询
        self.wbgd.chaxun(self.driver)
        # 输入判断值pd的工单进行查询
        self.driver.find_element('xpath', '(//input[@placeholder="请输入内容"])[1]').send_keys(pd)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保状态
        self.driver.find_element('xpath', '//div[text()=" 状态 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言
        expectValue = "待运营班长验收"
        actualValue = self.driver.find_element('xpath', '//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def test_005_yybzyanshou_01(self):
        '''运营班长验收维保工单正向测试'''
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 点击维修班长验收按钮
        yybzys = self.driver.find_element('xpath', '(//span[text()="运营班长验收"])[1]')
        self.driver.execute_script("arguments[0].click();", yybzys)
        # 选择验收意见
        self.driver.find_element('xpath', '//input[@placeholder="请选择验收意见"]').click()
        self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="通过"]').click()
        # 填写验收描述
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写验收描述"]').send_keys("已经验收完毕！")
        # 获取判断值pd
        pd = self.driver.find_element('xpath', '(//span[text()="工单编号"]/following-sibling::span)[1]').text
        # 点击保存提交按钮
        self.driver.find_element('xpath', '//span[text()="保存提交"]//parent::button').click()
        # 初始化查询
        self.wbgd.chaxun(self.driver)
        # 输入判断值pd的工单进行查询
        self.driver.find_element('xpath', '(//input[@placeholder="请输入内容"])[1]').send_keys(pd)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保状态
        self.driver.find_element('xpath', '//div[text()=" 状态 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言
        expectValue = "待经理验收"
        actualValue = self.driver.find_element('xpath', '//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def test_006_jlyanshou_01(self):
        '''经理验收维保工单正向测试'''
        # 调用恢复初始查询条件的方法
        self.wbgd.chaxuntoday(self.driver)
        # 点击维修班长验收按钮
        jlys = self.driver.find_element('xpath', '(//span[text()="经理验收"])[1]')
        self.driver.execute_script("arguments[0].click();", jlys)
        # 选择验收意见
        self.driver.find_element('xpath', '//input[@placeholder="请选择验收意见"]').click()
        self.driver.find_element('xpath', '//div[@x-placement="bottom-start"]//span[text()="通过"]').click()
        # 填写验收描述
        self.driver.find_element('xpath', '//textarea[@placeholder="请填写验收描述"]').send_keys("已经验收完毕！")
        # 获取判断值pd
        pd = self.driver.find_element('xpath', '(//span[text()="工单编号"]/following-sibling::span)[1]').text
        # 点击保存提交按钮
        self.driver.find_element('xpath', '//span[text()="保存提交"]//parent::button').click()
        # 初始化查询
        self.wbgd.chaxun(self.driver)
        # 输入判断值pd的工单进行查询
        self.driver.find_element('xpath', '(//input[@placeholder="请输入内容"])[1]').send_keys(pd)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()
        # 调用自定义列的方法，默认全不选
        self.wbgd.zidingyilie(self.driver)
        # 选择维保状态
        self.driver.find_element('xpath', '//div[text()=" 状态 "]').click()
        # 点击页面元素，关闭自定义列窗口
        self.driver.find_element('xpath', '// div[contains(text(), "已选择")]').click()
        # 断言
        expectValue = "已完成"
        actualValue = self.driver.find_element('xpath', '//table[@class="el-table__body"]').text
        self.assertIn(expectValue, actualValue)

    def tearDown(self):
        self.ll.logout(self.driver)
        self.ll.qiut_browser(self.driver)

if __name__ == '__main__':
    unittest.main()
