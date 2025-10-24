import os
import pandas as pd
from matplotlib import pyplot as plt
from ch05.common_function import init_plt

#kor 데이터(1, 1, 2....)
#usa 데이터(2, 3, 1....)
#index데이터(2020.01.19....)


# file_path에 대한 데이터 리턴 함수(dataframe)
def get_covid_data_series(file_path):
    kor_df = pd.read_csv(file_path)
    kor_index_df = kor_df.set_index('date')
    return kor_index_df['total_cases']
#end-def

kor_data = get_covid_data_series('../ch05/data/covid_korea.csv')
usa_data = get_covid_data_series('../ch05/data/covid_usa.csv')
index_data = kor_data.index
#index_data = usa_data.index 도 같은 인덱스라 (바로 위에 안 적고) 이걸로 적어도 됨.

print('kor_date tpye:',type(kor_data.index))

rate = 6.53

covid_data = pd.DataFrame(
    {
        '대한민국':kor_data * rate,
        '미국': usa_data,
    }, index=index_data)
#covid_data['2022-01-01':'2022-12-31'].plot.line(rot = 45) #특정 기간
#[:] <-이거 기억하지??
#rot 옵션
covid_data[:].plot.line(rot = 45) #전체 기간

plt.show()

# kor_total_cases = kor_df['total_cases']
# print(type(kor_total_cases))
# print(type(kor_df))