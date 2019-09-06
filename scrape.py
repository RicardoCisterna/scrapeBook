#Ricardo Cisterna

#Scrape BOOKS Thech-K

#1 tomar lista de catgorias
    #aside
    #a href, text
#2 por categoria tomar cada articulo
#3 por articulo tomar detalle

from bs4 import BeautifulSoup
import requests


#clases
class Category:
    def __init__(self, name, link,image):
        self.name = name
        self.link = link
        

class Book:
    def __init__(self, name, link,category):
        self.name = name
        self.link = link
        self.category = category
        self.image =image
    

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
    print (category.link)
    for sibling in soup.html.body.find_all('article'): #find_all("div", {"class": "col-sm-8 col-md-9"}).article:  # .h3.find_all('a', href=True):
        print(sibling.h3.a['href'].replace('../',''))
        #name = sibling .h3.find_all('a', href=True).text.strip()
        link = "http://books.toscrape.com/catalogue/"#buscar mejor forma 
        link=link + sibling.h3.a['href'].replace('../','')
        details.append(link)
    return details

def getBookDetail(link,category):
    r = requests.get(category.link)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    details=[]
    print (category.link)
    for sibling in soup.html.body.find_all('article'): #find_all("div", {"class": "col-sm-8 col-md-9"}).article:  # .h3.find_all('a', href=True):
        print(sibling.h3.a['href'].replace('../',''))
        #name = sibling .h3.find_all('a', href=True).text.strip()
        link = "http://books.toscrape.com/catalogue/"#buscar mejor forma 
        link=link + sibling.h3.a['href'].replace('../','')
        details.appedn


    return 0




a=Category('Treavel','http://books.toscrape.com/catalogue/category/books/travel_2/index.html')

b = getBook(a)


r = requests.get('http://books.toscrape.com')
html = r.text
   
categorys = getCategory(html)
for category in categorys:
    details = getBookLinkDetail(category)
    for detail in details:
        book = (detail,category)
    
    






#print(soup.html.body.aside.ul.li.ul.li.a)


#print(soup.html.body.section.article)

#print (r.text[:100])
