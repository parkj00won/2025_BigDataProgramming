import os
import platform

#현재 파이썬이 실행되는 os 확인
# system = platform.system()
# print(system)

def is_windows_platform():
    return platform.system() == "Windows"

def is_mac_platform():
    return platform.system() == "Darwin"

def is_linux_platform():
    return platform.system() == "Linux"

def get_font_name():
    if is_windows_platform():
        return 'Malgun Gothic'
    elif is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'linuxfont!'
    else:
        return None

#한글 폰트 초기화
def init_plt():
    rc('font', family=get_font_name())
    plt.rcParams['axes.unicode_minus'] = 'False'