import pandas as pd
from matplotlib import pyplot as plt

# 1단계: CSV 파일 읽기
file_name = '../ch11/survey_raw.csv'
df_raw = pd.read_csv(file_name)

print('-'*50)
print('전체 데이터 개수:', len(df_raw))
print('-'*50)

# 2단계: 나이가 '35-44 years old'인 데이터만 필터링
COL_AGE = 'Age'
df_filtered = df_raw[df_raw[COL_AGE] == '35-44 years old']
print('35-44세 개발자 데이터 개수:', len(df_filtered))
print('-'*50)

# 3단계: 프로그래밍 언어 컬럼에서 데이터 추출
COL_LANG = 'LanguageHaveWorkedWith'
data_lang = df_filtered[COL_LANG]

# NaN 값 제거 (값이 없는 행 제거)
data_lang = data_lang.dropna()
print('언어 데이터가 있는 개수:', len(data_lang))
print('-'*50)

# 4단계: 세미콜론(;)으로 구분된 언어들을 분리
data_lang = data_lang.str.split(';')
print('분리된 언어 데이터 (상위 3개):')
print(data_lang.head(3))
print('-'*50)

# 5단계: explode()를 사용하여 각 요소를 별도 행으로 변환
data_lang2 = data_lang.explode()
print('전개된 언어 데이터 (상위 10개):')
print(data_lang2.head(10))
print('-'*50)

# 6단계: 각 언어별 사용 빈도 계산
data_lang3 = data_lang2.groupby(data_lang2).size()
data_lang3 = data_lang3.sort_values(ascending=False)
print('언어별 사용 빈도 (상위 10개):')
print(data_lang3.head(10))
print('-'*50)

# 7단계: 상위 5개 언어 선택
top_5_langs = data_lang3.nlargest(5)
print('상위 5개 언어:')
print(top_5_langs)
print('-'*50)

# 8단계: 파이 차트 생성
plt.figure(figsize=(10, 8))
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
top_5_langs.plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 11, 'weight': 'bold'}
)
# plt.title('35-44 Years Old Developers\nTop 5 Programming Languages',
plt.title('35-44살 개발자들이 쓰는 \n프로그래밍 언어 상위 5개',
          fontsize=14, fontweight='bold', pad=20)
plt.ylabel('')

plt.tight_layout()

# 9단계: 이미지 저장
plt.savefig('./ch12_homework.png', dpi=300, bbox_inches='tight')

plt.show()