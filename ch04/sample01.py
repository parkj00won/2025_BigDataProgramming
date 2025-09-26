from importlib.util import source_hash

import pandas as pd

covid_file_path = './data/owid-covid-data.csv'
#ver1
#covid_file_path = './data/data_bar.csv'
#df = pd.read_csv(covid_file_path, sep='|')
#print(df)

#ver2
# covid_file_path = './data/data_bar_euckr.csv'
# df = pd.read_csv(covid_file_path, sep='|', encoding='euc-kr') #읽기 가능
#print(df)

df = pd.read_csv(covid_file_path)

print('-'*50)
df.info()

print('-'*50)
print(df.head())

#원하는 컬럼만
selected_columns = ['iso_code', 'location', 'date','total_cases','population']
selected_df = df[selected_columns]
print('-'*50)
print(selected_df.head())

#locations = df['loaction']
locations = selected_df['location']
print('-'*50)
print(locations)

print('-'*50)
print(locations.unique())
print(locations.unique().size)

#South Korea
south_korea_df = selected_df[selected_df.location == 'South Korea']
print('-'*50)
print(south_korea_df.head())