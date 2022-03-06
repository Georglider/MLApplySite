import math
import time
from mlapplysite.blueprints.main import main
from flask import render_template, redirect
import requests
from flask import request
from loguru import logger


API_KEY="e126c953-d76e-4077-a69f-f66bcf6e3772"
@main.route("/statscheck", methods=['post', 'get'])
def mainpage():
    username=""
    name=""
    level=""
    bw=""
    da=""
    guild=""
    if request.method == "POST":
        try:
            username = request.form.get('username')
            print(username)
            data = requests.get(url=f"https://api.slothpixel.me/api/players/{username}").json()
            try:
                response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}?").json()
                uuid = response['id']
                data = requests.get(
                    url="https://api.hypixel.net/player",
                    params={
                        "key": f"{API_KEY}",
                        "uuid": f"{uuid}"
                    }
                ).json()

                if not 'player' in data:

                    return

                # if not 'socialMedia' in data['player']:
                #     await self.no_discord(ctx, ign, "дискорд не привязан.")
                #     return
                # if not 'DISCORD' in data['player']['socialMedia']['links']:
                #     await self.no_discord(ctx, ign, "дискорд не привязан.")
                #     return
                # if str(data["player"]["socialMedia"]["links"]["DISCORD"]) != str(ctx.author):
                #     await self.no_discord(ctx, ign, "указанный дискорд не соответствует данному.")
                #     return

                skywars, buildbattle, bedwars, quake, tnttag, uhc, duels, murdermystery, arcade = False, False, False, False, False, False, False, False, False
                skywarsr, buildbattler, bedwarsr, quaker, tnttagr, uhcr, duelsr, murdermysteryr, arcader = 0, 0, 0, 0, 0, 0, 0, 0, 0
                skyblockavg = 0
                skyblock = 0
                if 'SkyWars' in data['player']['stats']:
                    if 'kills' in data['player']['stats']['SkyWars']:
                        skywars = data['player']['stats']['SkyWars']['kills'] >= 2000
                        skywarsr = data['player']['stats']['SkyWars']['kills']
                if 'BuildBattle' in data['player']['stats']:
                    if 'score' in data['player']['stats']['BuildBattle']:
                        buildbattle = data['player']['stats']['BuildBattle']['score'] >= 2000
                        buildbattler = data['player']['stats']['BuildBattle']['score']
                if 'Bedwars' in data['player']['stats']:
                    if 'final_kills_bedwars' in data['player']['stats']['Bedwars']:
                        bedwars = data['player']['stats']['Bedwars']['final_kills_bedwars'] >= 500
                        bedwarsr = data['player']['stats']['Bedwars']['final_kills_bedwars']
                if 'Quake' in data['player']['stats']:
                    if 'kills' in data['player']['stats']['Quake']:
                        quake = data['player']['stats']['Quake']['kills'] >= 1000
                        quaker = data['player']['stats']['Quake']['kills']
                if 'TNTGames' in data['player']['stats']:
                    if 'wins_tntag' in data['player']['stats']['TNTGames']:
                        tnttag = data['player']['stats']['TNTGames']['wins_tntag'] >= 10
                        tnttagr = data['player']['stats']['TNTGames']['wins_tntag']
                if 'UHC' in data['player']['stats']:
                    if 'wins_solo' in data['player']['stats']['UHC'] and 'wins' in data['player']['stats']['UHC']:
                        uhc = data['player']['stats']['UHC']['wins_solo'] >= 1 or data['player']['stats']['UHC'][
                            'wins'] >= 1
                        uhcr = data['player']['stats']['UHC']['wins_solo'] >= 1 or data['player']['stats']['UHC'][
                            'wins']
                if 'Duels' in data['player']['stats']:
                    if 'wins' in data['player']['stats']['Duels']:
                        duels = data['player']['stats']['Duels']['wins'] >= 800
                        duelsr = data['player']['stats']['Duels']['wins']
                if 'MurderMystery' in data['player']['stats']:
                    if 'wins' in data['player']['stats']['MurderMystery']:
                        murdermystery = data['player']['stats']['MurderMystery']['wins'] >= 200
                        murdermysteryr = data['player']['stats']['MurderMystery']['wins']
                if 'Arcade' in data['player']['stats']:
                    arcadetmp = data['player']['stats']['Arcade']
                    arcade = 0
                    if 'wins_party_3' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_party_2"]
                    if 'wins_party_2' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_party_2"]
                    if 'wins_party' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_party"]
                    if 'wins_simon_says' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_simon_says"]
                    if 'sw_game_wins' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["sw_game_wins"]
                    if 'wins_soccer' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_soccer"]
                    if 'wins_mini_walls' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_mini_walls"]
                    if 'wins_draw_their_thing' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_draw_their_thing"]
                    if 'wins_hole_in_the_wall' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_hole_in_the_wall"]
                    if 'wins_farm_hunt' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_farm_hunt"]
                    if 'seeker_wins_hide_and_seek' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["seeker_wins_hide_and_seek"]
                    if 'party_pooper_seeker_wins_hide_and_seek' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["party_pooper_seeker_wins_hide_and_seek"]
                    if 'wins_dragonwars2' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_dragonwars2"]
                    if 'wins_hypixel_sports' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_hypixel_sports"]
                    if 'wins_throw_out' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_throw_out"]
                    if 'wins_grinch_simulator_v2' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_grinch_simulator_v2"]
                    if 'wins_oneinthequiver' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_oneinthequiver"]
                    if 'prop_hunt_seeker_wins_hide_and_seek' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["prop_hunt_seeker_wins_hide_and_seek"]
                    if 'hider_wins_hide_and_seek' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["hider_wins_hide_and_seek"]
                    if 'party_pooper_hider_wins_hide_and_seek' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["party_pooper_hider_wins_hide_and_seek"]
                    if 'wins_dayone' in data['player']['stats']['Arcade']:
                        arcade += arcadetmp["wins_dayone"]
                    arcader = arcade
                    arcade = arcade > 200
                if 'SkyBlock' in data['player']['stats']:
                    if data['player']['stats']['SkyBlock']:
                        skyblockavg = 0
                        sbstats = requests.get(
                            f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={uuid}").json()
                        levels = [50, 125, 200, 300, 500, 750, 1000, 1500, 2000, 3500, 5000, 7500, 10000, 15000, 20000,
                                  30000,
                                  50000, 75000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000,
                                  1000000,
                                  1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000,
                                  2000000,
                                  2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2750000, 2900000, 3100000,
                                  3400000,
                                  3700000, 4000000, 4300000, 4600000, 4900000, 5200000, 5500000, 5800000, 6100000,
                                  6400000,
                                  6700000, 7000000]
                        lvlcaps = [60, 50, 50, 60, 60, 60, 50, 50]
                        catacombslvl = [50, 75, 110, 160, 230, 330, 470, 670, 950, 1340, 1890, 2665, 3760, 5260, 7380,
                                        10300,
                                        14400, 20000, 27600, 38000, 52500, 71500, 97000, 132000, 180000, 243000, 328000,
                                        445000,
                                        600000, 800000, 1065000, 1410000, 1900000, 2500000, 3300000, 4300000, 5600000,
                                        7200000,
                                        9200000, 12000000, 15000000, 19000000, 24000000, 30000000, 38000000, 48000000,
                                        60000000,
                                        75000000, 93000000, 116250000]
                        if sbstats['profiles'] != None:
                            for i in sbstats['profiles']:
                                player = i['members'][uuid]
                                if not 'experience_skill_mining' in player or not 'experience_skill_alchemy' in player or not 'experience_skill_taming' in player or not 'experience_skill_combat' in player or not 'experience_skill_farming' in player or not 'experience_skill_enchanting' in player or not 'experience_skill_fishing' in player or not 'experience_skill_foraging' in player or not 'experience_skill_carpentry' in player:
                                    print("smth went wrong")
                                    continue
                                avg = 0
                                skills = [player['experience_skill_mining'], player['experience_skill_alchemy'],
                                          player['experience_skill_taming'], player['experience_skill_combat'],
                                          player['experience_skill_farming'], player['experience_skill_enchanting'],
                                          player['experience_skill_fishing'], player['experience_skill_foraging'],
                                          player['experience_skill_carpentry']]
                                for x in skills:
                                    exp = x
                                    lvlxp = 0
                                    iteration = 0
                                    maxlvl = lvlcaps[iteration]
                                    while exp > lvlxp and iteration < maxlvl:
                                        lvlxp = levels[iteration]
                                        exp -= lvlxp
                                        iteration += 1
                                    avg += 1 + iteration
                                exp = player['dungeons']['dungeon_types']['catacombs']['experience']
                                lvlxp = 0
                                iteration = 0
                                maxlvl = 50
                                avg += 1 + iteration
                                while exp > lvlxp and iteration < maxlvl:
                                    lvlxp = catacombslvl[iteration]
                                    exp -= lvlxp
                                    iteration += 1
                                if avg > skyblockavg:
                                    skyblockavg = avg / 10
                    if skyblockavg == 0:
                        print("api closed or no profile")
                        skyblock = 0
                    else:
                        skyblock = skyblockavg >= 19
                if (
                        buildbattle or skywars or bedwars or quake or tnttag or uhc or duels or murdermystery or arcade or skyblock) and round(
                    1 + -3.5 + math.sqrt(12.25 + 0.0008 * data['player']['networkExp'])) >= 55:
                        da = "Подходит"
                        return redirect("/redirecturl")
                else:
                    da = "Не подходит"
            except:
                logger.error('Error in data')
        except:
            logger.error('Error POST method')

    return render_template('main.html', name = username, guild=da)
