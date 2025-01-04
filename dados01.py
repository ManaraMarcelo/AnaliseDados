import pandas as pd
import numpy as np

cuisine_rating = pd.read_csv('Cuisine_rating.csv') # Open the archive inside the code folder

print(cuisine_rating.head()) # Show the firsts lines
print(cuisine_rating.info()) # Show the Dtype and more of the database
print(cuisine_rating['Cuisines'].value_counts()) # Show the quantidy of all values of the 'Cuisines' column
print(cuisine_rating.describe()) # Show a simple resume about all the data 

'''
Let's make a question: If i should open a Restaurant in Central Park NY what kind of food should I make? 
'''

print(cuisine_rating['Location'].value_counts()) # Looking for all the places there
numeric_cols = cuisine_rating.select_dtypes(include=np.number).columns.to_list() # Crio uma variavel para armazenar apenas o que é considerado numero
# pelo numpy e pego as colunas, transformando em uma lista.
print(cuisine_rating[numeric_cols])
print(cuisine_rating.groupby(['Location'])[numeric_cols].mean()) # Me baseio na coluna Location, pego os numeros e faço uma média geral
print(cuisine_rating.groupby(['Location', 'Cuisines'])[numeric_cols].mean()) # Now I used Location and Cuisines as a filter to make the table
