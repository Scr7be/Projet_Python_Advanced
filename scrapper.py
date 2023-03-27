user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
headers = {'User-Agent': user_agent}
from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.statsf1.com/fr/2020.aspx"
page_content = requests.get(url,headers=headers).content
soup = BeautifulSoup(page_content, 'lxml')


#! Permet de scrapper la partie formulaire du site
listeResultF1 = [[x.text for x in soup.find("table", {"id": "ctl00_CPH_Main_TBL_CHP_P"}).findAll('tr')[i].findAll('td')] for i in range(22)]

#! Création du dataframe de pilotes
piloteF1Desc=pd.DataFrame(listeResultF1[1:], columns=["-"]+listeResultF1[0])

print(listeResultF1)


