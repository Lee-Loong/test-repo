#需要设计一个方法，这个方法可以提供注册的基本步骤，通过参数传数据
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SEDLogin():
    def login(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        #打开登录页面
        self.driver.get("http://39.99.202.162:8181/")
        driver.maximize_window()
        #输入用户名
        self.driver.find_element('xpath', '//*[@id="username"]').send_keys("adminUser")
        #输入密码
        self.driver.find_element('xpath', '//*[@id="password"]').send_keys("Admin2021")
        #点击登录按钮
        self.driver.find_element('xpath', '//*[@id="btnNoCaptcha"]').click()

    def login2(self,driver):
        self.driver = driver
        #输入用户名
        self.driver.find_element('xpath', '//*[@id="username"]').send_keys("niukun")
        #输入密码
        self.driver.find_element('xpath', '//*[@id="password"]').send_keys("123456")
        #点击登录按钮
        self.driver.find_element('xpath', '//*[@id="btnNoCaptcha"]').click()

    def taochong(self,driver):
        self.driver = driver
        self.driver.find_element('xpath', '//span[text()=" 天津创业环保集团 "]').click()
        self.driver.find_element('xpath', '//span[text()="天津创业环保集团"]').click()
        self.driver.find_element('xpath', '//span[text()="长三角区域"]//ancestor::div[contains(@style,"padding-left")]/span').click()
        self.driver.find_element('xpath', '//span[text()="合肥创业水务有限公司"]//ancestor::div[contains(@style,"padding-left")]/span').click()
        ele = WebDriverWait(driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH, '//span[text()="合肥陶冲"]')), "找不到元素")
        if ele:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            print(ele)
        time.sleep(1)
        # self.driver.find_element('xpath', '//span[text()="合肥陶冲"]').click()

    def logout(self,driver):
        self.driver = driver
        self.driver.find_element('xpath', '//i[@data-v-30d65868 and @class="el-icon-arrow-down el-icon--right"]').click()
        element = driver.find_element('xpath', '//span[text()="退出登录"]')
        driver.execute_script("arguments[0].click();", element)
        ActionChains(driver).send_keys(Keys.ENTER).perform()

    #退出浏览器对象
    def qiut_browser(self,driver):
        self.driver = driver
        self.driver.quit()


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    aa = SEDLogin()
    aa.login(driver)
    aa.taochong(driver)
    aa.logout(driver)
    aa.qiut_browser(driver)

