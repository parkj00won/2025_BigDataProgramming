import os
import pandas as pd
from matplotlib import pyplot as plt
from ch05.common_function import init_plt

#kor 데이터(1, 1, 2....)
#usa 데이터(2, 3, 1....)
#index데이터(2020.01.19....)


# file_path에 대한 데이터 리턴 함수(dataframe)
def get_covid_data_series(file_path):
    df = pd.read_csv(file_path)
    index_df = df.set_index('date')
    return index_df['total_cases']
#end-def

def get_population(file_path):
    df = pd.read_csv(file_path)
    index_df = df.set_index('date')
    return index_df['population']['2020-01-05']
#end-def

kor_population = get_population('../ch05/data/covid_korea.csv')
usa_population = get_population('../ch05/data/covid_usa.csv')

print('-'*50)
print('대한민국 인구수:',kor_population)
print('미국 인구수:', usa_population)

rate = usa_population/kor_population
print('인구비율: ', rate)
rate = round(usa_population/kor_population,2)
print('인구비율: ', rate)