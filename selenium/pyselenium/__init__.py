
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def run_selenium(debug=True):

    driver = get_driver(debug)

    driver.get("http://vedmark.ru")

    # elem = driver.find_element_by_name("q")
    elem = driver.find_elements_by_tag_name('a')[7]
    # elem.send_keys("Hello WebDriver!")
    # elem.submit()
    elem.click()

    print(driver.title)

    if not debug: driver.quit()


def get_driver(debug: bool):
    options = Options()
    options.headless = not debug
    driver = webdriver.Firefox(options=options)
    return driver
