# Outliers são dados muito altos ou muito baixos, que trazem uma curva defeituosa para nossas análises.
import pandas as pd
import numpy as np

houses = pd.read_csv('houses_to_rent.csv')
# print(houses.head)
print(houses.describe)
print(houses['bathroom'].value_counts)
'''
Vamos remover esses outliers eliminando o primeiro quartil e o quarto quartil do total de nossos dados
'''

q1 = houses['bathroom'].quantile(0.25) # Primeiro quartil
q3 = houses['bathroom'].quantile(0.75) # Terceiro quartil, pois vou usar o que vem acima dele

IQR = q3 - q1 # IQR -> Distância inter quartil

houses_outliers = houses[(houses['bathroom'] < q1 - (IQR * 1.5)) | (houses['bathroom'] > q3 + (IQR * 1.5))]
print(houses_outliers) # Assim eu mostro os meus outliers

houses_inliers = houses[(houses['bathroom'] >= q1 - (IQR * 1.5)) | (houses['bathroom'] <= q3 + (IQR * 1.5))]
print(houses_inliers.describe())