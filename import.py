import pandas as pd  # Manipulation de données
import numpy as np  # Calculs mathématiques
import matplotlib.pyplot as plt  # Affichage de graphiques
from sklearn.feature_extraction.text import CountVectorizer  # Transformer le texte en nombres
from sklearn.model_selection import train_test_split  # Séparer les données
from sklearn.naive_bayes import MultinomialNB  # Modèle d'apprentissage
from sklearn.metrics import accuracy_score  # Vérifier la performance du modèle

# Importer les bibliothèques nécessaires
import pandas as pd

# Charger le fichier depuis Google Colab
df = pd.read_csv('/SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])

# Afficher les 5 premières lignes du dataset
df.head()