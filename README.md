# Projet_Python_Advanced, Scrapping du site statsF1 afin de récupérer le tableau des classements de 2020

Le projet consciste à scrapper le site web statsf1 afin de récupérer les données du classement de la saison 2020 et de les stocker dans une base de donnée Mongo.
Les données stockés seront utilisé par la suite afin de faire des diagrams et des dataframes qui seront affichés à l'aide de Streamlit.

#### NB : les #! et les #TODO permette de changer la couleur de mes commentaires, pour une meilleure lisibilité, je vous invite à installer l'extension BetterComments sur Visual Studio Code

## Composition du code :
- scrapper.py : Fichier contenant le code afin d'effectuer le scrapping sur le site statsf1.
- main.py : Fichier qui contient tout les diagrams et tout les tableaux qui seront affiché grâce à la bibliothèque Streamlit.
- configMongo.py : Ce fichier contient tout ce qui va permettre de se connecter à la base de donnée et il contient aussi le code qui implémente les données dans la BDD.
- test.py : Le fichier test contient des tests unitaires sur le fichier configMongo.py et sur le fichier scrapper.py

## Exécution du code : 
Afin de récupérer le projet python, commencez par créez un dossier qui accueillera le projet.

Suite à cela, dans le terminal de ce même dossier, entrez la commande :
```
git clone https://github.com/Scr7be/Projet_Python_Advanced
```
Pour accéder au projet faite un :
```
cd Projet_Python_Advanced
```
N'oubliez pas d'installer les bibliothèque, voici les install à faire: 
```
pip install streamlit beautifulsoup4 pandas seaborn matplotlib pymongo requests unittest numpy
```
Pour exécuter le code afin d'afficher la fenêtre Streamlit faite : 
```
streamlit run main.py
```

## Attention : Si le test sur Mongo ne passe pas, entrez la commande suivante dans mongosh :
```
db.dropDatabase()
```
Ce problème est dû au faite que le test regénère des données fictives, or la base de donnée est déjà remplie. Cette commande va donc effacer la base de donnée afin de laisser le champ libre pour les tests.

## Bon courage 😁!
