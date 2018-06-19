import config
import discord
import asyncio
import urllib3
import certifi
import idna
import requests

def getAccount(username):
    reqUrl = config.gd_server + "getGJUsers20.php"
    param = {
        'gameVersion' : 21,
        'binaryVersion' : 34,
        'gdw' : 0,
        'str' : username,
        'total' : 0,
        'page' : 0,
        'secret' : config.secret
    }
    r = requests.get(url = reqUrl, params = param)
    res = r.text.split("#")[0]
    i = 0
    while i < len(res.split("|")):
        if username == res.split("|")[i].split(":")[1]:
            result = res.split("|")[i]
            return result
        i = i + 1
    return -1
def getStars(acc):
    return acc.split(":")[21]
def getUsername(acc):
    return acc.split(":")[1]
def getDiamonds(acc):
    return acc.split(":")[17]
def getCoins(acc):
    return acc.split(":")[6]
def getUCoins(acc):
    return acc.split(":")[8]
def getDemons(acc):
    return acc.split(":")[25]
def getCP(acc):
    return acc.split(":")[23]
def getAccountInfo(acc):
    eb = discord.Embed()
    eb.add_field(name=":chart_with_upwards_trend:  " + getUsername(acc) + "'s stats",
                 value"<:Star:376445841885495316>  " + getStars(acc)+ "\t\t"
		 + "<:Diamond:376444770613985280>  " + getDiamonds(acc) + "\t\t"
		 + "<:UserCoin:376444770438086667>  " + getUCoins(acc) + "\t\t"
		 + "<:SecretCoin:376444770156937228>  " + getCoins(acc) + "\t\t"
		 + "<:Demon:376444770186166273>  " + getDemons(acc) + "\t\t"
		 + "<:CreatorPoints:364075937857273867>  " + getCP(acc) + "\n");
    return eb.to_dict()
