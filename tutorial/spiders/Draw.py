# encoding=utf-8
import matplotlib.pyplot as plt
import plotly
from pylab import *  # 支持中文
import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import numpy as np


def Draw(eco, dragon, first_kill_info, team_name, towerevent):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    ecol = []
    for i in range(0, len(eco)):
        ecol.append(i)

    # plt.plot(x, y, 'ro-')
    # plt.plot(x, y1, 'bo-')
    # pl.xlim(-1, 11)  # 限定横轴的范围
    # pl.ylim(-1, 110)  # 限定纵轴的范围
    fig = plt.figure(figsize=(6, 3))
    ax = fig.add_subplot(111)
    ar_eco = np.array(eco)
    ar_ecol = np.array(ecol)
    for i in range(0, len(eco) - 1):
        te = eco[i]
        if eco[i] + eco[i + 1] > 0:

            plt.scatter(i, te, c='b', s=15)
            plt.plot((i, i + 1), (eco[i], eco[i + 1]), c='b')
        else:
            plt.scatter(i, te, c='r', s=15)
            plt.plot((i, i + 1), (eco[i], eco[i + 1]), c='r')

    # plt.plot(x, y1, marker='*', ms=10, label=u'y=x^3曲线图')
    # ax.legend('11111', '2222')  # 让图例生效
    # plt.xticks(x, names, rotation=45)
    # plt.margins(0)
    # plt.subplots_adjust(bottom=0.15)
    # ax.set_xlabel('时间',horizontalalignment='right')
    ax.set_ylabel('经济差')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    ax.grid(True)  # 网格
    team_blue = team_name[0][0]
    team_red = team_name[1][0]
    plt.title(team_blue + ' VS ' + team_red + ' 比赛走势\n\n')
    plt.tight_layout()
    fig.set_size_inches(6, 4)
    # plt.title("A simple plot")  # 标题
    abs_eco = map(abs, eco)
    max_eco = max(abs_eco)
    plt.text(len(ecol) / 2, min(eco) - max_eco / 8, '时间', ha='center', wrap=True)
    plt.text(0, min(eco) - max_eco / 8, '-- ' + team_red + '领先', ha='left', color='r', size=10, wrap=True)
    plt.text(len(eco) / 5, min(eco) - max_eco / 8, '-- ' + team_blue + '领先', ha='left', color='b', size=10, wrap=True)

    for event in dragon:
        print(dragon[event])
        time = event // 60
        if dragon[event][0] == 0 or dragon[event][0] == 'BARON_NASHOR':
            if dragon[event][1] == 200:
                ax.annotate('大龙', color='r', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] - max_eco / 6),
                            arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            else:
                ax.annotate('大龙', color='b', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] + max_eco / 6),
                            arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
        elif dragon[event][0] == 5 or dragon[event][0] == 'ELDER_DRAGON':
            if dragon[event][1] == 200:
                ax.annotate('远古巨龙', color='r', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] - max_eco / 5),
                            arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            else:
                ax.annotate('远古巨龙', color='b', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] + max_eco / 5),
                            arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
        elif dragon[event][0] == 'RIFTHERALD':
            if dragon[event][1] == 200:
                ax.annotate('峡谷先锋', color='r', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] - max_eco / 5),
                            arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            else:
                ax.annotate('峡谷先锋', color='b', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] + max_eco / 5),
                            arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
        else:
            if dragon[event][1] == 200:
                ax.annotate('小龙', color='r', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] - max_eco / 6),
                            arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            else:
                ax.annotate('小龙', color='b', horizontalalignment='center', xy=(time, eco[round(time)]),
                            xytext=(time, eco[round(time)] + max_eco / 6),
                            arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
                # plt.text(time, eco[round(time)], '大龙', size=15)
                # p1.text(tx, ty, label_f1, fontsize=15, verticalalignment="top", horizontalalignment="right")
    # plt.xlabel('时间',verticalalignment='bottom')
    kill_time = int(first_kill_info[0] // 60)
    if first_kill_info[1] == 200:
        ax.annotate('一血', color='r', horizontalalignment='center', xy=(kill_time, eco[kill_time]),
                    xytext=(kill_time, eco[kill_time] - (max_eco / 8)),
                    arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
    else:
        ax.annotate('一血', color='b', horizontalalignment='center', xy=(kill_time, eco[kill_time]),
                    xytext=(kill_time, eco[kill_time] + max_eco / 8),
                    arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
    # tower_time = towerevent[0]['game_time'] // 60
    # if 'T1' in towerevent[0]['tower_name']:
    #     ax.annotate('一塔', color='r', horizontalalignment='center', xy=(tower_time, eco[tower_time]),
    #                 xytext=(tower_time, eco[tower_time] - (max_eco / 8)),
    #                 arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
    # else:
    #     ax.annotate('一塔', color='b', horizontalalignment='center', xy=(tower_time, eco[tower_time]),
    #                 xytext=(tower_time, eco[tower_time] + max_eco / 8),
    #                 arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
    # blue_Tower='Turret_T1_C_03_A Turret_T1_C_07_A Turret_T1_C_06_A'
    # red_Tower = 'Turret_T2_C_03_A Turret_T2_C_07_A Turret_T2_C_06_A'
    # for event in towerevent:
    #     if towerevent[event]['tower_name'] in blue_Tower:
    #         tower_base_time = towerevent[event]['game_time'] // 60
    #         ax.annotate('上高地', color='r', horizontalalignment='center', xy=(tower_base_time, eco[tower_base_time]),
    #                     xytext=(tower_base_time, eco[tower_base_time] - (max_eco / 8)),
    #                     arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
    #         break
    # for event in towerevent:
    #     if towerevent[event]['tower_name'] in red_Tower:
    #         tower_base_time =  towerevent[event]['game_time'] // 60
    #         ax.annotate('上高地', color='b', horizontalalignment='center', xy=(tower_base_time, eco[tower_base_time]),
    #                     xytext=(tower_base_time, eco[tower_base_time] + max_eco / 8),
    #                     arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
    #         break

    tower_time = int(towerevent[0]['timestamp'] // 60000)
    if towerevent[0]['killerId'] > 5:
        ax.annotate('一塔', color='r', horizontalalignment='center', xy=(tower_time, eco[tower_time]),
                    xytext=(tower_time, eco[tower_time] - (max_eco / 8)),
                    arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
    else:
        ax.annotate('一塔', color='b', horizontalalignment='center', xy=(tower_time, eco[tower_time]),
                    xytext=(tower_time, eco[tower_time] + max_eco / 8),
                    arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
    blue_Tower = 'Turret_T1_C_03_A Turret_T1_C_07_A Turret_T1_C_06_A'
    red_Tower = 'Turret_T2_C_03_A Turret_T2_C_07_A Turret_T2_C_06_A'
    for event in towerevent:
        if event['towerType'] == 'BASE_TURRET' and event['killerId'] > 5:
            tower_base_time = int(event['timestamp'] // 60000)
            ax.annotate('上高地', color='r', horizontalalignment='center', xy=(tower_base_time, eco[tower_base_time]),
                        xytext=(tower_base_time, eco[tower_base_time] - (max_eco / 5)),
                        arrowprops=dict(facecolor='red', shrink=0.03, headlength=5, headwidth=5, width=2))
            break
    for event in towerevent:
        if event['towerType'] == 'BASE_TURRET' and 0 < event['killerId'] < 6:
            tower_base_time = int(event['timestamp'] // 60000)
            ax.annotate('上高地', color='b', horizontalalignment='center', xy=(tower_base_time, eco[tower_base_time]),
                        xytext=(tower_base_time, eco[tower_base_time] + max_eco / 5),
                        arrowprops=dict(facecolor='blue', shrink=0.03, headlength=5, headwidth=5, width=2))
            break
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\1.png')
    # plt.show()
