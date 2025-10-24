import os
from importlib.util import source_hash
import pandas as pd
from matplotlib import pyplot as plt


#직접 풀어보기2
def get_covid_data(iso_code, rate_yn):
    file_path = './data/common_covid.csv'

    raw_df = pd.read_csv(file_path)

    # 인구비율 기준국가는 미국(USA)에 해당하는 인구수
    common_population_sr = raw_df[raw_df.iso_code == 'USA']['population']
    common_population = common_population_sr.iat[0]
    print('common population:', common_population)
    #iat란??

    #매개변수로 넘어온 iso_code 국사의 인구수
    cur_population = raw_df[raw_df.iso_code == iso_code]['population']
    cur_population = cur_population.iat[0]
    print('current population:', cur_population)

    rate = round(common_population/cur_population, 2)
    print('rate:', rate)

    filter_df = raw_df[raw_df.iso_code == iso_code]
    filter_index_df = filter_df.set_index('date')

    if rate_yn:
        return filter_index_df['total_cases'] * rate
    else:
        return filter_index_df['total_cases']

    return filter_index_df['total_cases'] * rate
#end-def

kor_data = get_covid_data('KOR',False)
usa_data = get_covid_data('USA',False)
fra_data = get_covid_data('FRA',False)
gbr_data = get_covid_data('GBR',False)
pol_data = get_covid_data('POL',False)
index_data = kor_data.index

#추가 작성 코드!!
#인구비율 감안해서 로직 수정하기


covid_data = pd.DataFrame({
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data,
}, index=index_data)
covid_data[:].plot.line(rot = 45) #전체 기간

kor_data = get_covid_data('KOR',True)
usa_data = get_covid_data('USA',True)
fra_data = get_covid_data('FRA',True)
gbr_data = get_covid_data('GBR',True)
pol_data = get_covid_data('POL',True)
index_data = kor_data.index

#추가 작성 코드!!
#인구비율 감안해서 로직 수정하기


covid_data = pd.DataFrame({
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data,
}, index=index_data)
covid_data[:].plot.line(rot = 45) #전체 기간
plt.show()