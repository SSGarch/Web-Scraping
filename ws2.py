from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"J:\chromedriver_win32\chromedriver.exe")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content)

for data in soup.findAll('data',href=True, attrs={'class':'_2kHMtA'}):

    name=data.find('div', attrs={'class':'_4rR01T'})   
    price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=data.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

    

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')