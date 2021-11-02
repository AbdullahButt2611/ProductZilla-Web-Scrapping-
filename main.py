import sys
import PyQt5.uic
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
from lxml import html
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from decimal import Decimal
from lxml import html
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait



classObjects = []
listDaraz=[ 'https://www.daraz.pk/smartphones/?page={}&spm=a2a0e.searchlistcategory.cate_1.1.2e3c7242Kuty9m',
          'https://www.daraz.pk/mobiles-tablets-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_2.1.6587c414XLrCZ9',
          'https://www.daraz.pk/home-appliances/?page={}&spm=a2a0e.searchlistcategory.cate_3.6.5ca57acaDKnCAX',
          'https://www.daraz.pk/computing-peripherals-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_2.5.7e4a7f01R8haY7',
          'https://www.daraz.pk/bath-body/?page={}&spm=a2a0e.searchlistcategory.cate_4.1.717f6c37SVBAad',
          'https://www.daraz.pk/remote-control-toys-and-play-vehicles/?page={}&spm=a2a0e.searchlistcategory.cate_5.6.1fd784faBcJAtQ',
          'https://www.daraz.pk/health-beauty-tools/?page={}&spm=a2a0e.searchlistcategory.cate_4.2.367e29c3kXWyv0',
          'https://www.daraz.pk/womens-make-up/?page={}&spm=a2a0e.searchlistcategory.cate_4.5.481f6337vEz4dh']
listDaraz1=[ 'https://www.daraz.pk/smartphones/?page={}&spm=a2a0e.searchlistcategory.cate_1.1.2e3c7242Kuty9m',
          'https://www.daraz.pk/mobiles-tablets-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_2.1.6587c414XLrCZ9']
class productzilla:
    def __init__(self,name,price,solditems,ratings,taxes,shopname,Topseller):
        self.name=name
        self.price=price
        self.solditems = solditems
        self.ratings = ratings
        self.taxes = taxes
        self.shopname = shopname
        self.topSeller = Topseller


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tabletutorial.ui",self)
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,350)
        self.btn.clicked.connect(lambda: self.scrap())
        self.loaddata()
    def scrap(self):
        thread = threading.Thread(target=self.scrapData)
        thread.start()
        print(threading.activeCount())

    def loaddata(self):
        row=0
        self.tableWidget.setRowCount(len(classObjects))
        for person in classObjects:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person.name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person.price)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person.solditems)))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person.ratings)))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(person.taxes)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(person.shopname)))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(person.topSeller)))
            row=row+1

    def solditemsno(self):
        value=randint(5,400)
        return value

    def ratingsitem(self,solditems):
        if solditems>=0 and solditems<50:
            return 1.0
        elif solditems>=50 and solditems<100:
            return 2.0
        elif solditems>=100 and solditems<150:
            return 2.5
        elif solditems>150 and solditems<250:
            return 3.3
        elif solditems>250 and solditems<350:
            return 3.8
        elif solditems>350 and solditems<375:
            return 4.2
        elif solditems>375 and solditems<400:
            return 4.75

    def checkTopseller(self,ratingss):
        if ratingss!=None:
            if ratingss>=3.8:
                return 'yes'
            else:
                return 'no'
        else:
            return 'no'

    def taxx(self,price):
        x=price/100
        c=round(x,2)
        return c

    def scrapData(self):
        driver = webdriver.Chrome(executable_path=r'C:\Users\qaziz\chromedriver.exe')
        driver.maximize_window()
        for link in listDaraz1:
            for pageno in range(1, 3):

                driver.get(link.format(pageno))

                driver.execute_script('window.scrollTo(0,(document.body.scrollHeight)/4)')
                sleep(2)
                driver.execute_script('window.scrollTo((document.body.scrollHeight)/4,(document.body.scrollHeight)/2)')
                sleep(2)
                driver.execute_script('window.scrollTo(((document.body.scrollHeight)/2),(((document.body.scrollHeight)/2)+(document.body.scrollHeight)/4))')
                sleep(2)
                driver.execute_script('window.scrollTo((((document.body.scrollHeight)/2) + (document.body.scrollHeight)/4),document.body.scrollHeight)')
                sleep(0.5)

                source = driver.page_source
                soup = BeautifulSoup(source)

                mainDiv = driver.find_element_by_class_name("c1_t2i")
                mobileDetails = mainDiv.find_elements_by_class_name("c3KeDq")
                for mobileDetail in mobileDetails:
                    price = 0
                    name = str(mobileDetail.find_element_by_class_name("c16H9d").text)
                    price = str(mobileDetail.find_element_by_class_name("c13VH6").text)

                    price = price.split(' ')[1]

                    price = float(price.replace(',', ''))
                    price = price / 170
                    try:
                        solditem = str(mobileDetail.find_element_by_class_name("c3XbGJ").text)
                        solditem = str(mobileDetail.find_element_by_class_name("c3XbGJ").text)
                        solditem = solditem.replace('(', '')
                        solditem = int(solditem.replace(')', ''))
                    except:
                        solditem = 0
                    rating = self.ratingsitem(solditem)
                    tax = self.taxx(price)
                    topseller = self.checkTopseller(rating)

                    store_name = str(mobileDetail.find_element_by_class_name("c2i43- ").text)
                    store_name = store_name + "Store"
                    data = productzilla(name, price,solditem,rating,tax,store_name,topseller)
                    classObjects.append(data)
                mainwindow.loaddata()






# main

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")