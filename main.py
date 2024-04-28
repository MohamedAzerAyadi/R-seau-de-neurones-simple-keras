#Import des modules keras et numpy
from keras import *
import numpy as np
#Création d'un modèle de réseau de neurones vide
model = Sequential()

#Ajout de 3 couches au modèle
model.add(layers.Dense(units=3,input_shape=[1])) #entrée unidimentionnelle (couche à 3 unités)
model.add(layers.Dense(units=32)) #couche de 32 unités
model.add(layers.Dense(units=1)) #couche d'une unité pour prédire une seule valeur à la sortie

#entrée + sortie
entree = np.array([1,2,3,4,5])
sortie = np.array([2,4,6,8,10])

#compialtion du modèle
model.compile(loss='mean_squared_error', optimizer='adam')
#entrainement du modèle sur les données entree et sortie en 1000 itérations
model.fit(x=entree, y=sortie, epochs=1000)
#prédiction avec le modèle entrainé
while True:
    x=int(input('nombre :'))
    print('Prédiction :' + str(model.predict(np.array([x]))))
