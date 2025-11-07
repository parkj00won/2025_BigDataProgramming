import os
import pandas as pd
from matplotlib import pyplot as plt
# from ch05.common_function import init_plt
# from ch05.sample03 import index_data


#kor 데이터(1, 1, 2....)
#usa 데이터(2, 3, 1....)
#index데이터(2020.01.19....)

#TODO: 백현아 이코드 확인좀!

# file_path에 대한 데이터 리턴 함수(dataframe)
def get_covid_data_series(file_path):
    kor_df = pd.read_csv(file_path)
    kor_index_df = kor_df.set_index('date')
    return kor_index_df['total_cases']
#end-def

#2020-01-01 ~ 2021-12-01
kor_data_sr = get_covid_data_series('../ch05/data/covid_korea.csv')
#2021-02-01 ~ 2022-01-01
kor_data_index = kor_data_sr.index

hi_data_sr = get_covid_data_series('./hi_covid_data.csv')
hi_data_index = hi_data_sr.index

#2020-01-01 ~ 2-22-01-01
#2개의 인덱스를 합침
data_index = kor_data_index.union(hi_data_index)

#인구비율 구하기!!!!
kor_pop = pd.read_csv('../ch05/data/covid_korea.csv')['population'][0]
hi_pop = pd.read_csv('./hi_covid_data.csv')['population'][0]

hi_rate = kor_pop / hi_pop

covid_df = pd.DataFrame(
    {
        '대한민국':kor_data_sr,
        '하와이': hi_data_sr * hi_rate,
    }, index= data_index)

covid_df.plot.line()
plt.show()



# kor_total_cases = kor_df['total_cases']
# print(type(kor_total_cases))
# print(type(kor_df))