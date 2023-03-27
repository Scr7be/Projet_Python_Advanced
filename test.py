import unittest
from pymongo import MongoClient
from Scrapper import piloteF1Desc
from bs4 import BeautifulSoup
import requests
import pandas as pd

class TestMongo(unittest.TestCase):

    def setUp(self):
        self.url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0"
        self.client = MongoClient(self.url)
        self.db = self.client['Projet_Python_Advanced']
        self.collection = self.db['InfoF1_2022']
        self.infoF1 = piloteF1Desc.to_dict('records')
    
    #! Test ajout des informations dans la bdd
    def test_ajout(self):
        self.collection.insert_many(self.infoF1)
        count = self.collection.count_documents({})
        self.assertEqual(count, len(self.infoF1))
        #faut que tu vides ta db avant de faire les tests

class TestScraping(unittest.TestCase):

    def test_scraping(self):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
        headers = {'User-Agent': user_agent}
        url="https://www.statsf1.com/fr/2020.aspx"
        page_content = requests.get(url,headers=headers).content
        soup = BeautifulSoup(page_content, 'lxml')

        #! Permet de scrapper la partie formulaire du site
        listeResultF1 = [[x.text for x in soup.find("table", {"id": "ctl00_CPH_Main_TBL_CHP_P"}).findAll('tr')[i].findAll('td')] for i in range(22)]

        #! Création du dataframe de pilotes
        piloteF1Desc=pd.DataFrame(listeResultF1[1:], columns=["-"]+listeResultF1[0])

        #! Vérification que le dataframe contient bien les colonnes attendues
        self.assertListEqual(list(piloteF1Desc.columns), ['-', 'Pilotes', '1AUT', '2STY', '3HUN', '4GBR', '570', '6ESP', '7BEL', '8ITA', '9TOS', '10RUS', '11EIF', '12PRT', '13ERO', '14TUR', '15BHR', '16SAK', '17ABD', 'Pts'])

        #! Vérification que le dataframe contient bien des données
        self.assertGreater(len(piloteF1Desc), 0)

        #ce que tu insères est pas bon par rapport à ce qu'il ressort


if __name__ == '__main__':
    unittest.main()