import os
import pandas as pd
from matplotlib import pyplot as plt


#kor 데이터(1, 1, 2....)
#usa 데이터(2, 3, 1....)
#index데이터(2020.01.19....)

# file_path에 대한 데이터 리턴 함수(dataframe)
def get_covid_data_series(file_path):
    kor_df = pd.read_csv(file_path)
    kor_index_df = kor_df.set_index('date')
    return kor_index_df['total_cases']
#end-deg

kor_data = get_covid_data_series('data/covid_korea.csv')
usa_data = get_covid_data_series('data/covid_usa.csv')
index_data = kor_data.index

covid_data = pd.DataFrame(
    {
        '대한민국':kor_data,
        '미국': usa_data,
    }, index=index_data)

covid_data.plot.line()
plt.show()

# kor_total_cases = kor_df['total_cases']
# print(type(kor_total_cases))
# print(type(kor_df))