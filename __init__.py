stylelist = {}

# スタイルのインストール
import matplotlib.pyplot as plt
from .styles import default
from .styles import seaborn

def setStyle(name):

    # 存在しないスタイルを指定した場合
    if not name in stylelist:
        print("the style name doesn't exist.")
        help()
        return -1

    # スタイルの設定
    for key, value in stylelist[name].items():
        plt.rcParams[key] = value
    
def help():

    print("Options:")
    print("-"*20)
    
    for key in stylelist.keys():
        print(f"・{key}")
    