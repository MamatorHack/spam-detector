# Convertir les labels en 0 (ham) et 1 (spam)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Afficher les 5 premières lignes
df.head()

from sklearn.feature_extraction.text import CountVectorizer

# Convertir les messages en nombres
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])

# Labels (0 ou 1)
y = df['label']

# Afficher la taille des données
X.shape, y.shape