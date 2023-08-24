import pandas as pd
df = pd.read_csv('Dados\MICRODADOS_ENEM_2022.csv', encoding = 'latin1', sep= ';', decimal = ',')
df.head()