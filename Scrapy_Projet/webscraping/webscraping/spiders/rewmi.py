import scrapy
from scrapy import Spider

import pymongo

from pymongo import MongoClient
from scrapy.crawler import CrawlerProcess
from ..items import webscrapingItem 

class rewmiSpider(Spider):
    name = "rewmi"
    allowed_domains = ["rewmi"]
    start_urls = ["https://www.rewmi.com/"]

# Configure MongoDB connection
#client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change connection URL if needed
#database = client["news_database"]  # Change database name if needed
#collection = database["articles"]  # Change collection name if needed


    def parse(self, response):
            items = webscrapingItem()
            links = response.css("h2.post-box-title a::attr(href)").extract()
            items["links"] = links
            for link in links:
                print(link)
                yield scrapy.Request(link, callback=self.parse_items)


    def parse_items(self, response):
            items = webscrapingItem()

            Categorie = response.css("div.cat h2::text").extract() 
            Titre = response.css("div.masonry-grid  a::text").extract()
            Contenu = response.css("div.entry ::text").extract()
            Commentaire = response.css("h3.comment-reply-tile ::text").extract()

            items["Categorie"] = Categorie
            items["Titre"] = Titre
            items["Contenu"] = Contenu
            items["Commentaire"] = Commentaire

            yield items
