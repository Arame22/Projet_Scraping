import scrapy
from scrapy import Spider

import pymongo

from pymongo import MongoClient
from scrapy.crawler import CrawlerProcess
from ..items import webscrapingItem 

class Senegal7Spider(Spider):
    name = "senegal7"
    allowed_domains = ["senegal7.com"]
    start_urls = ["https://senegal7.com"]

# Configure MongoDB connection
#client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change connection URL if needed
#database = client["news_database"]  # Change database name if needed
#collection = database["articles"]  # Change collection name if needed


    def parse(self, response):
            items = webscrapingItem()
            links = response.css("h2.title a::attr(href)").extract()
            items["links"] = links
            for link in links:
                print(link)
                yield scrapy.Request(link, callback=self.parse_items)


    def parse_items(self, response):
            items = webscrapingItem()

            Categorie = response.css("span.term-badges::text").extract()
            Titre = response.css("span.post-title::text").extract()
            Contenu = response.css("div.entry-content p::text").extract()
            Commentaire = response.css("span.title-counts::text").extract()

            items["Categorie"] = Categorie
            items["Titre"] = Titre
            items["Contenu"] = Contenu
            items["Commentaire"] = Commentaire

            yield items

#def parse(self, response):
    #for article in response.css("div.article"):
        #items =  Senegal7Item()
     #   #items["category"] = article.xpath("/html/head/link[10]/a/text()").extract_first()
       # items["title"] = article.css("h1 ::text").extract_first()
        #items["description"] = article.xpath("/html/head/meta[32]/@content").extract_first()
            
        
        #yield items
 
        # Insert the item into MongoDB
       # collection.insert_one(dict(items))
        
    

#def store_data_in_mongodb(data):
    #client = MongoClient('mongodb://localhost:27017/')
    #db = client['news_database']
    #collection = db['articles']
    
    #for article in data:
       # collection.insert_one(article)

#if __name__ == '_main_':
   # process = CrawlerProcess()
    #news_database = process.crawl(Senegal7Spider)
   # process.start()
    
   # store_data_in_mongodb(news_database)
     
        #yield {
           #  'url' : response.url,
           # 'title' : response.css("h1 ::text").get(),
            #'category' : response.xpath("/html/head/link[10]/a/text()").get(),
           # 'description' : response.xpath("/html/head/meta[32]::p/text()").get()
        #}  
    
        
        #yield {
#import scrapy
#from WebscrapingItem import NewsItem

#class Senegal7Spider(scrapy.Spider):
 #   name = "senegal7"
  #  allowed_domains = ["senegal7.com"]
   # start_urls = ["https://senegal7.com"]

    #def parse(self, response):
     #   for article in response.css("div.article"):
      #      item = NewsItem()
       #     item["title"] = article.css("h1 ::text").extract_first()
        #    item["category"] = article.xpath("/html/head/link[10]/a/text()").extract_first()
         #   item["description"] = article.xpath("/html/head/meta[32]/@content").extract_first()
            
          #  yield item



