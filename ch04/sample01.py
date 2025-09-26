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