import scrapy
import numpy as np
import json
import os


cd = os.getcwd()
file = json.load(open(cd+'\\urls.json','r',encoding='utf-8'))
url_dict = file[0]




trendyol = 'https://www.trendyol.com'

class TrendyolUrlSpider(scrapy.Spider):
    name = 'ty-url'
    allowed_domains = ['trendyol.com']
    start_urls = [url + "{}".format(str(i)) for url in list(url_dict.values()) for i in np.arange(0,10000,16)]

    def parse(self, response):
        data = response.json()
        for product in data['result']['products']:
            try:
                name=product['name']
                brand=product['brand']['name']
                price=product["price"]["sellingPrice"]
                url=trendyol+product["url"]
            except:
                name=None
                brand=None
                price=None
                url=None

            try:
                product_category=product["categoryName"]
                product_category_hierarchy=product["categoryHierarchy"]
            except:
                product_category=None
                product_category_hierarchy=None

            try:
                bussinesUnit=product["businessUnit"]
                Attributes=product["variants"][0]["attributeValue"]
            except:
                bussinesUnit=None
                Attributes=None

            try:
                AverageRatingScore=product["ratingScore"]["averageRating"]
                TotalRating=product["ratingScore"]["totalCount"]
            except:
                AverageRatingScore=None
                TotalRating=None

            

            yield {
                    "name":name,
                    "brand":brand,
                    "price":price,
                    "url":url,
                    "product_category":product_category,
                    "product_category_hierarchy":product_category_hierarchy,
                    "bussinesUnit":bussinesUnit,
                    "AverageRatingScore":AverageRatingScore,
                    "TotalRating":TotalRating,
                    "Attributes":Attributes
                }


