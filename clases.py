#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Ricardo Cisterna

#clases






#link y nombre categoria
class Category:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        
#datos a exportar
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


