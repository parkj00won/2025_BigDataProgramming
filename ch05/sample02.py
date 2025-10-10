import os
from importlib.util import source_hash
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc

from ch05.sample03 import is_windows_platform, is_mac_platform

#한글폰트 설정
if is_windows_platform():
    rc('font', family='Malgun Gothic')
elif is_mac_platform():
    rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

jumsu1 = [3.5, 4.0, 4.5, 3.8]
jumsu2 = [3.0, 4.5, 4.0, 3.2]
year = [2024, 2025, 2026, 2027]

jumsu_df = pd.DataFrame(
    {
    '홍길동': jumsu1,
    '이순신': jumsu2,
    },index=year)

lines = jumsu_df.plot.line()

# 제목 및 라벨 추가
plt.rc('font', family='NanumGothic')
plt.title("연도별 점수 변화")
plt.xlabel("Year")
plt.ylabel("Jumsu")
plt.grid(True)

plt.show()