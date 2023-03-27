from pymongo import MongoClient
from Scrapper import piloteF1Desc

#! Connexion à la base de données MongoDB
url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0"
client = MongoClient(url)
db = client['Projet_Python_Advanced']
collection = db['InfoF1_2022']

#! Implémentation dans la base de donnée du formulaire F1 2020
infoF1 = piloteF1Desc.to_dict('records')
result = collection.insert_many(infoF1)