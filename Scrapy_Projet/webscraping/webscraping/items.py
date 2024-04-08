import scrapy


class webscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    Categorie = scrapy.Field()
    Titre = scrapy.Field()
    Contenu = scrapy.Field()
    Commentaire = scrapy.Field()
    links = scrapy.Field()
    pass
