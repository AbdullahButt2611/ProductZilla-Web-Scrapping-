from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep
from random import randint
from decimal import Decimal

names = []
prices = []
solditems = []
ratings = []
taxes = []
store_names = []
toppSellers = []


def solditemsno():
    value = randint(5, 400)
    return value


def ratingsitem(solditems):
    if solditems > 0 and solditems < 50:
        return 1.0
    elif solditems >= 50 and solditems < 100:
        return 2.0
    elif solditems >= 100 and solditems < 150:
        return 2.5
    elif solditems > 150 and solditems < 250:
        return 3.3
    elif solditems > 250 and solditems < 350:
        return 3.8
    elif solditems > 350 and solditems < 375:
        return 4.2
    elif solditems > 375 and solditems < 400:
        return 4.75


def checkTopseller(ratingss):
    if ratingss != None:
        if ratingss >= 4:
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'


def taxx(price):
    x = price / 100
    return x


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
        price = price.split(' ')[1]
        price = float(price.strip('$'))

        solditem = solditemsno()
        rating = ratingsitem(solditem)
        tax = taxx(price)
        topseller = checkTopseller(rating)
        # solditem = str(mobileDetail.find_element_by_class_name("_1YxeD").text)

        # tax = str(mobileDetail.find_element_by_class_name("ZCLbI").text)
        store_name = str(mobileDetail.find_element_by_class_name("_2lsU7").text)

        names.append(name)
        prices.append(price)
        solditems.append(solditem)
        ratings.append(rating)
        toppSellers.append(topseller)
        store_names.append(store_name)
        taxes.append(tax)

data = pandas.DataFrame(
    {"Names": names, "prices": prices, "Store name": store_names, "Sold items ": solditems, "ToppSeller": toppSellers,
     "ratings": ratings, "Shipping taxes": taxes})
data.to_csv("ScrapFileOrignal.csv", index=False)
