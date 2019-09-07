#Ricardo Cisterna

#Scrape BOOKS Thech-K

#1 tomar lista de catgorias
    #aside
    #a href, text
#2 por categoria tomar cada articulo
#3 por articulo tomar detalle

from bs4 import BeautifulSoup
import requests
import re


#clases
class Category:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        

class Book:
    def __init__(self, title, price,stock,category,cover,upc,productType,priceWtax,priceWOtax,tax,
                 avalilability,numberOfReviews):
        self.title = title
        self.price = price
        self.stock = stock
        self.category = category
        self.cover = cover
        self.upc =upc
        self.productType =productType
        self.priceWtax =priceWtax
        self.priceWOtax =priceWOtax
        self.tax =tax
        self.avalilability =avalilability
        self.numberOfReviews =numberOfReviews

    

#funciones
#retorna lista de objeto Category        
def getCategory(html):
    soup = BeautifulSoup(html, 'html.parser')
    categ=[]
    for sibling in soup.html.body.aside.ul.li.ul.find_all('a'):
        name = sibling.text.strip()
        link = "http://books.toscrape.com/"#buscar mejor forma 
        link=link + sibling['href'].replace('..','')
        categ.append(Category(name,link))
    return categ





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

def getBookDetail(link,category):
    r = requests.get(link)
    html = r.text
    
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.html.body.article#.find_all('div',class_="row")
    link = "http://books.toscrape.com/"#buscar mejor forma
    cover=link + main.div.img['src'].replace('../','')#4
    productMain = main.find_all('div',{"class": "product_main"})
    title = productMain[0].h1.text
    aux = productMain[0].find_all('p')
    price = aux[0].text.replace('Â','')
    stock = re.sub("\D", "", aux[1].text.strip())
    table = main.table.find_all('td')
    upc=table[0].text
    productType=table[1].text
    priceWtax =table[2].text.replace('Â','')
    priceWOtax =table[3].text.replace('Â','')
    tax =table[4].text.replace('Â','')
    avalilability =table[5].text
    numberOfReviews =table[6].text
    book=Book(title,price,stock,category,cover,upc,productType,priceWtax,priceWOtax,tax,avalilability,numberOfReviews)
    return book




a=Category('Treavel','http://books.toscrape.com/catalogue/category/books/travel_2/index.html')




r = requests.get('http://books.toscrape.com')
html = r.text
   
categorys = getCategory(html)
for category in categorys:
    details = getBookLinkDetail(category)
   
    for detail in details:
        
        book = getBookDetail(detail,category.name)
        break
    break
    






#print(soup.html.body.aside.ul.li.ul.li.a)


#print(soup.html.body.section.article)

#print (r.text[:100])
