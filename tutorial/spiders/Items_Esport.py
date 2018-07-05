#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from skimage import io
from pylab import *  # 支持中文
import matplotlib.image as mpimg  # mpimg 用于读取图片
from PIL import Image
def Items_Esport(Item_Build,game_time,player_pair_a,player_pair_b,team_nam):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 新建figure
    fig = plt.figure()
    fig.set_size_inches(6, 8)
    # 定义数据
    x = [0, 10000]
    y = [0, 10000]
    # 新建区域ax1
    # figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.3
    # 获得绘制的句柄
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(0, 0, game_time + 1, 1)
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    # ax1.set_yticks([])
    ax1.grid(axis='y', linestyle='--')
    # ax1.setx
    ax1.set_xlabel('时间')
    ax1.set_title('[ '+team_nam[0][0]+' ] 出装路线',color='blue')

    left, bottom, width, height = 0.1, 0.6, 0.8, 0.3
    # 获得绘制的句柄
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(0, 0, game_time + 1, 1)
    ax1.spines['right'].set_color('none')

    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    # ax1.set_yticks([])
    ax1.grid(axis='y', linestyle='--')
    # ax1.setx
    ax1.set_title('[ '+team_nam[1][0]+' ] 出装路线',color='red')
    high = 0.12
    high1 = 0.62
    red_id = []
    blue_id = []
    red_imge = []
    blue_imge = []
    for i in range(0, 5):
        red_id.append(player_pair_b[i][0])
        red_imge.append(player_pair_b[i][1])
    for i in range(0, 5):
        blue_id.append(player_pair_a[i][0])
        blue_imge.append(player_pair_a[i][1])

    for i in range(0, 5):
            left, bottom, width, height = 0.03, high, 0.04, 0.04
            # 获得绘制的句柄
            ax2 = fig.add_axes([left, bottom, width, height])
            ax2.spines['right'].set_color('none')
            ax2.spines['top'].set_color('none')
            ax2.spines['left'].set_color('none')
            ax2.spines['bottom'].set_color('none')
            ax2.set_xticks([])
            ax2.set_yticks([])
            image = io.imread(blue_imge[i])
            io.imshow(image)
            for k in Item_Build:
                if k['itemId']>3000 and k['participantId']==i+1:
                    # test=Item_Build[i][k]

                    time = k['timestamp']/60000
                    left, bottom, width, height = 0.1 + (time+1.85) / (
                    game_time + 1+1.85+1.85) * 0.8-0.02, high, 0.04, 0.04
                    # 获得绘制的句柄
                    ax2 = fig.add_axes([left, bottom, width, height])
                    ax2.spines['right'].set_color('none')
                    ax2.spines['top'].set_color('none')
                    ax2.spines['left'].set_color('none')
                    ax2.spines['bottom'].set_color('none')
                    ax2.set_xticks([])
                    ax2.set_yticks([])
                    # image=Image.open(k['image'])
                    # plt.show(image)
                    image = io.imread('https://ddragon.leagueoflegends.com/cdn/8.8.2/img/item/'+str(k['itemId'])+'.png')
                    io.imshow(image)
            high = high + 0.055

    # plt.show()
    for i in range(0, 5):

            left, bottom, width, height = 0.03, high1, 0.04, 0.04
            # 获得绘制的句柄
            ax2 = fig.add_axes([left, bottom, width, height])
            ax2.spines['right'].set_color('none')
            ax2.spines['top'].set_color('none')
            ax2.spines['left'].set_color('none')
            ax2.spines['bottom'].set_color('none')
            ax2.set_xticks([])
            ax2.set_yticks([])
            image = io.imread(red_imge[i])
            io.imshow(image)
            for k in Item_Build:
                if k['itemId'] > 3000 and k['participantId']==i+6:
                    # test=Item_Build[i][k]

                    time = k['timestamp'] / 60000
                    left, bottom, width, height = 0.1 + (time+1.85) / (
                        game_time + 1+1.85+1.85) * 0.8-0.02, high1, 0.04, 0.04
                    # 获得绘制的句柄
                    ax2 = fig.add_axes([left, bottom, width, height])
                    ax2.spines['right'].set_color('none')
                    ax2.spines['top'].set_color('none')
                    ax2.spines['left'].set_color('none')
                    ax2.spines['bottom'].set_color('none')
                    ax2.set_xticks([])
                    ax2.set_yticks([])
                    # image=Image.open(k['image'])
                    # plt.show(image)
                    image = io.imread('https://ddragon.leagueoflegends.com/cdn/8.8.2/img/item/'+str(k['itemId'])+'.png')
                    io.imshow(image)

            high1 = high1 + 0.055

            print("12")

    # 新增区域ax2,嵌套在ax1内
    # for i in Item_Build:
    #     for k in i:
    #         if 'item/3' in k['image']:
    #             # test=Item_Build[i][k]
    #             test = (k['date']).split(':')
    #             time = eval(test[0])
    #             left, bottom, width, height = 0.03 + 0.1 + time / (eval(game_time[0]) + 1) * 0.8, high, 0.05, 0.05
    #             # 获得绘制的句柄
    #             ax2 = fig.add_axes([left, bottom, width, height])
    #             ax2.spines['right'].set_color('none')
    #             ax2.spines['top'].set_color('none')
    #             ax2.spines['left'].set_color('none')
    #             ax2.spines['bottom'].set_color('none')
    #             ax2.set_xticks([])
    #             ax2.set_yticks([])
    #             image = io.imread(k['image'])
    #             io.imshow(image)

    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\3.png')
    # plt.show()
