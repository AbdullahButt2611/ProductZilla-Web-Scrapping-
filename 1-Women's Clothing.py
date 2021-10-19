from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import tqdm
import pandas
from random import randint
from time import sleep

# Comsumer Electronics 37


class Data:
    def __init__(self,Name,Price,SoldItems,Rating,Tax,Store):
        self.Name = Name
        self.Price = Price
        self.Sold_Items = SoldItems
        self.Ratings = Rating
        self.Ship_Tax = Tax
        self.Store_Name = Store
        if Rating>=4.5:
            self.Top_Sell = True
        else:
            self.Top_Sell = False

    def __str__(self):
        s = "Name: "+self.Name+"\n"
        s += "Price: "+str(self.Price)+"\n"
        s += "SoldItems: "+str(self.Sold_Items)+"\n"
        s += "Ratings: "+str(self.Ratings)+"\n"
        s += "Tax: "+str(self.Ship_Tax)+"\n"
        s += "StoreName: "+self.Store_Name+"\n"
        s += "Top Seller: "+str(self.Top_Sell)+"\n"

        return s





options = Options()
options.headless = True
driverPath = 'C:\\Users\\DEll\\Desktop\\Waste\\Help\\chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path=driverPath)
url = 'https://www.aliexpress.com/premium/category/100003109.html?CatId=100003109'
driver.get(url)

# main = driver.find_element_by_class_name('next-pagination-pages')
# pages = main.find_elements_by_class_name('next-pagination-item')
# lastPage = pages[-1]
# lastPage = int(lastPage.text)
lastPage = 1


Namelist = []
Pricelist = []
SoldItemslist = []
Ratingslist = []
Taxlist = []
Storelist = []
TopSellList = []

currentPageNumber = 1
while(currentPageNumber <= lastPage):
    try:

        driver.maximize_window()
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)/4')
        sleep(2)
        driver.execute_script('window.scrollTo(((document.body.scrollHeight)/2)+(document.body.scrollHeight)/4),document.body.scrollHeight)')
        sleep(2)
        driver.execute_script('window.scrollTo(((document.body.scrollHeight)/2)+(document.body.scrollHeight)/4),document.body.scrollHeight)')
        sleep(1)
        print(currentPageNumber)


        pageSource = driver.page_source

        mainDiv = driver.find_element_by_class_name('JIIxO')
        # itemDetails = mainDiv.find_elements_by_class_name('_3L3yc')
        itemDetails = mainDiv.find_elements_by_class_name('_1OUGS')

        for itemDetail in itemDetails:
            Name, Price, SoldItems, Rating, Tax, Store= "",0.0,0,1.0,0.0,""

            try:
                Name = str(itemDetail.find_element_by_class_name('_18_85'))
                print(Name+"\n")
            except:
                print("In except")
                pass

            try:
                Price = str(itemDetail.find_element_by_class_name('mGXnE _37W_B'))
                Price = float("".join(Price.split(' ')[1].split(',')))
            except:
                pass

            try:
                SoldItems = str(itemDetail.find_element_by_class_name('_1kNf9'))
                SoldItems = int(SoldItems.split(' ')[0])
            except:
                pass

            try:
                Rating = float(itemDetail.find_element_by_class_name('eXPaM'))
            except:
                pass

            try:
                Tax = float(itemDetail.find_element_by_class_name('_2jcMA'))
            except:
                pass

            try:
                Store = str(itemDetail.find_element_by_class_name('ox0KZ'))
            except:
                pass

            if Rating >= 4.5:
                Top_Sell = True
            else:
                Top_Sell = False


            Namelist.append(Name)
            Pricelist.append(Price)
            SoldItemslist.append(SoldItems)
            Ratingslist.append(Rating)
            Taxlist.append(Tax)
            Storelist.append(Store)
            TopSellList.append(Top_Sell)

            # data = Data(Name,Price,SoldItems,Rating,Tax,Store)
            # ScrappedList.append(data.__str__())
    except:
        print("The Page is not found of index "+str(currentPageNumber)+"\n")
        pass

    currentPageNumber += 1

    url = 'https://www.aliexpress.com/premium/category/100003109.html?trafficChannel=ppc&catName=Women%27s+Clothing&CatId=100003109&ltype=premium&SortType=default&page='+str(currentPageNumber)+'&isrefine=y'
    driver.get(url)



# print((ScrappedList))
# print('----')
# EndData = pandas.DataFrame(ScrappedList)
EndData = pandas.DataFrame({"Name":Namelist,"Price":Pricelist,"Sold Items":SoldItemslist,"Ratings":Ratingslist,"Shipping Taxes":Taxlist,"Store Names":Storelist,"Top Sellers":TopSellList})
# print(EndData)
EndData.to_csv("Women's Section.csv",index=False)

driver.quit()