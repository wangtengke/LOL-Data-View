import matplotlib.pyplot as plt
from pylab import *  # 支持中文
def Dam_Rate(player_a_player,player_b_player,team_name):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()
    fig.set_size_inches(6, 10)
    player_a_dam=[]
    player_b_dam=[]
    player_a_name=[]
    player_b_name=[]
    player_a_assis = []
    player_b_assis = []
    player_a_death = []
    player_b_death = []
    player_a_kill  = []
    player_b_kill  = []
    labels = []
    player_info_a=[]
    player_info_b = []
    for player_a in player_a_player[0]:
        player_a_dam.append(player_a['hero_damage'])
        player_a_name.append(player_a['hero_name'])
        player_a_kill.append(player_a['kill_num'])
        player_a_death.append(player_a['dead_num'])
        player_a_assis.append(player_a['assis_num'])
    for i in range(0,5):
        player_info_a.append(player_a_name[i]+'\n('+str(player_a_kill[i])+'-'+str(player_a_death[i])+'-'+str(player_a_assis[i])+')\n伤害'+str(player_a_dam[i]))

    labels = 'a', 'b', 'c', 'd','e'
    colors = 'lightgreen', 'gold', 'lightskyblue', 'lightcoral','yellowgreen'
    explode = 0, 0, 0, 0,0
    plt.subplot(211)
    plt.pie(player_a_dam, explode=explode, labels=player_info_a,
            colors=colors, autopct='%1.1f%%', startangle=50)
    plt.axis('equal')
    plt.title('[ '+team_name[0][0]+' ] 伤害占比\n\n',color='blue')

    for player_b in player_b_player[0]:
        player_b_dam.append(player_b['hero_damage'])
        player_b_name.append(player_b['hero_name'])
        player_b_kill.append(player_b['kill_num'])
        player_b_death.append(player_b['dead_num'])
        player_b_assis.append(player_b['assis_num'])
    for i in range(0, 5):
        player_info_b.append(player_b_name[i] + '\n(' + str(player_b_kill[i]) + '-' + str(player_b_death[i]) + '-' + str(player_b_assis[i]) + ')\n伤害' + str(player_b_dam[i]))

    labels = 'a', 'b', 'c', 'd', 'e'
    colors = 'lightgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellowgreen'
    explode = 0, 0, 0, 0, 0
    plt.subplot(212)
    plt.pie(player_b_dam, explode=explode, labels=player_info_b,
            colors=colors, autopct='%1.1f%%', startangle=50)
    plt.axis('equal')
    plt.title('\n\n\n\n\n\n\n[ '+team_name[1][0]+' ] 伤害占比\n\n',color='red')
    plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\4.png')
    # plt.show()
    print('11')