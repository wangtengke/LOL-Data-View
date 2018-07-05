import matplotlib.pyplot as plt
from pylab import *  # 支持中文
from skimage import io
def BP_List(pick_list,ban_list,team_name):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()
    fig.set_size_inches(5, 7)
    left, bottom, width, height = 0, 0 , 1, 1
    ax1 = fig.add_axes([left, bottom, width, height])
    # ax2.plot([0,1], [0,1], '--k')
    # ax1.spines['right'].set_color('none')
    # ax1.spines['top'].set_color('none')
    # ax1.spines['left'].set_color('none')
    # ax1.spines['bottom'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.text(0.25,0.92,'  [  '+team_name[0][0]+'  ]'+'\nBan      Pick',ha='center', color='b', size=15, wrap=True)
    ax1.text(0.74,0.92,'  [  '+team_name[1][0]+'  ]'+'\nPick  '
                                                     '    Ban',ha='center', color='r', size=15, wrap=True)
    # 蓝色方第一轮ban
    for i in [0,2,4]:
        left, bottom, width, height = 0.1, 0.85-0.03*i, 0.08,0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        # ax2.plot([0,1], [0,1], '--k')
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(ban_list[0][i]['hero_image'])
        io.imshow(image)
        ax2.plot([0, 110], [0, 110], '-b',linewidth='3')
        # ax2.set_title('第一轮Ban',c='b')
    # 红色方第一轮ban
    for i in [1, 3, 5]:
        left, bottom, width, height = 0.8, 0.85 - 0.03 * (i-1), 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(ban_list[0][i]['hero_image'])
        io.imshow(image)
        ax2.plot([0, 110], [0, 110], '-r', linewidth='3')
     # 蓝色方第一轮pick
    for i in [0, 3, 4]:
        left, bottom, width, height = 0.3, 0.67 - 0.06 * i, 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(pick_list[0][i]['hero_image'])
        io.imshow(image)
    #红色方一轮pick
    for i in [1, 2, 5]:
        left, bottom, width, height = 0.6, 0.67 - 0.06 * i, 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(pick_list[0][i]['hero_image'])
        io.imshow(image)
    # 蓝色方第二轮ban
    for i in [7, 9]:
        left, bottom, width, height = 0.1, 0.48 - 0.03 * (i-1), 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(ban_list[0][i]['hero_image'])
        io.imshow(image)
        ax2.plot([0, 110], [0, 110], '-b', linewidth='3')
    # 红色方第二轮ban
    for i in [6, 8]:
        left, bottom, width, height = 0.8, 0.48 - 0.03 * (i), 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(ban_list[0][i]['hero_image'])
        io.imshow(image)
        ax2.plot([0, 110], [0, 110], '-r', linewidth='3')
    # 蓝色方第二轮pick
    for i in [7,8]:
        left, bottom, width, height = 0.3, 0.54 - 0.06 * i, 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(pick_list[0][i]['hero_image'])
        io.imshow(image)
    # 红色方第二轮pick
    for i in [6,9]:
        left, bottom, width, height = 0.6, 0.54 - 0.06 * i, 0.08, 0.08
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.spines['left'].set_color('none')
        ax2.spines['bottom'].set_color('none')
        ax2.set_xticks([])
        ax2.set_yticks([])
        image = io.imread(pick_list[0][i]['hero_image'])
        io.imshow(image)
        plt.savefig('C:\\Users\\USER\\Desktop\\战报绘图\\0.png')
    # plt.show()