import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_test():
    options = Options()
    #chromeOptions.add_argument("--remote-debugging-port=92222")  

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("start-maximized")
    driver = new_func(options)
    driver.get("http://127.0.0.1:8000/")
    time.sleep(10)

def new_func(options):
    driver = webdriver.Chrome(executable_path=r"/home/gleb/WebDriver/PATH/chromedriver", chrome_options=options)
    return driver

    #textarea = driver.find_element(By.CSS_SELECTOR, "#city")
    #textarea.send_keys("get(Moscow)")
    #time.sleep(8)
    #submit_button = driver.find_element(By.CSS_SELECTOR, ".mt-2")
    #submit_button.click()
    #time.sleep(8)
    #print(submit_button[0].text)


if __name__ == "__main__":
    get_test()
