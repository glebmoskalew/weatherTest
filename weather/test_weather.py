import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def get_test():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(executable_path=r"/home/gleb/selenium_chrome/drivers/chromedriver", chrome_options=options)
    driver.get("http://127.0.0.1:8000/")
    time.sleep(10)


    textarea = driver.find_element(By.CSS_SELECTOR, "#city")
    textarea.send_keys("Moscow")
    time.sleep(8)
    submit_button = driver.find_element(By.CSS_SELECTOR, ".mt-2")
    submit_button.click()
    time.sleep(8)
    print(submit_button[0].text)


if __name__ == "__main__":
    get_test()
