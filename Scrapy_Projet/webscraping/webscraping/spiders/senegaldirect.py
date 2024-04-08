import scrapy
from scrapy import Spider

import pymongo

from pymongo import MongoClient
from scrapy.crawler import CrawlerProcess
from ..items import webscrapingItem 

class senegaldirectSpider(Spider):
    name = "senegaldirect"
    allowed_domains = ["senegaldirect.com"]
    start_urls = ["https://www.senegaldirect.com/"]

# Configure MongoDB connection
#client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change connection URL if needed
#database = client["news_database"]  # Change database name if needed
#collection = database["articles"]  # Change collection name if needed


    def parse(self, response):
            items = webscrapingItem()
            links = response.css("h2.title  a::attr(href)").extract()
            items["links"] = links
            for link in links:
                print(link)
                yield scrapy.Request(link, callback=self.parse_items)


    def parse_items(self, response):
            items = webscrapingItem()

            Categorie = response.css("span.term-badge ::text").extract()
            Titre = response.css("div.item-inner ::text").extract()
            Contenu = response.css("div.entry-content p::text").extract()
            

          

            items["Categorie"] = Categorie
            items["Titre"] = Titre
            items["Contenu"] = Contenu
            

            yield items