# -*- coding: cp936 -*-
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from skimage import io
from pylab import *  # 支持中文

def Best_Partner(assisnt, player_pair_a, player_pair_b,team_name):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    image = []
    group = []
    group_co = 0
    group_weight = []
    group_name=[]
    for i in range(5):
        image.append(player_pair_a[i][1])
    for i in range(0, 5):
        for k in range(i + 1, 5):
            group.append([player_pair_a[i][0], player_pair_a[k][0]])
            group_name.append([player_pair_a[i][2], player_pair_a[k][2]])
    for group_event in group:
        for kill_event in assisnt:
            event = [False for c in group_event if c not in kill_event]
            if event:
                pass
            else:
                group_co += 1
        group_weight.append(group_co)
        group_co = 0
    print("1")

    fig = plt.figure()
    fig.set_size_inches(6, 8)
    weight_a = group_weight
    best_group=group_name[group_weight.index(max(group_weight))]
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.4])
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    ax1.spines['bottom'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    G = nx.Graph()
    count = 0
    # for group in team_a:
    #     G.add_edge(group[0],group[1],weight=weight_a[count])
    #     count+=1
    # for i in range(3):
    # G.add_node(i)
    G.add_weighted_edges_from(
        [(0, 1, weight_a[0]), (0, 2, weight_a[1]), (0, 3, weight_a[2]), (0, 4, weight_a[3]), (1, 2, weight_a[4]),
         (1, 3, weight_a[5]), (1, 4, weight_a[6]), (2, 3, weight_a[7]), (2, 4, weight_a[8]),
         (3, 4, weight_a[9])])  # 添加边的权值

    pos = [(1.5, 0.5), (3.5, 0.5), (0.5, 2), (4.5, 2), (2.5, 3)]  # 元组中的两个数字是第i（从0开始计数）个点的坐标
    text_pos = []
    for i in range(0, 5):
        for k in range(i + 1, 5):
            text_pos.append([(pos[i][0] + pos[k][0]) / 2, (pos[i][1] + pos[k][1]) / 2])
    for weight in range(0, 10):
        if weight_a[weight] != 0:
            plt.text(text_pos[weight][0], text_pos[weight][1] - 0.05, weight_a[weight], color='w', ha='center',
                     wrap=True,
                     fontsize=12, bbox=dict(facecolor="b", alpha=0.5))
    # nx.draw(G, pos, with_labels=True, node_color='white', edge_color='black', alpha=0.2, width=10)  # 按参数构图
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    for i in range(0, 10):
        nx.draw_networkx_edges(G, pos, edgelist=[elarge[i]], width=weight_a[i], alpha=0.2)
    plt.xlim(0, 5)  # 设置首界面X轴坐标范围
    plt.ylim(0, 3.5)  # 设置首界面Y轴坐标范围

    image_i = 0
    for p in pos:
        ax2 = fig.add_axes([0.05 + p[0] * 0.8 / 5, 0.05 + p[1] * 0.4 / 3.5, 0.1, 0.1])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image1 = io.imread(image[image_i])
        io.imshow(image1)
        image_i += 1
    ax1.set_title('[ '+team_name[0][0]+' 最佳组合 ]---('+best_group[0]+'&'+best_group[1]+')携手击杀'+str(max(group_weight))+'人',color='b')

    image = []
    group = []
    group_co = 0
    group_weight = []
    group_name = []
    for i in range(5):
        image.append(player_pair_b[i][1])
    for i in range(0, 5):
        for k in range(i + 1, 5):
            group.append([player_pair_b[i][0], player_pair_b[k][0]])
            group_name.append([player_pair_b[i][2], player_pair_b[k][2]])

    for group_event in group:
        for kill_event in assisnt:
            event = [False for c in group_event if c not in kill_event]
            if event:
                pass
            else:
                group_co += 1
        group_weight.append(group_co)
        group_co = 0
    print("1")
    weight_a = group_weight
    best_group = group_name[group_weight.index(max(group_weight))]
    ax1 = fig.add_axes([0.1, 0.55, 0.8, 0.4])
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    ax1.spines['bottom'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    G = nx.Graph()
    count = 0
    # for group in team_a:
    #     G.add_edge(group[0],group[1],weight=weight_a[count])
    #     count+=1
    # for i in range(3):
    # G.add_node(i)
    G.add_weighted_edges_from(
        [(0, 1, weight_a[0]), (0, 2, weight_a[1]), (0, 3, weight_a[2]), (0, 4, weight_a[3]), (1, 2, weight_a[4]),
         (1, 3, weight_a[5]), (1, 4, weight_a[6]), (2, 3, weight_a[7]), (2, 4, weight_a[8]),
         (3, 4, weight_a[9])])  # 添加边的权值

    pos = [(1.5, 0.5), (3.5, 0.5), (0.5, 2), (4.5, 2), (2.5, 3)]  # 元组中的两个数字是第i（从0开始计数）个点的坐标
    text_pos = []
    for i in range(0, 5):
        for k in range(i + 1, 5):
            text_pos.append([(pos[i][0] + pos[k][0]) / 2, (pos[i][1] + pos[k][1]) / 2])
    for weight in range(0, 10):
        if weight_a[weight] != 0:
            plt.text(text_pos[weight][0], text_pos[weight][1] - 0.05, weight_a[weight], color='w', ha='center',
                     wrap=True,
                     fontsize=12, bbox=dict(facecolor="r", alpha=0.5))
    # nx.draw(G, pos, with_labels=True, node_color='white', edge_color='black', alpha=0.2, width=10)  # 按参数构图
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    for i in range(0, 10):
        nx.draw_networkx_edges(G, pos, edgelist=[elarge[i]], width=weight_a[i], alpha=0.2)
    plt.xlim(0, 5)  # 设置首界面X轴坐标范围
    plt.ylim(0, 3.5)  # 设置首界面Y轴坐标范围

    image_i = 0
    for p in pos:
        ax2 = fig.add_axes([0.05 + p[0] * 0.8 / 5, 0.05 + 0.45 + p[1] * 0.4 / 3.5, 0.1, 0.1])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image1 = io.imread(image[image_i])
        io.imshow(image1)
        image_i += 1
        ax1.set_title('[ '+team_name[1][0]+' 最佳组合 ]---(' + best_group[0] + '&' + best_group[1] + ')携手击杀' + str(max(group_weight)) + '人',color='r')

    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\5.png')
    # plt.show()  # 显示图像
