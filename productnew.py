from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep

names = []
prices = []
solditems = []
ratings = []
taxes = []
store_names = []
topseller=[]







driver = webdriver.Chrome(executable_path=r'C:\Users\qaziz\chromedriver.exe')
driver.maximize_window()
for pag_no in range(1, 30):
    driver.get(
        "https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=smart+watches&ltype=wholesale&SortType=default&page={}".format(
            pag_no))

    driver.execute_script('window.scrollTo(0,(document.body.scrollHeight)/4)')
    sleep(2)
    driver.execute_script('window.scrollTo((document.body.scrollHeight)/4,(document.body.scrollHeight)/2)')
    sleep(2)
    driver.execute_script(
        'window.scrollTo(((document.body.scrollHeight)/2),(((document.body.scrollHeight)/2)+(document.body.scrollHeight)/4))')
    sleep(2)
    driver.execute_script(
        'window.scrollTo((((document.body.scrollHeight)/2) + (document.body.scrollHeight)/4),document.body.scrollHeight)')
    sleep(1)

    source = driver.page_source
    soup = BeautifulSoup(source)

    mainDiv = driver.find_element_by_class_name("JIIxO")
    mobileDetails = mainDiv.find_elements_by_class_name("_1OUGS")
    for mobileDetail in mobileDetails:
        # rating = mobileDetail.find_element_by_class_name("_1hEhM").text)
        name = str(mobileDetail.find_element_by_class_name("awV9E").text)
        price = str(mobileDetail.find_element_by_class_name("_12A8D").text)

        # solditem = str(mobileDetail.find_element_by_class_name("_1YxeD").text)

        # tax = str(mobileDetail.find_element_by_class_name("ZCLbI").text)
        store_name = str(mobileDetail.find_element_by_class_name("_2lsU7").text)

        names.append(name)
        prices.append(price)
        # solditems.append(solditem)
        # ratings.append(rating)
        # taxes.append(tax)
        store_names.append(store_name)

data = pandas.DataFrame({"Names": names, "prices": prices, "Store name": store_names})
data.to_csv("scrap.csv", index=False)