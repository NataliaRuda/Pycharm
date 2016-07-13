# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://vulkanstavka.stage-00.ginsp.net ")

element = driver.find_element_by_link_text("Начать выигрывать!")
element.click()
time.sleep(2)

login = driver.find_element_by_id("popup-register-bonus-email")
ts = (time.time())
email = "test%d%s" % (ts, "@test.com")
login.send_keys(email)

password = driver.find_element_by_id("popup-register-bonus-password")
password.send_keys("user123")
password.send_keys(Keys.ENTER)
time.sleep(8)

# register = driver.find_element_by_link_text("Регистрация")
# register.click()
# time.sleep(7)

close = driver.find_element_by_css_selector("#popup-confirm-email > div.popup-container.popup-md > div.popup-close")
close.click()

logout = driver.find_element_by_id("dropdown-user")
logout.click()
out = driver.find_element_by_link_text("Выход")
out.click()
time.sleep(7)

signin = driver.find_element_by_link_text("Войти")
signin.click()
signin_login = driver.find_element_by_id("popup-sign-in-login")
signin_login.send_keys("test1468328630@test.com")
si_pass = driver.find_element_by_id("popup-sign-in-password")
si_pass.send_keys("user123")
si_pass.send_keys(Keys.ENTER)
time.sleep(5)

driver.get("http://vulkanstavka.stage-00.ginsp.net/igrovye-avtomaty-real/crazy-monkey")
time.sleep(3)
cashier = driver.find_element_by_id("popup-cashier-deposit")
if cashier.is_displayed():
    print('TRUE')
else:
    print('FALSE')

time.sleep(10)

driver.back()

logout = driver.find_element_by_id("dropdown-user")
logout.click()
out = driver.find_element_by_link_text("Выход")
out.click()

# back = driver.find_element_by_xpath("//*[@id='popup-cashier-deposit']/div[2]/div[1])
# back.click()
print('smth')

