import pandas as pd

covid_file_path = './data/owid-covid-data.csv'
df = pd.read_csv(covid_file_path)
print(df)