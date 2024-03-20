#需要设计一个方法，这个方法可以提供注册的基本步骤，通过参数传数据
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SetWeiBaoGongDan():
    def wbtiaozhuan(self,driver):
        self.driver = driver
        # 跳转到维保工单页面
        self.driver.get("http://39.99.202.162:8181/#/asset/maintenance/maintenanceTaskList")


    def chaxuntoday(self, driver):
        self.driver = driver
        #初始化筛选条件并关闭弹窗
        # ele = WebDriverWait(driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//img[@title="个性化筛选条件"]')), "找不到元素")
        # if ele:
        #     # self.driver.execute_script("arguments[0].click();", ele)
        #     ele.click()
        # else:
        #     print(ele)
        time.sleep(3)
        self.driver.find_element('xpath', '//img[@title="个性化筛选条件"]').click()
        self.driver.find_element('xpath', '//span[text()="恢复初始查询条件"]').click()
        self.driver.find_element('xpath', '//span[text()="设置查询条件"]//parent::div/button/i').click()
        #查询工单编号为当前日期的工单数据
        today = time.strftime("%Y-%m-%d")
        self.driver.find_element('xpath', '//input[@placeholder="开始日期"]').send_keys(today)
        self.driver.find_element('xpath', '//input[@placeholder="结束日期"]').send_keys(today)
        self.driver.find_element('xpath', '//div[text()="计划开始日期"]').click()
        self.driver.find_element('xpath', '//span[text()="查询"]').click()

    def chaxun(self, driver):
        self.driver = driver
        time.sleep(2)
        #初始化筛选条件并关闭弹窗
        self.driver.find_element('xpath', '//img[@title="个性化筛选条件"]').click()
        # shaixuan = self.driver.find_element('xpath', '//img[@title="个性化筛选条件"]')
        # self.driver.execute_script("arguments[0].click();", shaixuan)
        self.driver.find_element('xpath', '//span[text()="恢复初始查询条件"]').click()
        self.driver.find_element('xpath', '//span[text()="设置查询条件"]//parent::div/button/i').click()

    def zidingyilie(self,driver):
        self.driver = driver
        # 自定义列表判断是否全选，如果没有全选,点击两次全选按钮，如果全选，点击全选按钮
        ele = WebDriverWait(driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//span[text()="自定义列"]')), "找不到元素")
        if ele:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        # self.driver.find_element('xpath', '//span[text()="自定义列"]').click()
        # time.sleep(5)
        quanxuan = self.driver.find_element('xpath', '// span[text() = "全选"]')
        tiaojian = self.driver.find_element('xpath', '// span[text() = "全选"] // parent::label').get_attribute("class")
        if tiaojian == "el-checkbox is-checked":
            quanxuan.click()
        else:
            quanxuan.click()
            # time.sleep(1)
            quanxuan.click()


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    aa = SEDLogin()
    aa.login(driver)
    aa.taochong(driver)
    aa.logout(driver)
    aa.qiut_browser(driver)

