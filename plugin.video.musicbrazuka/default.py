# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/gsfvideos
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.musicbrazuka'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')
icon = local.getAddonInfo('icon')
icon2 = "special://home/addons/plugin.video.musicbrazuka/Capas/shows.jpg"
icon3 = "special://home/addons/plugin.video.musicbrazuka/Capas/melhores.jpg"
icon4 = "special://home/addons/plugin.video.musicbrazuka/Capas/videos.jpg"
icon5 = "special://home/addons/plugin.video.musicbrazuka/Capas/top.jpg"
icon6 = "special://home/addons/plugin.video.musicbrazuka/Capas/anos.jpg"
icon7 = "special://home/addons/plugin.video.musicbrazuka/Capas/classico.jpg"
icon8 = "special://home/addons/plugin.video.musicbrazuka/Capas/toppop.jpg"
icon9 = "special://home/addons/plugin.video.musicbrazuka/Capas/pop.jpg"
icon10 = "special://home/addons/plugin.video.musicbrazuka/Capas/lancpop.jpg"
icon11 = "special://home/addons/plugin.video.musicbrazuka/Capas/tbr.jpg"
icon12 = "special://home/addons/plugin.video.musicbrazuka/Capas/tr.jpg"
icon13 = "special://home/addons/plugin.video.musicbrazuka/Capas/cr.jpg"
icon14 = "special://home/addons/plugin.video.musicbrazuka/Capas/mm.jpg"
icon15 = "special://home/addons/plugin.video.musicbrazuka/Capas/mt.jpg"
icon16 = "special://home/addons/plugin.video.musicbrazuka/Capas/cm.jpg"
addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID = "playlist/PLcsMX-TwGym6iK1EgOkl6q8cR1VVFRkKy"
YOUTUBE_CHANNEL_ID2 = "playlist/PL_Q15fKxrBb5hIXum_6kk5vUiPxqFJaH8"
YOUTUBE_CHANNEL_ID3 = "playlist/PLrAwPW0DD1gIVYye-sObT1m-QWJlr7rIM"
YOUTUBE_CHANNEL_ID4 = "playlist/PLB8HqqmpyIBfdUtpzHax1jLmMLKRHcgF1"
YOUTUBE_CHANNEL_ID5 = "playlist/PLdQ4n6NTvkjHPU078MgYl3m48cvlap0fi"
YOUTUBE_CHANNEL_ID6 = "playlist/PLPcFC8viD-2O5eY1GZvmpHJHg9J4e4ClV"
YOUTUBE_CHANNEL_ID7 = "playlist/PL_Q15fKxrBb70cuYuG1e8197zcXOTX5rQ"
YOUTUBE_CHANNEL_ID8 = "playlist/PLB8HqqmpyIBdiRK9o_Xv4Yfr8BJeHxrHB"
YOUTUBE_CHANNEL_ID9 = "playlist/PLOvc47UgH6TCA-HqSitq7-w5bgn5CkhQ0"
YOUTUBE_CHANNEL_ID10 = "playlist/PL2MNAymGX6Du_z617o0ko7Trr9MRCtYg0"
YOUTUBE_CHANNEL_ID11 = "playlist/PLB8HqqmpyIBcAHYt_w15AprSLViIGrToO"
YOUTUBE_CHANNEL_ID12 = "playlist/PLdiTb55wBMHx2en0ShdG1QOCMwXFh17gm"
YOUTUBE_CHANNEL_ID13 = "playlist/PL_Q15fKxrBb7C163SjzBIPYMrGcNzb_-X"
YOUTUBE_CHANNEL_ID14 = "playlist/PLtlvnqGZ6MnCzdHBjC3FUVrm21lOKjDk7"
YOUTUBE_CHANNEL_ID15 = "playlist/PLCfIb_L7XB6qW7c_eV7VmYgyW8R8tAWDK"


# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("musicbrazuka.main_list "+repr(params))
	
	plugintools.log("musicbrazuka.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "SHOWS COMPLETOS",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon2,
		folder = True )
		
plugintools.add_item(
		title = "MELHORES ROCK NACIONAL",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon3,
		folder = True )

plugintools.add_item(
		title = "POP ROCK, ROCK NACIONAL e REGGAE ",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon4,
		folder = True )		

plugintools.add_item(
		title = "TOP ROCK NACIONAL",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon5,
		folder = True )		

plugintools.add_item(
		title = "ROCK ANOS 80,90 E 2000",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon6,
		folder = True )		
		
plugintools.add_item(
		title = "ROCK NACIONAL CLASSICO",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon7,
		folder = True )	
		
		
plugintools.add_item(
		title = "TOP 100 POP",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon8,
		folder = True )	
		
plugintools.add_item(
		title = "POP NACIONAL",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon9,
		folder = True )	
		
plugintools.add_item(
		title = "LANCAMENTO POP",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon10,
		folder = True )			
		
plugintools.add_item(
		title = "THE BEST REGGAE",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail = icon11,
		folder = True )		

plugintools.add_item(
		title = "TOP REGGAE",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail = icon12,
		folder = True )		

plugintools.add_item(
		title = "COLETÂNEA REGGAE",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail = icon13,
		folder = True )		

plugintools.add_item(
		title = "MELHORES MPB",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID13+"/",
		thumbnail = icon14,
		folder = True )		

plugintools.add_item(
		title = "TOP MPB",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID14+"/",
		thumbnail = icon15,
		folder = True )		

plugintools.add_item(
		title = "COLETÂNEA MPB",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID15+"/",
		thumbnail = icon16,
		folder = True )				
run()