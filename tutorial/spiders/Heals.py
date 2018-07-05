import matplotlib.pyplot as plt
import numpy as np


# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_y()
        plt.text(rect.get_width() , height, rect.get_width(), ha='right', va='bottom',fontsize=9)
        # rect.set_edgecolor('black')
def Heals(Healed,player_pair_a,player_pair_b,team_nameLOL):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # data = np.random.randint(10, 100, size=10)
    champion_name=[]
    Healed1=Healed.copy()
    player_name=[]
    for i in range(5):

        player_name.append('('+player_pair_a[i][3]+')'+player_pair_a[i][2])
    for i in range(5):

        player_name.append('(' + player_pair_b[i][3] + ')' + player_pair_b[i][2])
    # pyexcel_xls 以 OrderedDict 结构处理数据
    n_groups = 10
    index1 = np.arange(n_groups)
    for i in range(9):
        for k in range(i+1,10):
            if Healed[i]> Healed[k]:
                Healed[i],Healed[k] = Healed[k],Healed[i]
                player_name[i], player_name[k] = player_name[k], player_name[i]
                index1[i], index1[k] = index1[k], index1[i]
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.8
    opacity = 0.4

    rects1 = plt.barh(index, Healed, bar_width / 2, alpha=opacity, color='b', label='回复量')

    # rects3 = plt.bar(index + bar_width, means_VotexF36, bar_width / 2, alpha=opacity, color='c', label='VotexF36')
    # rects4 = plt.bar(index + 1.5 * bar_width, means_VotexF50, bar_width / 2, alpha=opacity, color='m', label='VotexF50')
    # gold_blue=sum(gold1_15[0:5])
    # gold_red=sum(gold1_15[5:10])
    # if sum(gold1_15[0:5])>sum(gold1_15[5:10]):
    #     plt.xlabel('对线期 '+team_nameLOL[0][0]+' 领先 '+team_nameLOL[1][0]+' '+str( sum(gold1_15[0:5])-sum(gold1_15[5:10]))+' 块',color='red')
    # else:
    #     plt.xlabel('对线期 ' + team_nameLOL[1][0] + ' 领先 ' + team_nameLOL[0][0] + str(
    #         sum(gold1_15[5:10]) - sum(gold1_15[0:5])) + ' 块',color='red')
    # plt.ylabel('Scores')
    plt.title('英雄血量回复值')

    # plt.xticks(index - 0.2+ 2*bar_width, ('balde', 'bunny', 'dragon', 'happy', 'pillow'))

    plt.yticks(index - 1.4 + 2 * bar_width, player_name, fontsize=10)


    plt.xticks(fontsize=12)  # change the num axis size
    add_labels(rects1)
    # plt.ylim(0, 1.5)  # The ceil
    plt.legend()
    plt.tight_layout()
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\10.png')
    # plt.show()