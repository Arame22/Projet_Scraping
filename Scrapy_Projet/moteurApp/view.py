from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['Sp_projet']
db.sengal7.create_index([("Contenu", "text")])





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        
        # Effectuez la recherche dans MongoDB en utilisant un index texte
        results = db.sengal7.find({"$text": {"$search": query}})
        return render_template('result.html', results=results)

    


if __name__ == '__main__':
    app.run(debug=True)
