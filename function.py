
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Ricardo Cisterna
from bs4 import BeautifulSoup
import requests
import re
from clases import *

#funciones
#entrada: link a la pagina
#salida: lista de objeto Category        
def getCategory(html):
    soup = BeautifulSoup(html, 'html.parser')
    categ=[]
    for sibling in soup.html.body.aside.ul.li.ul.find_all('a'):
        name = sibling.text.strip()
        link = "http://books.toscrape.com/"#buscar mejor forma 
        link=link + sibling['href'].replace('..','')
        categ.append(Category(name,link))
    return categ




#entrada: link a categoria
#salida: lista con link a los detalles de los libros
def getBookLinkDetail(category):
    r = requests.get(category.link)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    details=[]
    for sibling in soup.html.body.find_all('article'): #find_all("div", {"class": "col-sm-8 col-md-9"}).article:  # .h3.find_all('a', href=True):
        #name = sibling .h3.find_all('a', href=True).text.strip()
        link = "http://books.toscrape.com/catalogue/"#buscar mejor forma 
        link=link + sibling.h3.a['href'].replace('../','')
        details.append(link)
    return details

#entrada: link al detalle del libro y categoria del libro
#salida: objeto tipo libro, datos necesarios para el 
def getBookDetail(link,category):
    r = requests.get(link)
    html = r.text
    
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.html.body.article#.find_all('div',class_="row")
    link = "http://books.toscrape.com/"#buscar mejor forma
    cover=link + main.div.img['src'].replace('../','')#4
    productMain = main.find_all('div',{"class": "product_main"})
    title =productMain[0].h1.text.replace(",",".") 
    aux = productMain[0].find_all('p')
    price = aux[0].text.replace('Â','')
    stock = re.sub("\D", "", aux[1].text.strip())
    table = main.table.find_all('td')
    upc=table[0].text
    productType=table[1].text
    priceWtax =table[2].text.replace('Â','')
    priceWOtax =table[3].text.replace('Â','')
    tax =table[4].text.replace('Â','')
    avalilability =re.sub("\D", "", table[5].text.strip())
    numberOfReviews =table[6].text
    book=Book(title,price,stock,category,cover,upc,productType,priceWtax,priceWOtax,tax,avalilability,numberOfReviews)
    return book
