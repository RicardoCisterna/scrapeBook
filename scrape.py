#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Ricardo Cisterna

#Scrape BOOKS Thech-K

from bs4 import BeautifulSoup
import requests
import re
import csv
from clases import *
from function import *



    



f = open('bookstoscrape.csv', 'w',encoding="utf-8")
#no alcanzo a ocupar CSV :D 
f.write('Title,Price,Stock,Category,Cover,UPC,Product Type,Price (excl. tax),Price (incl. tax),Tax,Availability,Number of reviews\n')

r = requests.get('http://books.toscrape.com')
html = r.text
print("ini")  
categorys = getCategory(html)
for category in categorys:
    details = getBookLinkDetail(category)
   
    for detail in details:
        book = getBookDetail(detail,category.name)
        try:
            f.write(book.title+','+book.price+','+book.stock+','+book.category+','+book.cover+','+book.upc+','+book.productType+','
                +book.priceWOtax+','+book.priceWtax+','+book.tax+','+book.avalilability+','+book.numberOfReviews+'\n')
            print(book.title)
        except:
          print(book.title+book.category+"An exception occurred")
    break    
    
print("temino")
f.close()

