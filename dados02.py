import pandas as pd
import numpy as np

# -- Dados Constantes ----------------
houses_sp = pd.read_csv('houses_sp.csv')
print(houses_sp.head(10)) # o dado City é constante e desnecessário, custeanddo muito de nossa memória
houses_sp = houses_sp.drop(columns=['city'])
print(houses_sp.head())

# -- Dados Erroneos ou Nulos -----------------
''' São os NaN, atrapalham muito, devo sempre substitui-los por algum dados valido, isso analisando bem o roteiro'''

print(houses_sp.info()) # com isso eu vejo a quantidade de dados nulos e onde estão
# No caso de rooms eu vou substituir por uma mediana desse dado.
houses_sp['rooms'] = houses_sp['rooms'].fillna(houses_sp['rooms'].median()) # 'fillna' é para substituir dados
print(houses_sp.info()) # vejo que deu certo