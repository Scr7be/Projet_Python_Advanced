from configMongo import collection
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#! Enlève l'avertissement sur Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

#! Récupération des données de ProjectPythonAdvanced
records = collection.find({}, {'_id': 0})

# ! Conversion des données de la BDD en dataFrame
df_BDD_F1 = pd.DataFrame(list(records))
df_BDD_F1 = df_BDD_F1.drop_duplicates()
st.title("🟢Tableau du contenu de InfoF1")
st.table(df_BDD_F1)


#!affiche le diagram des points totaux des pilotes
st.title("🔵Graphe des points totaux des pilotes sur la saison 2020")
plt.bar(df_BDD_F1['Pilotes'], df_BDD_F1['Pts'])
plt.xticks(rotation=90)
plt.xlabel('Pilotes')
plt.ylabel('Points')
plt.title('Classement des pilotes')
st.pyplot()

#TODO: Mise en place des filtres
#! Créer les filtres
st.title("🔴 Mise en place des filtres sur le DataFrame")
pil_filter = st.sidebar.selectbox('Nom Pilote', ['L. HAMILTON', 'V. BOTTAS', 'M. VERSTAPPEN', 'S. PEREZ', 'D. RICCIARDO', 'C. SAINZ', 'A. ALBON', 'C. LECLERC', 'L. NORRIS', 'P. GASLY', 'L. STROLL', 'E. OCON', 'S. VETTEL', 'D. KVYAT', 'N. HULKENBERG', 'K. RAIKKONEN', 'A. GIOVINAZZI', 'G. RUSSELL', 'R. GROSJEAN', 'K. MAGNUSSEN'])
#! Appliquer les filtres
filtered_data = df_BDD_F1[(df_BDD_F1['Pilotes'] == pil_filter)]
#! Afficher le résultat
filtered_data

#TODO: Diagram Circulaire
#!Filtre pour choisir le nombre de pilote à afficher sur le diagram
nombrePil_filtre = st.sidebar.selectbox('Nombre de pilotes que vous souhaitez afficher', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
df_top5 = df_BDD_F1.head(nombrePil_filtre)

#! Création du diagram circulaire
plt.figure(figsize=(8,6))
plt.pie(df_top5['Pts'], labels=df_top5['Pilotes'], autopct='%1.1f%%', startangle=90, counterclock=False)
st.title('🟠Classement des pilotes - Saison 2020')

#! Afficher le diagramme circulaire sur Streamlit
st.pyplot()


