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
    def __init__(self, name, link):
        self.category = name
        self.link = link
#funciones
#retorna lista de objeto Category        
def getCategory(html):
    soup = BeautifulSoup(html, 'html.parser')
    categ=[]
    for sibling in soup.html.body.aside.ul.li.ul.find_all('a'):
        name = sibling.text.strip()
        link = "http://books.toscrape.com/catalogue/category/books"#buscar mejor forma 
        link=link + sibling['href'].replace('..','')
        categ.append(Category(name,link))
    return categ


def getBook(html,category):
    return 0

r = requests.get('http://books.toscrape.com')
html = r.text
   
aux = getCategory(html)
for i in aux:
    print (i.category)
    print (i.link)






#print(soup.html.body.aside.ul.li.ul.li.a)


#print(soup.html.body.section.article)

#print (r.text[:100])
