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

def First_WardsPlaced(event_wardplaced):
    # https: // img1.famulei.com / static / 59 / images / match / map.png
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 新建figure
    fig = plt.figure()
    fig.set_size_inches(5, 6)
    left, bottom, width, height = 0, 0, 1, 0.95
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.set_title('(一级视野)3分钟前双方视野情况\n时间格式XX:XX-XX:XX（视野开始到结束时间）')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    ax1.spines['bottom'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    image = io.imread('https://img1.famulei.com/static/59/images/match/map.png')
    io.imshow(image)

    for first_eye in event_wardplaced:
        if first_eye['start_time']<180:
            if first_eye['groupId']==100:
                ax1.scatter(first_eye['axis_x']*8,first_eye['axis_y']*8, c='b', s=20)
                ax1.annotate('', color='b', horizontalalignment='center', xy=(first_eye['axis_x']*8, first_eye['axis_y']*8),
                            xytext=(first_eye['axis_x']*8, first_eye['axis_y']*8+40),
                            arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2)
                             )
                ax1.text(first_eye['axis_x']*8-80, first_eye['axis_y']*8+40, str(first_eye['start_time']//60)+':'+str(first_eye['start_time']%60)+'-'+str(first_eye['end_time']//60)+':'+str(first_eye['end_time']%60) , color='w', fontsize=8,
                         bbox=dict(facecolor="blue", alpha=0.5))
            else:
                ax1.scatter(first_eye['axis_x']*8, first_eye['axis_y']*8, c='r', s=20)
                ax1.annotate('', color='r', horizontalalignment='center',
                             xy=(first_eye['axis_x'] * 8, first_eye['axis_y'] * 8),
                             xytext=(first_eye['axis_x'] * 8, first_eye['axis_y'] * 8-30),
                             arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
                ax1.text(first_eye['axis_x'] * 8, first_eye['axis_y'] * 8 -30,
                         str(first_eye['start_time'] // 60) + ':' + str(first_eye['start_time'] % 60) + '-' + str(
                             first_eye['end_time'] // 60) + ':' + str(first_eye['end_time'] % 60), color='w',
                         fontsize=8,
                         bbox=dict(facecolor="red", alpha=0.5))
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\11.png')
    plt.show()
    pass