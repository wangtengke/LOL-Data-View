import scrapy
import json
import matplotlib
import jsonpath

from tutorial.spiders.First_WardsPlaced import First_WardsPlaced
from tutorial.spiders.Heals import Heals
from tutorial.spiders.Items_Esport import Items_Esport
from tutorial.spiders.BP_List import BP_List
from tutorial.spiders.Best_Partner import Best_Partner
from tutorial.spiders.Dam_Rate import Dam_Rate
from tutorial.spiders.Dam_Rate_Esport import Dam_Rate_Esport
from tutorial.spiders.Draw import Draw
from tutorial.spiders.Dam_Eco import Dam_Eco
from tutorial.spiders.Eco_xp15 import Eco_xp15
from tutorial.spiders.Items import Items
from tutorial.spiders.Pos_Jungle import Pos_Jungle
from tutorial.spiders.Pos_Jungle_Esport import Pos_Jungle_Esport
from tutorial.spiders.Team_Battle import Team_Battle
from tutorial.spiders.wardsPlaced import wardsPlaced
from tutorial.spiders.Draw_LPL import Draw_LPL


class TestSpider(scrapy.Spider):  # QuotesSpider类必须要继承scrapy.Spider类，你可以在这个类里面定义一些方法和属性。
    name = "test"  # name属性，用来区分爬虫，在一个项目中，你不能用同样的名称来命名不同的爬虫。
    player_pair_a = []
    player_pair_b = []
    num = False
    a_hotpoint = []
    b_hotpoint = []
    player_team_a_id = 0
    towerevent = {}
    team_nameLOL = [['1'], ['1']]
    champion = []
    game_time = 0
    kill_a = []
    kill_b = []
    win_team = []
    items_id=[]
    def start_requests(self):  # 必须返回一个可迭代的对象，或者写一个生成器。你的爬虫将会从这个类开始抓取。
        urls = [  # 初始url，这里不解释了，这两个网站是给你做练习用的，原来中文教程的DMOZ挂了。
            # 'http://img1.famulei.com/lol/livedata/46517911528025548.json',
            # 'http://img1.famulei.com/lol/livedata/2/46517911528025548.json'
            # 'http://img1.famulei.com/lol/livedata/46416301527751701.json',
            # 'http://img1.famulei.com/lol/livedata/2/46416301527751701.json'
            # 'http://img1.famulei.com/match/result/9112.json'
            'https://ddragon.leagueoflegends.com/cdn/8.11.1/data/en_US/champion.json',
            'https://acs.leagueoflegends.com/v1/stats/game/ESPORTSTMNT06/730459?gameHash=31f6dddb599ae13f',
            'https://acs.leagueoflegends.com/v1/stats/game/ESPORTSTMNT06/730459/timeline?gameHash=31f6dddb599ae13f'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # parse方法用来处理request返回的结果。关于这一部分的一些内容，我在后面详细介绍。
        # T = TestSpider()
        if 'livedata/2/' in response.url:
            # T = TestSpider()
            text = response.text
            data = json.loads(text)
            eco = data['data']['eco_list']
            first_kill_time = data['data']['kill_pos'][0]['game_time']
            kill_team = data['data']['kill_pos'][0]['groupId']
            first_kill_info = [first_kill_time, kill_team]
            dragon_type = jsonpath.jsonpath(data, "$..dragon_event[*].dragon_type")
            dragon_team = jsonpath.jsonpath(data, "$..dragon_event[*].groupId")
            dragon_test = []
            for i in range(0, len(dragon_type)):
                dragon_test.append([dragon_type[i], dragon_team[i]])
            dragon_time = jsonpath.jsonpath(data, "$..dragon_event[*].game_time")
            dragon = dict(zip(dragon_time, dragon_test))

            team_id = [jsonpath.jsonpath(data, "$.data.team_a.clan_id"),
                       jsonpath.jsonpath(data, "$.data.team_b.clan_id")]
            team_game_id = [jsonpath.jsonpath(data, "$.data.game.blue_clan_id"),
                            jsonpath.jsonpath(data, "$.data.game.red_clan_id")]
            if team_id[0] == team_game_id[0]:
                team_name = [jsonpath.jsonpath(data, "$.data.team_a.team_short_name_a"),
                             jsonpath.jsonpath(data, "$.data.team_b.team_short_name_b")]
            else:
                team_name = [jsonpath.jsonpath(data, "$.data.team_b.team_short_name_b"),
                             jsonpath.jsonpath(data, "$.data.team_a.team_short_name_a")]
            while (self.towerevent == {}):
                print('not')
                pass
            Draw_LPL(eco, dragon, first_kill_info, team_name, self.towerevent)  # 经济曲线

            #########################################################################################
            # 第二幅图 伤害经济比
            player_name = []
            player_heroname = []
            player_name.append(jsonpath.jsonpath(data, "$.data.team_a.players[*].player_name"))
            player_name.append(jsonpath.jsonpath(data, "$.data.team_b.players[*].player_name"))
            player_heroname.append(jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_name"))
            player_heroname.append(jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_name"))
            player_info_a = dict(zip(player_name[0], player_heroname[0]))
            player_info_b = dict(zip(player_name[1], player_heroname[1]))
            # player_b_team = jsonpath.jsonpath(data, "$.data.team_b)
            player_a_img = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_image")
            player_b_img = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_image")
            player_a_eco = jsonpath.jsonpath(data, "$.data.team_a.players[*].economics")
            player_b_eco = jsonpath.jsonpath(data, "$.data.team_b.players[*].economics")
            player_a_dam = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_damage")
            player_b_dam = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_damage")
            player_a_hero = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_name")
            player_b_hero = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_name")
            player_test_a = []
            player_test_b = []
            for i in range(0, len(player_a_eco)):
                player_test_a.append([player_a_eco[i], player_a_dam[i], player_a_img[i]])
            for i in range(0, len(player_b_eco)):
                player_test_b.append([player_b_eco[i], player_b_dam[i], player_b_img[i]])
            player_a = dict(zip(player_a_hero, player_test_a))
            player_b = dict(zip(player_b_hero, player_test_b))

            Dam_Eco(player_a, player_b, player_info_a, player_info_b)  # 经济伤害图

            ##########################################################################################
            # 第三幅 打野走位图
            # Pos_Jungle()

            ##########################################################################################
            # 第四幅  伤害占比图
            if team_id[0] == team_game_id[0]:
                player_a_player = jsonpath.jsonpath(data, "$.data.team_a.players")
                player_b_player = jsonpath.jsonpath(data, "$.data.team_b.players")
            else:
                player_b_player = jsonpath.jsonpath(data, "$.data.team_a.players")
                player_a_player = jsonpath.jsonpath(data, "$.data.team_b.players")
            Dam_Rate(player_a_player, player_b_player, team_name)  # 伤害占比图
            ##########################################################################################
            # 第五幅 最佳组合

            num = 0
            assisnt = []  # 每次助攻击杀id列表
            # player_pair_a = []  # team_a照片和id对应
            # player_pair_b = []  # team_b照片和id对应
            player_hero_id_assis = jsonpath.jsonpath(data, "$.data.kill_pos[*].assistant_id_list")
            player_hero_id_killer = jsonpath.jsonpath(data, "$.data.kill_pos[*].killer_id")
            player_hero_id_a = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_id")
            player_hero_image_a = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_image")
            player_hero_name_a = jsonpath.jsonpath(data, "$.data.team_a.players[*].hero_name")
            player_hero_id_b = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_id")
            player_hero_image_b = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_image")
            player_hero_name_b = jsonpath.jsonpath(data, "$.data.team_b.players[*].hero_name")
            self.player_team_a_id = jsonpath.jsonpath(data, "$.data.team_a.groupId")
            for i in range(len(player_hero_id_a)):
                self.player_pair_a.append([player_hero_id_a[i], player_hero_image_a[i], player_hero_name_a[i]])
            for i in range(len(player_hero_id_b)):
                self.player_pair_b.append([player_hero_id_b[i], player_hero_image_b[i], player_hero_name_b[i]])
            for row in range(len(player_hero_id_assis)):
                assisnt.append([])
            for assis in player_hero_id_assis:
                for hero_id in assis:
                    assisnt[num].append(hero_id['hero_id'])
                assisnt[num].append(player_hero_id_killer[num])
                num += 1
            if team_id[0] == team_game_id[0]:
                pass
            else:
                temp = self.player_pair_a
                self.player_pair_a = self.player_pair_b
                self.player_pair_b = temp
            Best_Partner(assisnt, self.player_pair_a, self.player_pair_b, team_name)  # 最佳组合
            player_a_Jungle_id = self.player_pair_a[1][0]
            player_b_Jungle_id = self.player_pair_b[1][0]
            urls = [  # 初始url，这里不解释了，这两个网站是给你做练习用的，原来中文教程的DMOZ挂了。
                'http://img1.famulei.com/lol/livedata/hp/2849-' + str(player_a_Jungle_id) + '.json',
                'http://img1.famulei.com/lol/livedata/hp/2849-' + str(player_b_Jungle_id) + '.json'
            ]
            for url in urls:
                yield scrapy.Request(url, self.parse)
            ##########################################################################################
            # 第六幅图 精彩团战
            game_team_battle = jsonpath.jsonpath(data, "$.data.team_battle[*]")
            best_battle = game_team_battle[len(game_team_battle) - 1]
            # Team_Battle(best_battle,player_a_player,player_b_player)

            ##########################################################################################
            # 第七幅图 一级视野
            eye_pos = jsonpath.jsonpath(data, "$.data.eye_pos[*]")
            First_WardsPlaced(eye_pos)
            # player_hero_id=[player_hero_id_a,player_hero_id_b]
            ##########################################################################################
            # 数据介绍
            game_time_txt = jsonpath.jsonpath(data, "$.data.game.game_time_txt")
            number_txt = jsonpath.jsonpath(data, "$.data.game.number_txt")
            if team_id[0] == team_game_id[0]:
                kill_a = jsonpath.jsonpath(data, "$.data.team_a.kills")
                kill_b = jsonpath.jsonpath(data, "$.data.team_b.kills")
            else:
                kill_b = jsonpath.jsonpath(data, "$.data.team_a.kills")
                kill_a = jsonpath.jsonpath(data, "$.data.team_b.kills")
            blue_id = jsonpath.jsonpath(data, "$.data.game.blue_clan_id")
            red_id = jsonpath.jsonpath(data, "$.data.game.red_clan_id")
            win_id = jsonpath.jsonpath(data, "$.data.game.win_clan_id")
            blue_name = team_name[0]
            red_name = team_name[1]
            win_team = ''
            if win_id == blue_id:
                win_team = blue_name
            else:
                win_team = red_name
            f = open('C:\\Users\\USER\\Desktop\\战报绘图\\战报介绍.txt', 'w')

            f.write('#英雄联盟# #LPL# #2018LPL#\n[ 数据快报 ]：' + blue_name[0] + ' VS ' + red_name[0] + ',' + number_txt[
                0] + '比赛耗时' +
                    game_time_txt[0] + ',人头比' + str(kill_a[0]) + ':' + str(kill_b[0]) + ',' + win_team[
                        0] + '获得比赛胜利。\n(ps.战报持续更新中,觉得不错就点个赞and关注吧！欢迎对战报内容提意见！)')
            f.close()

        elif 'hp/' in response.url:
            text = response.text
            url = response.url
            data = json.loads(text)
            player_a_Jungle = self.player_pair_a[1]
            player_b_Jungle = self.player_pair_b[1]
            ##########################################################################################
            # # 第七幅图 打野走位
            if '-' + str(player_a_Jungle[0]) + '.json' in url:
                # if self.player_team_a_id[0] == 200:
                self.a_hotpoint = jsonpath.jsonpath(data, "$.data.hot_point[*]")
                if self.num == True:
                    Pos_Jungle(player_a_Jungle, player_b_Jungle, self.a_hotpoint, self.b_hotpoint)
                self.num = True
                # else:
                #     self.b_hotpoint = jsonpath.jsonpath(data, "$.data.hot_point[*]")
                #     if self.num == True:
                #         Pos_Jungle(player_b_Jungle, player_a_Jungle, self.a_hotpoint, self.b_hotpoint)
                #     self.num = True

            else:
                # if self.player_team_a_id[0] == 200:
                self.b_hotpoint = jsonpath.jsonpath(data, "$.data.hot_point[*]")
                if self.num == True:
                    Pos_Jungle(player_a_Jungle, player_b_Jungle, self.a_hotpoint, self.b_hotpoint)
                self.num = True
                # else:
                #     self.a_hotpoint = jsonpath.jsonpath(data, "$.data.hot_point[*]")
                #     if self.num == True:
                #         Pos_Jungle(player_b_Jungle, player_a_Jungle, self.a_hotpoint, self.b_hotpoint)
                #     self.num = True

        elif 'match/result' in response.url:
            text = response.text
            data = json.loads(text)
            Item_Build = jsonpath.jsonpath(data, "$.item_builds")
            game_time = jsonpath.jsonpath(data, "$.result_list.game_time_m")
            game_team = jsonpath.jsonpath(data, "$.teams")
            team_nam = [jsonpath.jsonpath(data, "$.result_list.blue_name"),
                        jsonpath.jsonpath(data, "$.result_list.red_name")]

            Items(Item_Build, game_time, game_team, team_nam)  # 出装图
            print("11")
        elif '/timeline' in response.url:
            text = response.text
            data = json.loads(text)
            gold = jsonpath.jsonpath(data, "$.frames[*].participantFrames[*].totalGold")
            self.game_time = len(jsonpath.jsonpath(data, "$.frames[*]"))
            gold_list = []
            event_dragon = []
            dragon_test = []
            dragon_time = []
            event_kill = []
            event_building = []
            event_items = []
            event_wardplaced=[]
            for i in range(0, len(gold), 10):
                gold_list.append(
                    gold[i] + gold[i + 1] + gold[i + 2] + gold[i + 3] + gold[i + 4] - gold[i + 5] - gold[i + 6] - gold[
                        i + 7] - gold[i + 8] - gold[i + 9])
            event = jsonpath.jsonpath(data, "$.frames[*].events[*]")
            for event_temp in event:
                if event_temp['type'] == 'ELITE_MONSTER_KILL':
                    event_dragon.append(event_temp)
                elif event_temp['type'] == 'CHAMPION_KILL':
                    event_kill.append(event_temp)
                elif event_temp['type'] == 'BUILDING_KILL':
                    event_building.append(event_temp)
                elif event_temp['type'] == 'ITEM_PURCHASED':
                    event_items.append(event_temp)
                elif event_temp['type'] == 'WARD_PLACED':
                    event_wardplaced.append(event_temp)
            for i in range(0, len(event_dragon)):
                if event_dragon[i]['killerId'] > 5:
                    kill_team = 200
                else:
                    kill_team = 100
                if len(event_dragon[i]) == 6:
                    dragon_test.append([event_dragon[i]['monsterSubType'], kill_team])
                else:
                    dragon_test.append([event_dragon[i]['monsterType'], kill_team])
                dragon_time.append(event_dragon[i]['timestamp'] / 1000)
            dragon = dict(zip(dragon_time, dragon_test))
            first_kill_time = event_kill[0]['timestamp'] / 1000
            if event_kill[0]['killerId'] < 6:
                kill_team = 100
            else:
                kill_team = 200
            first_kill_info = [first_kill_time, kill_team]
            while (self.team_nameLOL == []):
                pass

            print("1")
            Draw(gold_list, dragon, first_kill_info, self.team_nameLOL, event_building)  # 经济曲线
            #########################################################################################
            # 最佳组合
            assisnt = []
            for i in range(len(event_kill)):
                assisnt.append(event_kill[i]['assistingParticipantIds'])
            for i in range(len(event_kill)):
                assisnt[i].append(event_kill[i]['killerId'])
            Best_Partner(assisnt, self.player_pair_a, self.player_pair_b, self.team_nameLOL)  # 最佳组合

            #########################################################################################
            # 15分钟经济/经验
            gold_15 = jsonpath.jsonpath(data, "$.frames[15].participantFrames[*].totalGold")
            xp_15 = jsonpath.jsonpath(data, "$.frames[15].participantFrames[*].xp")
            Eco_xp15(gold_15, xp_15, self.player_pair_a, self.player_pair_b,self.team_nameLOL)

            #########################################################################################
            # 出装线路

            Items_Esport(event_items, self.game_time, self.player_pair_a, self.player_pair_b, self.team_nameLOL)
            #########################################################################################
            # 打野走位图
            player_a_Jungle = self.player_pair_a[1]
            player_b_Jungle = self.player_pair_b[1]
            hotpos_a=jsonpath.jsonpath(data,"$.frames[*].participantFrames[2].position")
            hotpos_b=jsonpath.jsonpath(data,"$.frames[*].participantFrames[7].position")
            Pos_Jungle_Esport(player_a_Jungle, player_b_Jungle,hotpos_a,hotpos_b)
            #########################################################################################
            # 一级视野
            # First_WardsPlaced(event_wardplaced[0:10])
            #########################################################################################
            # 战报
            f = open('C:\\Users\\USER\\Desktop\\战报绘图\\战报介绍.txt', 'w')

            f.write(
                '#英雄联盟# #2018LCK# #LCK# @英雄联盟赛事\n[ 数据快报 ]：' + self.team_nameLOL[0][0] + ' VS ' + self.team_nameLOL[1][
                    0] + ',' + 'BO3第一场' + '比赛耗时' +
                str(self.game_time) + '分钟,人头比' + str(self.kill_a) + ':' + str(
                    self.kill_b) + ',' + self.win_team + '获得比赛胜利。\n(ps.觉得不错就点个赞and关注吧！战报持续更新中，欢迎对战报内容提意见！)')
            f.close()
            #########################################################################################
            # 第二幅图 伤害经济比
        elif ('ESPORTSTMNT06/' in response.url) & ('/timeline' not in response.url):
            text = response.text
            data = json.loads(text)
            player_name = jsonpath.jsonpath(data, "$.participantIdentities[*].player.summonerName")
            self.team_nameLOL[0][0] = player_name[0].split(' ')[0]
            self.team_nameLOL[1][0] = player_name[5].split(' ')[0]

            #########################################################################################
            # 第二幅图 伤害经济比
            while self.champion == []:
                pass
            player_name = []
            player_heroname = []
            player_id = []
            player_a_img = []
            player_b_img = []
            player_name.append(jsonpath.jsonpath(data, "$.participantIdentities[0:5].player.summonerName"))
            player_name.append(jsonpath.jsonpath(data, "$.participantIdentities[5:10].player.summonerName"))
            player_id.append(jsonpath.jsonpath(data, "$.participants[*].championId"))
            # player_id.append(jsonpath.jsonpath(data, "$.participants[5:10].championId"))
            for i in range(10):
                for k in self.champion:
                    if int(k[0]) == player_id[0][i]:
                        player_heroname.append(k[1])
            # for i in range(5):
            #     player_heroname.append(self.champion[i][1])
            # for i in range(5,10):
            #     player_heroname.append(self.champion[i][1])
            player_info_a = dict(zip(player_name[0], player_heroname[0:5]))
            player_info_b = dict(zip(player_name[1], player_heroname[5:10]))
            # player_b_team = jsonpath.jsonpath(data, "$.data.team_b)
            for i in range(5):
                player_a_img.append(
                    'https://ddragon.leagueoflegends.com/cdn/8.11.1/img/champion/' + player_heroname[i] + '.png')
            for i in range(5, 10):
                player_b_img.append(
                    'https://ddragon.leagueoflegends.com/cdn/8.11.1/img/champion/' + player_heroname[i] + '.png')
            player_a_eco = jsonpath.jsonpath(data, "$.participants[0:5].stats.goldEarned")
            player_b_eco = jsonpath.jsonpath(data, "$.participants[5:10].stats.goldEarned")
            player_a_dam = jsonpath.jsonpath(data, "$.participants[0:5].stats.totalDamageDealtToChampions")
            player_b_dam = jsonpath.jsonpath(data, "$.participants[5:10].stats.totalDamageDealtToChampions")
            player_a_hero = player_heroname[0:5]
            player_b_hero = player_heroname[5:10]
            player_test_a = []
            player_test_b = []
            for i in range(0, len(player_a_eco)):
                player_test_a.append([player_a_eco[i], player_a_dam[i], player_a_img[i]])
            for i in range(0, len(player_b_eco)):
                player_test_b.append([player_b_eco[i], player_b_dam[i], player_b_img[i]])
            player_a = dict(zip(player_a_hero, player_test_a))
            player_b = dict(zip(player_b_hero, player_test_b))

            Dam_Eco(player_a, player_b, player_info_a, player_info_b)  # 经济伤害图
            for i in range(5):
                self.player_pair_a.append([i + 1, player_a_img[i], player_a_hero[i], player_name[0][i]])
                self.player_pair_b.append([i + 6, player_b_img[i], player_b_hero[i], player_name[1][i]])
            ##########################################################################################
            # 第四幅  伤害占比图

            player_a_player = jsonpath.jsonpath(data, "$.participants[0:5]")
            player_b_player = jsonpath.jsonpath(data, "$..participants[5:10]")

            Dam_Rate_Esport(player_a_player, player_b_player, self.team_nameLOL, player_a_hero, player_b_hero)  # 伤害占比图
            print('1')
            ##########################################################################################
            # 放眼数图
            wardsPlaced_num = jsonpath.jsonpath(data, "$.participants[*].stats.wardsPlaced")
            wardsKilled_num = jsonpath.jsonpath(data, "$.participants[*].stats.wardsKilled")
            wardsPlaced(wardsPlaced_num,wardsKilled_num,self.player_pair_a,self.player_pair_b,self.team_nameLOL)

            ##########################################################################################
            # 治疗量图
            Healed = jsonpath.jsonpath(data, "$.participants[*].stats.totalHeal")
            Heals(Healed,self.player_pair_a,self.player_pair_b,self.team_nameLOL)
            ##########################################################################################
            # 数据介绍
            # while self.game_time==0:
            #     pass
            self.kill_a = sum(jsonpath.jsonpath(data, "$.participants[0:5].stats.kills"))
            self.kill_b = sum(jsonpath.jsonpath(data, "$.participants[5:10].stats.kills"))
            win_id = sum(jsonpath.jsonpath(data, "$.participants[0].stats.win"))
            if win_id:
                self.win_team = self.team_nameLOL[0][0]
            else:
                self.win_team = self.team_nameLOL[1][0]



        elif 'champion' in response.url:
            text = response.text
            data = json.loads(text)
            data1 = jsonpath.jsonpath(data, "$.data[*]")
            for champion in data1:
                self.champion.append([champion['key'], champion['id']])
            print('1')




        else:
            text = response.text
            data = json.loads(text)
            # towerevent={}
            timeline = jsonpath.jsonpath(data, "$.data.timeline[*]")
            k = 0
            for event in timeline:
                if event['type'] == 'tower':
                    self.towerevent[k] = event
                    k = k + 1
            pick_list = jsonpath.jsonpath(data, "$.data.pick_list")
            ban_list = jsonpath.jsonpath(data, "$.data.ban_list")
            team_id = [jsonpath.jsonpath(data, "$.data.team_a.clan_id"),
                       jsonpath.jsonpath(data, "$.data.team_b.clan_id")]
            team_game_id = [jsonpath.jsonpath(data, "$.data.game.blue_clan_id"),
                            jsonpath.jsonpath(data, "$.data.game.red_clan_id")]
            if team_id[0] == team_game_id[0]:
                team_name = [jsonpath.jsonpath(data, "$.data.team_a.team_short_name_a"),
                             jsonpath.jsonpath(data, "$.data.team_b.team_short_name_b")]
            else:
                team_name = [jsonpath.jsonpath(data, "$.data.team_b.team_short_name_b"),
                             jsonpath.jsonpath(data, "$.data.team_a.team_short_name_a")]
            BP_List(pick_list, ban_list, team_name)  ####BP表
            print('12')
