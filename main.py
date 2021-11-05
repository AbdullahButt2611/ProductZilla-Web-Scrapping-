import sys
import time

import PyQt5.uic
import threading

import self as self
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QProgressBar
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
listDaraz1=[ 'https://www.daraz.pk/smartphones/?page={}&spm=a2a0e.searchlistcategory.cate_1.1.2e3c7242Kuty9m']
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
        # self.Sc = Sc
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,350)
        self.btn.clicked.connect(lambda: self.scrap())
        self.btnpause.clicked.connect(lambda:self.pause(100000))
        self.btnSort.clicked.connect(lambda: self.SortingbyTajmuls())
        #self.btnSort.clicked.connect(lambda: mergeSort(classObjects,0,len(classObjects)-1))
       # self.algoMenu.currentIndexChanged.connect(self.algoValueGetter)
        #self.sortMenu.currentIndexChanged.connect(self.sortValueGetter)
        self.progressBar=QProgressBar()

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(40)
        self.loaddata()

    def clickMethod(self):
        QMessageBox.about(self, "Fixing", "We are sorry for inconvenience")

    def prices(self):
        cs = InsertionAlgorithm()
        cs.InsertionSortNam(classObjects)
        self.loaddata()
    def SortingbyTajmuls(self):
        value=self.algoMenu.currentIndex()
        v2=self.sortMenu.currentIndex()
        if v2==4:
            self.clickMethod()
        else:
            if value == 2 :
                cs = InsertionAlgorithm()
                cs.InsertionSort(classObjects,v2)
                self.loaddata()
            elif value == 3 :
                ce = SelectionAlgorithm()
                ce.SelectionSort(classObjects,v2)
                self.loaddata()
            elif value == 4:
                ce = BubbleAlgorithm()
                ce.BubbleSort(classObjects, v2)
                self.loaddata()
            elif value == 1:

                try:
                 ce = MergeAlgorithm()
                 ce.MergeSort(classObjects,v2)
                 self.loaddata()
                except:
                  self.clickMethod()
            elif value == 5:

                try:
                 c = QuickAlgorithm()
                 c.QuickSort(classObjects,v2)
                 self.loaddata()
                except:
                  self.clickMethod()
            elif value == 8:

                try:
                    cs = InsertionAlgorithm()
                    cs.InsertionSort(classObjects, v2)
                    self.loaddata()
                except:
                    self.clickMethod()







    # main

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


    def sortValueGetter(self,i):
        print("In function")
        value = i
        sc.sortingInsertion(value)

    def algoValueGetter(self,i):
        # print("Inside Function")
        # value = productzilla.algoMenu.getCurrentIndex
        value = i
        sc.sortAlg = i


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
        p=0
        driver = webdriver.Chrome(executable_path=r'C:\Users\qaziz\chromedriver.exe')
        driver.maximize_window()
        for link in listDaraz1:
            for pageno in range(1, 2):

                driver.get(link.format(pageno))

                driver.execute_script('window.scrollTo(0,(document.body.scrollHeight)/4)')
                sleep(1)
                driver.execute_script('window.scrollTo((document.body.scrollHeight)/4,(document.body.scrollHeight)/2)')
                sleep(1)
                driver.execute_script('window.scrollTo(((document.body.scrollHeight)/2),(((document.body.scrollHeight)/2)+(document.body.scrollHeight)/4))')
                sleep(1)
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
                    if price:
                        p=p+1

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


class Sorting:
    def __init__(self,srt):
        self.sortAlg=srt

    def sortingInsertion(self,value):
        if value == 1:
            self.InsertionName(classObjects)
            self.loaddata()
        elif value == 2:
            self.InsertionPrice(classObjects)
            self.loaddata()

    def InsertionName(self):
        size = len(classObjects)

        for j in range(1, len(classObjects)):
            key = classObjects[j]  # vAlue to be added inn the Sorted PArt
            i = j - 1
            while i >= 0 and classObjects[i].name > key.name:
                classObjects[i + 1] = classObjects[i]
                i = i - 1
            # print(i+1)
            classObjects[i + 1] = key

    def InsertionPrice(self):
        size = len(classObjects)

        for j in range(1, len(classObjects)):
            key = classObjects[j]  # vAlue to be added inn the Sorted PArt
            i = j - 1
            while i >= 0 and classObjects[i].peice > key.price:
                classObjects[i + 1] = classObjects[i]
                i = i - 1
            # print(i+1)
            classObjects[i + 1] = key

