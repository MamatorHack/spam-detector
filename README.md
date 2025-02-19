# 📩 Détection de Spam avec un Modèle IA

Ce projet permet de classifier un message en **spam** ou **non-spam** grâce à un modèle entraîné en **Python** avec `scikit-learn`.  

## 📂 Organisation du projet  
- **SMSSpamCollection** : Dataset des messages utilisés pour entraîner le modèle.  
- **import.py** : Chargement et préparation des données.  
- **converter.py** : Transformation des données textuelles en données exploitables par le modèle.  
- **trainer.py** : Entraînement du modèle de classification.  
- **test.py** : Test du modèle sur de nouveaux messages.  

## 🚀 Installation et Exécution  

### 1️⃣ Prérequis  
Assurez-vous d'avoir **Python 3.x** installé ainsi que les bibliothèques nécessaires :  
*pip install pandas scikit-learn*

### 2️⃣ Exécuter l'entraînement
Lancez le script d'entraînement du modèle :
*python trainer.py* 

### 3️⃣ Tester un message
Après l'entraînement, allez écrire le message que vous voulez dans le fichier *test.py* et executez :
*python test.py*

Vous verrez s'il est détecté comme spam ou non.

## 📜 Licence
Ce projet est sous licence MIT – vous pouvez l'utiliser librement. Voir le fichier **LICENSE** pour plus d’informations.
