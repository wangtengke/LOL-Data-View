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

def Dam_Eco(player_a, player_b,player_info_a,player_info_b):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 新建figure
    fig = plt.figure()
    # 定义数据
    player_eco=[]
    player_dam=[]
    player_img=[]
    for player_a_name in player_a:
        player_eco.append(player_a[player_a_name][0])
        player_dam.append(player_a[player_a_name][1])
        player_img.append(player_a[player_a_name][2])
    for player_b_name in player_b:
        player_eco.append(player_b[player_b_name][0])
        player_dam.append(player_b[player_b_name][1])
        player_img.append(player_b[player_b_name][2])

    player_name=[]
    player_heroname=[]
    for k in player_info_a:
        player_name.append(k)
        player_heroname.append(player_info_a[k])
    for i in player_info_b:
        # i=i.capitalize()
        player_name.append(i)
        player_heroname.append(player_info_b[i])
    x = [0, max(player_eco)]
    y = [0, max(player_dam)]
    # 新建区域ax1
    # figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.7
    # 获得绘制的句柄
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(x, y, '--k')
    dam_eco=0
    max_dam_eco=0
    dam_0=0
    max_dam_0=0
    eco_0 = 0
    max_eco_0 = 0
    for i in range(0,10):
        if player_dam[i]/player_eco[i]>dam_eco:
            dam_eco=player_dam[i]/player_eco[i]
            max_dam_eco=i
        if player_dam[i]>dam_0:
            dam_0=player_dam[i]
            max_dam_0=i
        if player_eco[i]>eco_0:
            eco_0=player_eco[i]
            max_eco_0=i
    ax1.set_title('[全场最高经济]'+player_name[max_eco_0]+'的'+player_heroname[max_eco_0]+'----'+str(eco_0)+'块\n[全场最高伤害]'+player_name[max_dam_0]+'的'+player_heroname[max_dam_0]+'----'+str(dam_0)+'点\n[伤害经济比最高]'+player_name[max_dam_eco]+'的'+player_heroname[max_dam_eco]+'----'+str(round(dam_eco,2))+'伤害=1经济\n')
    ax1.set_xlabel('经济')
    ax1.set_ylabel('伤害')
    for i in range(0,10):
    # 新增区域ax2,嵌套在ax1内
        left, bottom, width, height = 0.1 + player_eco[i] * 0.8 / max(player_eco) - 0.035, 0.1 + player_dam[i] * 0.7 / max(player_dam) - 0.035, 0.07, 0.07
    # 获得绘制的句柄
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(player_img[i])
        io.imshow(image)
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\2.png')
    # plt.show()
