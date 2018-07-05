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


def Pos_Jungle(player_a_Jungle, player_b_Jungle, a_hotpoint, b_hotpoint):
    # https: // img1.famulei.com / static / 59 / images / match / map.png
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 新建figure
    fig = plt.figure()
    fig.set_size_inches(4, 8)
    time_a = 0
    time_b = 0
    for k in range(2):
        left, bottom, width, height = 0, (1 - k) * 0.5, 1, 0.475
        ax1 = fig.add_axes([left, bottom, width, height])
        ax1.set_title(str(k * 2) + '-' + str((k + 1) * 2) + '分钟打野路线(B=回城，m=分钟)')
        ax1.spines['right'].set_color('none')
        ax1.spines['top'].set_color('none')
        ax1.spines['left'].set_color('none')
        ax1.spines['bottom'].set_color('none')
        ax1.set_xticks([])
        ax1.set_yticks([])
        image = io.imread('https://img1.famulei.com/static/59/images/match/map.png')
        io.imshow(image)
        for i in range(k * 24, (k + 1) * 24):
            if a_hotpoint[i + 1][1] > 80 and a_hotpoint[i + 1][0] < 20 and (a_hotpoint[i][1] < 80 or a_hotpoint[i][
                0] > 20):
                ax1.text(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8, 'B', fontsize=10,
                         bbox=dict(facecolor="b", alpha=0.5))
            else:
                ax1.annotate('', color='b', horizontalalignment='center',
                             xy=(a_hotpoint[i + 1][0] * 8, a_hotpoint[i + 1][1] * 8),
                             xytext=(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8),
                             arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
            if i % 12 == 0:
                ax1.text(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8, str(time_a) + 'm', color='w', fontsize=8,
                         bbox=dict(facecolor="blue", alpha=0.5))
                time_a = time_a + 1
        for i in range(k * 24, (k + 1) * 24):
            if b_hotpoint[i + 1][0] > 80 and b_hotpoint[i + 1][1] < 20 and (b_hotpoint[i][0] < 80 or b_hotpoint[i][
                1] > 20):
                ax1.text(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8, 'B', fontsize=10,
                         bbox=dict(facecolor="r", alpha=0.5))
            else:
                ax1.annotate('', color='r', horizontalalignment='center',
                             xy=(b_hotpoint[i + 1][0] * 8, b_hotpoint[i + 1][1] * 8),
                             xytext=(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8),
                             arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            if i % 12 == 0:
                ax1.text(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8, str(time_b) + 'm', color='w', fontsize=8,
                         bbox=dict(facecolor="r", alpha=0.5))
                time_b = time_b + 1

        ax2 = fig.add_axes([left + 0.025, bottom + 0.025, width / 20, height / 20])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(player_a_Jungle[1])
        io.imshow(image)
        ax2 = fig.add_axes([left + 1 - 0.025 - width / 20, bottom + 0.5 - 0.025 - height / 20, width / 20, height / 20])
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
    fig = plt.figure()
    fig.set_size_inches(4, 8)
    for k in range(2, 4):
        left, bottom, width, height = 0, (3 - k) * 0.5, 1, 0.475
        ax1 = fig.add_axes([left, bottom, width, height])
        ax1.set_title(str(k * 2) + '-' + str((k + 1) * 2) + '分钟打野路线(B=回城，m=分钟)')
        ax1.spines['right'].set_color('none')
        ax1.spines['top'].set_color('none')
        ax1.spines['left'].set_color('none')
        ax1.spines['bottom'].set_color('none')
        ax1.set_xticks([])
        ax1.set_yticks([])
        image = io.imread('https://img1.famulei.com/static/59/images/match/map.png')
        io.imshow(image)
        for i in range(k * 24, (k + 1) * 24):
            if a_hotpoint[i + 1][1] > 80 and a_hotpoint[i + 1][0] < 20 and (a_hotpoint[i][1] < 80 or a_hotpoint[i][0] > 20):
                ax1.text(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8, 'B', fontsize=10,
                         bbox=dict(facecolor="b", alpha=0.5))
            else:
                ax1.annotate('', color='b', horizontalalignment='center',
                             xy=(a_hotpoint[i + 1][0] * 8, a_hotpoint[i + 1][1] * 8),
                             xytext=(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8),
                             arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
            if i % 12 == 0:
                ax1.text(a_hotpoint[i][0] * 8, a_hotpoint[i][1] * 8, str(time_a) + 'm', color='w', fontsize=8,
                         bbox=dict(facecolor="b", alpha=0.5))
                time_a = time_a + 1
        for i in range(k * 24, (k + 1) * 24):
            if b_hotpoint[i + 1][0] > 80 and b_hotpoint[i + 1][1] < 20 and (b_hotpoint[i][0] < 80 or b_hotpoint[i][1] > 20):
                ax1.text(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8, 'B', fontsize=10,
                         bbox=dict(facecolor="r", alpha=0.5))
            else:
                ax1.annotate('', color='r', horizontalalignment='center',
                             xy=(b_hotpoint[i + 1][0] * 8, b_hotpoint[i + 1][1] * 8),
                             xytext=(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8),
                             arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            if i % 12 == 0:
                ax1.text(b_hotpoint[i][0] * 8, b_hotpoint[i][1] * 8, str(time_b) + 'm', color='w', fontsize=8,
                         bbox=dict(facecolor="r", alpha=0.5))
                time_b = time_b + 1

        ax2 = fig.add_axes([left + 0.025, bottom + 0.025, width / 20, height / 20])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(player_a_Jungle[1])
        io.imshow(image)
        ax2 = fig.add_axes([left + 1 - 0.025 - width / 20, bottom + 0.5 - 0.025 - height / 20, width / 20, height / 20])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(player_b_Jungle[1])
        io.imshow(image)
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\7.png')
    plt.show()
