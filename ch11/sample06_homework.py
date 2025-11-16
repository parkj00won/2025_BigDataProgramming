import pandas as pd
import matplotlib.pyplot as plt

from ch11.sample03 import sr_country

# 개발자 나라에 대한 차트
file_name = './data_count.csv'
df_raw = pd.read_csv(file_name)

COLUMN_COUNTRY = 'Country'
sr_country_count = df_raw.groupby(COLUMN_COUNTRY).size()

# 국가명 한국어 매핑 딕셔너리 추가
country_dict = {
    'United States of America': '미국',
    'India': '인도',
    'Germany': '독일',
    'United Kingdom of Great Britain and Northern Ireland': '영국',
    'Canada': '캐나다',
    'France': '프랑스',
    'Brazil': '브라질',
    'Poland': '폴란드',
    'Netherlands': '네덜란드',
    'Spain': '스페인',
    'Italy': '이탈리아',
    'Australia': '호주',
    'Russian Federation': '러시아',
    'Sweden': '스웨덴',
    'Turkey': '터키',
    'Switzerland': '스위스',
    'Austria': '오스트리아',
    'Israel': '이스라엘',
    'Iran, Islamic Republic of...': '이란',
    'Pakistan': '파키스탄'
}

# 인덱스(국가명)를 한국어로 변경
sr_country_count.index = sr_country_count.index.map(lambda x: country_dict.get(x, x))

sr_country_count.nlargest(20).plot.pie(figsize=(10, 10))

plt.tight_layout()
plt.show()