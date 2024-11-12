import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 指定ChromeDriver的路径
driver_path = "/Users/hanzhiqiang/Downloads/chromedriver-mac-x64/chromedriver"


def alert_stop(driver):
    # 使用JavaScript的alert函数显示一个对话框
    driver.execute_script(f"alert('test done will be closed');")
    time.sleep(3)

    print(f"test end")
    driver.quit()  # 所有测试完成后，关闭浏览器


def test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("http://baidu.com")
    logging.info(f"")

    # input xpath
    # /html/body/div/div[2]/div[5]/div[1]/div/form/span[1]/input
    # document.querySelector("#s_kw_wrap")
    element = driver.find_element(By.XPATH, '//*[@id="kw"]')

    driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("admin")
    element.send_keys(Keys.RETURN)
    # 现在你可以使用driver来控制浏览器了
    driver.find_element(By.XPATH, "//input[@id='su']").click()

    # 使用JavaScript的alert函数显示一个对话框
    driver.execute_script(f"alert('test done will be closed');")
    time.sleep(3)

    print(f"test end")
    driver.quit()  # 所有测试完成后，关闭浏览器


def test_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("http://baidu.com")

    driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
    # 等待按钮可以点击后再执行alert_stop
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='TANGRAM__PSP_11__regLink']")))

    # TODO clear input
    # driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName_clearbtn"]').clear()
    # driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password_clearbtn"]').clear()
    driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__userName']").send_keys("17600110411")
    driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__password']").send_keys("tars@123456")

    ele = driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__isAgree']")
    is_checked = ele.is_selected()
    if not is_checked:
        ele.click()
    else:
        print("already checked")


    driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__submit']").click()

    time.sleep(5)
    alert_stop(driver)


if __name__ == "__main__":
    print(f"test start")
    test_login()
    # test()
