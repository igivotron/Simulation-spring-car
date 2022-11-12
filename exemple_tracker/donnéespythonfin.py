# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 08:48:51 2022

@author: Tom
"""

import matplotlib.pyplot as plt
import numpy as np

### données d'exemple
sample_t = np.arange(0., 3., 0.1)
array1 = sample_t

sample_x = 4 * (1 - np.exp(-sample_t))
sample_v = 3 * np.exp(-sample_t)


"""
    Rassembler les données [t0, t1, ...], [x0, x1, ...], [v0, v1, ...]
    en un seul tableau transposé [[t0, x0, v0], [t1, x1, v1], ...]
"""
sample_data = np.array((sample_t, sample_x, sample_v)).T

np.savetxt('sample_data.txt', sample_data , fmt = '%i') 

"""
J'ai les données dans le format
1 2 3 
4 5 6 
7 8 9
"""


"""
    Écrire les données dans un fichier texte "sample.data".
    Le fichier contient une ligne par ligne du tableau,
    chaque ligne contient les valeurs séparées par des espaces:
        t0 x0 v0
        t1 x1 v1
        ...
"""
np.savetxt("sample.data", sample_data)

"""
    Relire les données à partir du fichier texte "sample.data".
    Produit un tableau [[t0, x0, v0], [t1, x1, v1], ...]
"""
read_data = np.loadtxt("sample.data")

"""d
    Décomposer le tableau en ses différentes colonnes
"""
(t, x, v) = read_data.T

array_temps = t; array_pos = x; array_vit = v;



"""
    Lire un fichier "mesure.data" exporté par Tracker.
    Le fichier a le même format que ci-avant.
    Pour obtenir ce fichier à partir de Tracker :
    *  Utiliser le point (period) et non la virgule pour les décimales:
        'Edition > Numbers > Formats > Decimal separator > period'
    *  Exporter les données souhaitées : 'Fichier > Exporter >
        Fichier de données', sélectionner les variables puis 'Enregistrer sous'.
    *  Editer le fichier pour éliminer les lignes initiales et finales
        incomplètes (données manquantes) ou hors format (titres)
"""
(mesure_t, mesure_x, mesure_v) = np.loadtxt("mesure.data").T
read_data2 = np.loadtxt("mesure.data")
np.savetxt('mesure_data.txt', read_data2 , fmt = '%i') 




"""
    Afficher plusieurs données sur un même graphique pour comparaison
"""
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t, x, label="x sample")
plt.plot(mesure_t, mesure_x, label="x mesure")
plt.legend()
plt.subplot(2,1,2)
plt.plot(t, v, label="v sample")
plt.plot(mesure_t, mesure_v, label="v mesure")
plt.legend()
plt.show()

"""
    Ecrire et relire les données dans un fichier "sample.csv"
    en format CSV séparé par des virgules.
    De nombreuses autres variations sont possibles, voir:
    >>> help(np.savetxt)
    >>> help(np.loadtxt)
"""
np.savetxt("sample.csv", sample_data, delimiter=",")
np.savetxt("mesure.csv", mesure_v, delimiter=",")    

csv_data = np.loadtxt("sample.csv", delimiter=",")





"""
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------


"""
