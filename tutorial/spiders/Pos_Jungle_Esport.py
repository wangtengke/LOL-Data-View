# encoding=utf-8
import matplotlib.pyplot as plt
import plotly
from pylab import *  # 支持中文
import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


def Pos_Jungle_Esport(player_a_Jungle, player_b_Jungle, a_hotpoint, b_hotpoint):
    # https: // img1.famulei.com / static / 59 / images / match / map.png
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 新建figure
    fig = plt.figure()
    fig.set_size_inches(5, 6)
    time_a = 0
    time_b = 0

    left, bottom, width, height = 0,  0, 1, 0.95
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.set_title(str(0) + '-' + str(10) + '分钟打野路线(m=分钟)')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    ax1.spines['bottom'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    image = io.imread('https://matchhistory.na.leagueoflegends.com/assets/1.0.36/images/maps/map11.png')
    io.imshow(image)
    # plt.show()
    for i in range(0, 10):
        ax1.text(a_hotpoint[i]['x'] * 512/15000, 512-a_hotpoint[i]['y'] * 512/15000, str(time_a) + 'm', color='w', fontsize=10,
                 bbox=dict(facecolor="blue", alpha=0.5))
        time_a = time_a + 1
    for i in range(0, 10):
        ax1.text(b_hotpoint[i]['x'] * 512/15000, 512-b_hotpoint[i]['y'] * 512/15000, str(time_b) + 'm', color='w', fontsize=10,
                 bbox=dict(facecolor="r", alpha=0.5))
        time_b = time_b + 1

    ax2 = fig.add_axes([left + 0.025, bottom , width / 15, height / 15])
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax2.spines['bottom'].set_color('none')
    ax2.set_xticks([])
    ax2.set_yticks([])
    image = io.imread(player_a_Jungle[1])
    io.imshow(image)
    ax2 = fig.add_axes([left + 1 - 0.065 - width / 20, bottom + 0.98 - height / 10, width / 15, height / 15])
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax2.spines['bottom'].set_color('none')
    ax2.set_xticks([])
    ax2.set_yticks([])
    image = io.imread(player_b_Jungle[1])
    io.imshow(image)
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\6.png')
    # plt.show()

    # plt.show()
