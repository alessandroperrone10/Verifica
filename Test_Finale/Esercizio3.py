#Crea un dataset autogenerandolo monolineare con 50 posizioni matematica e cambia la sua forma in 10 file da 5, 
# normalizza i valori e rendili interi , nessun valore deve essere uguale a un altro sulla stessa linea della collezione  
# dopodiché stampa un grafico che lo rappresenti. 


import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt

# Genero i dati monolineari
dataset = np.random.normal(0, 1, 50)


#Cambio la forma del dataset in 10 x 5
dataset = dataset.reshape(10, 5)






