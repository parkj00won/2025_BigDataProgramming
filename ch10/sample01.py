import os
from importlib.util import source_hash
import pandas as pd
from matplotlib import pyplot as plt

file_path = './hawaii-covid-data.csv'
df_raw = pd.read_csv(file_path)

print('-'*50)
print(df_raw.head())

print('-'*50)
print(df_raw.info())

df_raw['date'] = pd.to_datetime(df_raw['submission_date'])

# 2021년도 하와이 인구수: 1,441,553명
df_raw['population'] = 1441553
df_raw['total_cases'] = df_raw['tot_cases']

# 원하는 컬럼 : 날짜, 감연자수,인구수
print('-'*50)
print(df_raw.info())

# # 기존 아와이 csv에 인구수 없음
# # df_raw 데이터프레임에 population컬럼을 추가
# df_raw['population'] = 0

hi_columns = ['date', 'total_cases', 'population']
df_raw_filter = df_raw[hi_columns]
print('-'*50)
print(df_raw_filter.head())

print('-'*50)
print(df_raw_filter.info())

#ch05 sample01 복습하는 코드 1줄
df_raw_filter.set_index('date', inplace=True)
# df_raw_filter_index = df_raw_filter.set_index('date')
# df_raw_filter = df_raw_filter_index
print('-'*50)
print(df_raw_filter.head())

#저장(data frame -> csv파일로 저장)
hi_file_path = './hi_covid_data.csv'
if os.path.exists(hi_file_path):
    os.remove(hi_file_path)
df_raw_filter.to_csv(hi_file_path)

# print('-'*50)
# print(df_raw_filter['date'].dt.year.unique())

# df_raw_filter['date'] = pd.to_datetime(df_raw_filter['submission_date'], format='%m/%d/%y')
#
# print('-'*50)
# print(df_raw_filter.info())