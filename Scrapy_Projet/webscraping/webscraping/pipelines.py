# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from pymongo import MongoClient
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import re  
import string
import math


#class WebscrapingPipeline:
    #def __init__(self):         
        #self.conn = pymongo.MongoClient("localhost",27017)
        #db = self.conn["Sp_projet"]
        #self.collection = db["rewmi"]
        #self.collection = db["sengal7"]
        #self.collection = db["senegaldirect"]
        #self.collection = db["dakarbuzz"]
        #self.collection = db["senego"]
        #self.collection = db["senenews"]


    #def process_item(self, item, spider):
        #self.collection.insert_one(dict(item))
        #return item
    

import pymongo
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import re  
import string
import math

class MongoDBPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)

    def open_spider(self, spider):
        self.db = self.conn['Sp_projet']
        self.collection = self.db[f"{spider.name}_items"]

    def process_item(self, items, spider):
        text = self.clean_text(items['Contenu'])
        tokens = self.tokenize(text)
        tf = self.compute_tf(tokens)

        self.collection.insert_one({
            'Titre': items['Titre'],
            'Contenu': items['Contenu'],
            'tf': tf,
            'tfidf': {}
            })

        return items



    def compute_tf_idf(self, documents):
        documents = self.collection.find({})
        documents = [self.compute_tf(self.tokenize(doc['Contenu'])) for doc in documents]
        documents = [" ".join(doc.keys()) for doc in documents]
        idfs = self.compute_idf(documents)

        # Calcul TF-IDF et mise à jour MongoDB
        for doc in documents:
            tfidf = {}
            for word, tf_value in doc['tf'].items():
                tfidf[word] = tf_value * idfs[word]

            self.collection.update_one({'_id': doc['_id']}, {'$set': {'tfidf': tfidf}})
    def clean_text(self, text):
        if text is None:
            return None
        elif not isinstance(text, str):
            text = str(text)
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    def tokenize(self, text):
        tokens = nltk.word_tokenize(text)
        stemmer = SnowballStemmer('french')
        tokens = [stemmer.stem(t) for t in tokens]
        stop_words = set(stopwords.words('french'))
        tokens = [t for t in tokens if t not in stop_words]
        return tokens


    def compute_tf(self, tokens):
        return {w: tokens.count(w) / len(tokens) for w in tokens}

    def compute_idf(self, documents):
        idf = {}
        for doc in documents:
            for word in set(doc['tf']):
                idf[word] = idf.get(word, 0) + 1

        num_docs = len(documents)
        for word in idf:
            idf[word] = math.log(num_docs / idf[word])

        return idf

    def compute_tfidf(self, tf, idfs, documents):
        tfidf = {}
        for doc in documents:
            tfidf[doc['_id']] = {}
            for word, tf_value in doc['tf'].items():
                tfidf[doc['_id']][word] = tf_value * idfs[word]

        return tfidf


    







