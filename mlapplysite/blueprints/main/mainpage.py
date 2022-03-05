import math
import time
from mlapplysite.blueprints.main import main
from flask import render_template
import requests
from flask import request
from loguru import logger


API_KEY="e126c953-d76e-4077-a69f-f66bcf6e3772"
@main.route("/test", methods=['post', 'get'])
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

                if (
                        buildbattle or skywars or bedwars or quake or tnttag or uhc or duels or murdermystery or arcade or skyblock) and round(
                    1 + -3.5 + math.sqrt(12.25 + 0.0008 * data['player']['networkExp'])) >= 55:
                        da = "Подходит"
                else:
                    da = "Не подходит"
            except:
                logger.error('Error in data')
        except:
            logger.error('Error POST method')

    return render_template('main.html', name = username, guild=da)
