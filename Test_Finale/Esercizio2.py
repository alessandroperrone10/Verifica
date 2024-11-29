from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Caricamento del dataset
data = load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette


#visualizzo caratteristiche e etichette
df = pd.DataFrame(X, columns=data.feature_names)
print("Visualizzazione dei primi cinque dati del dataset")
print(df.head())

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Creazione del modello di classificazione
modello = DecisionTreeClassifier()


# Addestramento del modello
modello.fit(X_train, y_train)


# Predizione delle etichette per il set di test
predictions = modello.predict(X_test)

#Valuta la performance del modello utilizzando il classification_report (precisione, recall, F1-score)
classificazione = classification_report(y_test, predictions, target_names=data.target_names)
print("Classificazione del modello: \n", classificazione)


#Visualizzazione della matrice di confusione
matrice_confusione = confusion_matrix(y_test, predictions)

#Heatmap per la matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(matrice_confusione, annot=True, fmt='d', cmap='Blues',
            xticklabels=data.target_names,
            yticklabels=data.target_names)

plt.show()

