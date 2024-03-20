#需要设计一个方法，这个方法可以提供注册的基本步骤，通过参数传数据
from datetime import datetime
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class SetWeiBaoJiHua():
    def tiaozhuan(self,driver):
        self.driver = driver
        # 跳转到维保计划页面
        self.driver.get("http://39.99.202.162:8181/#/equipment_maintenance_plan/index.vue")

    def chaxuntoday(self, driver):
        self.driver = driver
        # 选择起止时间为当前年月日到+1年的年月日
        today = time.strftime("%Y-%m-%d")
        endday = (datetime.now() + relativedelta(years=1)).strftime("%Y-%m-%d")
        self.driver.find_element('xpath', '//input[@placeholder="开始日期"]').send_keys(today)
        self.driver.find_element('xpath', '//input[@placeholder="结束日期"]').send_keys(endday)
        self.driver.find_element('xpath', '//span[text()="查询"]').click()

    def tiaozhuangd(self, driver):
        self.driver = driver
        # 点击工单按钮
        ele = self.driver.find_element('xpath', '(//span[text()="工单"])[1]')
        self.driver.execute_script("arguments[0].click();", ele)




if __name__ == '__main__':
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    aa = SEDLogin()
    aa.login(driver)
    aa.taochong(driver)
    aa.logout(driver)
    aa.qiut_browser(driver)