class InsertionAlgorithm:

    def InsertionSort(self,arr,value):
        var=None
        if value==1:
            var="name"
        if value==2:
            var="price"
        if value==3:
            var="solditems"
        if value==4:
            var="ratings"
        if value==5:
            var="taxes"
        if value==6:
            var="shopname"
        if value==7:
            var="topSeller"
        for j in range(1, len(arr)):
            key = arr[j]  # vAlue to be added inn the Sorted PArt
            i = j - 1
            while i >= 0 and getattr(arr[i],var) > getattr(key,var):
                arr[i + 1] = arr[i]
                i = i - 1
            # print(i+1)
            arr[i + 1] = key
class SelectionAlgorithm:

    def SelectionSort(self,arr,value):
        var=None
        if value==1:
            var="name"
        if value==2:
            var="price"
        if value==3:
            var="solditems"
        if value==4:
            var="ratings"
        if value==5:
            var="taxes"
        if value==6:
            var="shopname"
        if value==7:
            var="topSeller"

        n = len(arr)

        for i in range(0, n - 1):
            min = i
            for j in range(i + 1, n):

                if getattr(arr[j],var) < getattr(arr[min],var):
                    min = j

            if min != i:
                arr[min], arr[i] = arr[i], arr[min]

class BubbleAlgorithm:

    def BubbleSort(self,arr,value):
        var=None
        if value==1:
            var="name"
        if value==2:
            var="price"
        if value==3:
            var="solditems"
        if value==4:
            var="ratings"
        if value==5:
            var="taxes"
        if value==6:
            var="shopname"
        if value==7:
            var="topSeller"


        size = len(arr)

        for i in range(0, size - 1):
            swapped = False

            for j in range(0, size - 1):
                if getattr(arr[j],var) > getattr(arr[j + 1],var):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if (not swapped):
                break
class MergeAlgorithm:
    def MergeSort(self,arr,value):


        l=0
        r=len(classObjects)

        self.mergeSort(classObjects,l,r-1,value)

    def mergeSort(self,arr,l,r,value):
        if r > l:
            m = l + (r - l) // 2
            self.mergeSort(arr, l, m,value)
            self.mergeSort(arr, m + 1, r,value)
            self.mergeString(arr, l, m, r,value)

    def mergeString(self,arr, l, m, r,value):

        helper = []
        for i in range(l, r + 1):
            helper.append(arr[i])

        i = 0
        j = m + 1 - l
        k = l
        if value == 1:
            var = "name"
        if value == 2:
            var = "price"
        if value == 3:
            var = "solditems"
        if value == 4:
            var = "ratings"
        if value == 5:
            var = "taxes"
        if value == 6:
            var = "shopname"
        if value == 7:
            var = "topSeller"
        while i <= m - l and j <= r - l:
            if getattr(helper[i],var) <= getattr(helper[j],var):
                arr[k] = helper[i]
                i += 1
            else:
                arr[k] = helper[j]
                j += 1

            k += 1
        while i <= m - l:
            arr[k] = helper[i]
            i += 1
            k += 1
        while j <= r - l:
            arr[k] = helper[j]
            j += 1
            k += 1

class QuickAlgorithm:
    def QuickSort(self,arr,value):


        l=0
        r=len(classObjects)

        self.quickSortString(classObjects,l,r-1,value)

    def quickSortString(self, Arr, low, high,value):
        if low < high:
            pi = self.partitionString(Arr, low, high,value)
            self.quickSortString(Arr, low, pi - 1,value)
            self.quickSortString(Arr, pi + 1, high,value)

    def partitionString(self, Arr, low, high,value):

        pivot = Arr[high]

        i = low - 1


        if value == 1:
             var = "name"
        if value == 2:
            var = "price"
        if value == 3:
            var = "solditems"
        if value == 4:
            var = "ratings"
        if value == 5:
            var = "taxes"
        if value == 6:
            var = "shopname"
        if value == 7:
            var = "topSeller"
        #var="name"
        for j in range(low, high):
            if getattr(Arr[j], var) < getattr(pivot, var):
                i += 1
                Arr[i], Arr[j] = Arr[j], Arr[i]
        Arr[i + 1], Arr[high] = Arr[high], Arr[i + 1]
        return i + 1

# main
try:
    sc = Sorting(1)
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(850)
    widget.setFixedWidth(1120)
    widget.show()
except Exception as e:
    print(str(e))





try:
    sys.exit(app.exec_())
except:
    print("Exiting")