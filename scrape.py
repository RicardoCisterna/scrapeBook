#Ricardo Cisterna

#Scrape BOOKS Thech-K

#1 tomar lista de catgorias
    #aside
    #a href, text
#2 por categoria tomar cada articulo
#3 por articulo tomar detalle

from bs4 import BeautifulSoup
import requests


r = requests.get('http://books.toscrape.com/catalogue/category/books/politics_48/index.html')
html = r.text


soup = BeautifulSoup(html, 'html.parser')
soup.tittle
#aside = BeautifulSoup(soup.html.body.aside.ul.li.ul.li.a, 'html.parser')

for sibling in soup.html.body.aside.ul.li.ul.find_all('a'):
    #print(repr(sibling))
    print( sibling['href'])
    print (sibling.text.strip())
    link = "http://books.toscrape.com/catalogue/category/books"#buscar mejor forma 
    print (link + sibling['href'].replace('..',''))

#print(soup.html.body.aside.ul.li.ul.li.a)


#print(soup.html.body.section.article)

#print (r.text[:100])
