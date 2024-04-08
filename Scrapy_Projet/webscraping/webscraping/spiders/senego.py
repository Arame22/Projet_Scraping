import scrapy
from scrapy import Spider

import pymongo

from pymongo import MongoClient
from scrapy.crawler import CrawlerProcess
from ..items import webscrapingItem 

class SenegoSpider(Spider):
    name = "senego"
    allowed_domains = ["senego.com"]
    start_urls = ["https://www.senego.com/"]

    def parse(self, response):
            items = webscrapingItem()
            links = response.css("article.populars-home-post a::attr(href)").extract()
            items["links"] = links
            for link in links:
                print(link)
                yield scrapy.Request(link, callback=self.parse_items)


    def parse_items(self, response):
            items = webscrapingItem()

            Categorie = response.css("span.sectionTitle h1::text").extract()
            Titre = response.css("div.populars-home-postInfos h2::text").extract()
            Contenu = response.css("div.article-detail-content p::text").extract()
            Commentaire = response.css("span.sectionTitle ::text").extract()
    
            
            items["Titre"] = Titre
            items["Contenu"] = Contenu
            items["Commentaire"] = Commentaire

            yield items