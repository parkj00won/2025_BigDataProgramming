import os
from importlib.util import source_hash
import pandas as pd
from matplotlib import pyplot as plt


#직접 풀어보기2
def get_covid_data(iso_code):
    file_path = './data/common_covid.csv'

    df = pd.read_csv(file_path)
    filter_df = df[df.iso_code == iso_code]
    index_df = filter_df.set_index('date')

    return index_df['total_cases']
#end-def

kor_data = get_covid_data('KOR')
usa_data = get_covid_data('USA')
fra_data = get_covid_data('FRA')
gbr_data = get_covid_data('GBR')
pol_data = get_covid_data('POL')
index_data = kor_data.index

#추가 작성 코드!!
#인구비율 감안해서 로직 수정하기


data = {
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data,
}

covid_data = pd.DataFrame(data, index=index_data)
covid_data[:].plot.line(rot = 45) #전체 기간
plt.show()