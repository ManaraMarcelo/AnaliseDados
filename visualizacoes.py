import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')

print(iris['species'].value_counts())
print(iris.head())
print(iris.describe())

col = 'sepal_length'
print(sns.histplot(data=iris, x= 'sepal_length').set_title(f'Distribuição da Variável {col}'))