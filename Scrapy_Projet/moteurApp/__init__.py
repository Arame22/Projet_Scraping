import pymongo
from flask import Flask
from .view import app  # Importez app depuis le module view

app = Flask(__name__)

# mongodb database
mongodb_client = pymongo(app)
db = mongodb_client.db

from moteurApp import view
