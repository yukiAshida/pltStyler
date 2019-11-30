from cycler import cycler
from .. import stylelist

# このスタイル全体の名前（ファイル名）
STYLE_NAME = __file__.split("\\")[-1].split(".")[0]

FIGURE = {
    # 基本設定（サイズ・dpi・限度Figure数）
    'figure.figsize':[6.4, 4.8],
    'figure.dpi':100.0,
    'figure.max_open_warning':20,

    # subplot同士の間のスペース（0 ~ 1）
    'figure.subplot.hspace':0.2,
    'figure.subplot.wspace':0.2,

    # subplotとFigureの間（上下左右）のスペース（0 ~ 1）
    'figure.subplot.bottom':0.11,
    'figure.subplot.left':0.125,
    'figure.subplot.right':0.9,
    'figure.subplot.top':0.88,
}

# 独自カラー定義
COLORS = {}

AXES = {
    # AXESのエッジ・フェイスの色
    'axes.edgecolor':'k',
    'axes.facecolor':'w',

    # AXESのエッジの太さ
    'axes.linewidth':0.8,

    # AXESのエッジをそれぞれ表示するかどうか
    'axes.spines.bottom':True,
    'axes.spines.left':True,
    'axes.spines.right':True,
    'axes.spines.top':True,

    # AXESの内側マージンをx,yそれぞれどれくらいとるか（0~1）
    'axes.xmargin':0.05,
    'axes.ymargin':0.05,

    # matplotlib全体で使われる色
    'axes.prop_cycle':cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']),    
}

TITLE = {
    # タイトルのAXESからの距離
    'axes.titlepad':6.0,

    # タイトルのサイズ・太さ
    'axes.titlesize':'large',     # 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'
    'axes.titleweight':'normal',  # 'normal', 'bold'
}

LABEL = {

    # x(y)軸ラベルのAXESからの距離
    'axes.labelpad':4.0,

    # x(y)軸ラベルのサイズ・太さ・色
    'axes.labelsize':'medium',    # 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'
    'axes.labelweight':'normal',  # 'normal', 'bold'
    'axes.labelcolor':'k',
}

GRID = {
    # グリッドを出すかどうか（'x'は縦線のみ、'y'は横線のみ）
    'axes.grid':False,
    'axes.grid.axis':'both',   # 'both', 'x', 'y'
    'axes.grid.which':'both',  # 'both', 'major', 'minor'

    # グリッドの線種・太さ・色・透過率
    'grid.linestyle':'-', # '-'('solid'), '--'('dashed'), '-.'('dashdot'), ':'('dotted')
    'grid.linewidth':0.8,
    'grid.color':'#b0b0b0',
    'grid.alpha':1.0,
}



TICKS = {
    
    # 目盛線と軸目盛の位置関係
    'xtick.alignment':'center',             # 'center', 'top', 'bottom', 'baseline', 'center_baseline'
    'ytick.alignment':'center_baseline',    # 'center', 'top', 'bottom', 'baseline', 'center_baseline'

    # 目盛線の向き
    'xtick.direction':'out',  # 'in', 'out'
    'ytick.direction':'out',  # 'in', 'out'
    
    # 上下左右の各目盛線を表示するかどうか
    'xtick.bottom':True,
    'xtick.top':False,
    'ytick.left':True,
    'ytick.right':False,
    
    # 上下左右の各主目盛線を表示するかどうか
    'xtick.major.bottom':True,
    'xtick.major.top':False,    
    'ytick.major.left':True,
    'ytick.major.right':False,

    # 上下左右の各補助目盛線を表示するかどうか
    'xtick.minor.visible':False,
    'ytick.minor.visible':False,    
    'xtick.minor.bottom':True,
    'xtick.minor.top':False,
    'ytick.minor.left':True,
    'ytick.minor.right':False,

    # 軸目盛のサイズ
    'xtick.labelsize':'medium',  # 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'
    'ytick.labelsize':'medium',  # 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'
    
    # 軸目盛の色（目盛線も変わる）
    'xtick.color':'k',
    'ytick.color':'k',
    
    # 軸目盛と軸の距離
    'xtick.major.pad':3.5,
    'ytick.major.pad':3.5,
    'xtick.minor.pad':3.4,
    'ytick.minor.pad':3.4,

    # 主/圃場軸目盛線の長さ・太さ
    'xtick.major.size':3.5,
    'xtick.major.width':0.8,
    'xtick.minor.size':2.0,
    'xtick.minor.width':0.6,
    'ytick.major.size':3.5,
    'ytick.major.width':0.8,
    'ytick.minor.size':2.0,
    'ytick.minor.width':0.6,
}

