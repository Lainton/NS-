from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#驱动位置
chromeDriver = '/Users/ansel/PycharmProjects/lrcGenerater/chromedriver'

browser = webdriver.Chrome(chromeDriver)
wait = WebDriverWait(browser, 10)

#宝贝url
url = 'https://item.taobao.com/item.htm?spm=2013.1.w4023-2235726351.11.78f21badzpajdS&id=559505733763'

#游戏版本
versions = ['普通版', '首发版', '特典版', '豪华版', '收藏版', '年度版', '完全版']

def get_item_price():
    price = ''
    try:
        price = browser.find_element_by_id('J_PromoPriceNum').text
    except NoSuchElementException:
        print('[!!!] 无价格信息节点')
    return price


def get_price(item):
    #单击类型
    item.click()

    #获取价格
    return get_item_price()


def get_info():
    version_price = {}

    try:
        #单击关闭登入按钮
        browser.find_element_by_id('sufei-dialog-close').click()
    except NoSuchElementException:
        print('[!!!]没有关闭框')

    priceBox = browser.find_element_by_css_selector('.J_TSaleProp.tb-clearfix')
    lis = priceBox.find_elements_by_tag_name('li')

    #遍历每个li  看是不是需要 获取价格的版本
    for item in lis:
        #获取li 的text内容, 如果是需要的li 则 获取价格
        if item.text in versions:
            price = get_price(item)
            version_price[item.text] = price
    
    return version_price


def get_page():
    try:
        browser.get(url)
        #看获取到price_box没
        priceBox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.J_TSaleProp.tb-clearfix')))

        #获取到了就进行解析
        get_info()
    except TimeoutException:
        get_page()
    finally:
        browser.close()
    

get_page()