# 凡例 ＝ アイコン (+ マーカー) + ラベル
# 凡例 + フレーム
LEGEND = {

    # 大体の位置
    'legend.loc':'best',         # 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

    # 位置調整
    'legend.handleheight':0.7,   # アイコンの高さ
    'legend.handlelength':2.0,   # アイコンの横幅
    'legend.borderaxespad':0.5,  # フレームとAXESの間のスペース 
    'legend.borderpad':0.4,      # 凡例とフレーム間のスペース
    'legend.handletextpad':0.8,  # アイコンとラベルの間のスペース
    'legend.labelspacing':0.5,   # アイコン(ラベル)同士の縦のスペース
    'legend.columnspacing':2.0,  # 凡例の列間のスペース（凡例が2列以上ある場合）    

    # ラベルのサイズ
    'legend.fontsize':'medium',  # 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'

    # マーカー
    'legend.markerscale':1.0,    # 凡例中のマーカーの大きさ
    'legend.numpoints':1,        # plotの凡例に対して、何個マーカーを表示するか
    'legend.scatterpoints':1,    # scatterの凡例に対して、何個マーカーを表示するか

    # フレーム
    'legend.frameon':True,         # フレームの有無
    'legend.edgecolor':'0.8',      # フレームのエッジの色
    'legend.facecolor':'inherit',  # フレームの背景色
    'legend.framealpha':0.8,       # フレームの透過率

    # オプション
    'legend.shadow':False,       # 凡例が浮き出て見える
    'legend.fancybox':True,      # 角を丸めるかどうか

}

# DatetimeObjectを渡した際に、差異のある最も大きいオーダーが採用される
# [Date(2019,1,...), Date(2019,2), ...]が渡された場合は 'date.autoformatter.month' の形式で表示される
# %Y(year) %m(month) %d(day) %H(hour) %M(minute) %S(seconds) %f(microseconds)
DATE = {
    'date.autoformatter.day':'%Y-%m-%d',
    'date.autoformatter.hour':'%m-%d %H',
    'date.autoformatter.microsecond':'%M:%S.%f',
    'date.autoformatter.minute':'%d %H:%M',
    'date.autoformatter.month':'%Y-%m',
    'date.autoformatter.second':'%H:%M:%S',
    'date.autoformatter.year':'%Y',
}



# FONT = {
#     'font.cursive':['Apple Chancery', 'Textile', 'Zapf Chancery', 'Sand', 'Script MT', 'Felipa', 'cursive'],
#     'font.family':['sans-serif'],
#     'font.fantasy':['Comic Sans MS', 'Chicago', 'Charcoal', 'ImpactWestern', 'Humor Sans', 'xkcd', 'fantasy'],
#     'font.monospace':['DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Computer Modern Typewriter', 'Andale Mono', 'Nimbus Mono L', 'Courier New', 'Courier', 'Fixed', 'Terminal', 'monospace'],
#     'font.sans-serif':['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif'],
#     'font.serif':['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif'],
#     'font.size':10.0,
#     'font.stretch':'normal',
#     'font.style':'normal',
#     'font.variant':'normal',
#     'font.weight':'normal',
# }

# TEXT = {
#     'text.antialiased':True,
#     'text.color':'k',
#     'text.hinting':'auto',
#     'text.hinting_factor':8,
#     'text.latex.preamble':[],
#     'text.latex.preview':False,
#     'text.latex.unicode':False,
#     'text.usetex':False,
# }


stylelist[STYLE_NAME] = {}
stylelist[STYLE_NAME].update(FIGURE)
stylelist[STYLE_NAME].update(AXES)
stylelist[STYLE_NAME].update(TITLE)
stylelist[STYLE_NAME].update(LABEL)
stylelist[STYLE_NAME].update(TITLE)
stylelist[STYLE_NAME].update(GRID)
stylelist[STYLE_NAME].update(TICKS)
stylelist[STYLE_NAME].update(LEGEND)
stylelist[STYLE_NAME].update(DATE)