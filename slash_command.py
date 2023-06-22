from discord import Guild, app_commands
import random
import discord
from discord.ext import commands
from discord import app_commands
import requests

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1069636660230357002))
        self.synved = True
        print(">>Bot is online<<")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="weather", description="Provides weather information", guild=discord.Object(id=1069636660230357002))
async def weather_command(interaction: discord.Interaction, where: str):
    if where == "1":
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-4630FA6E-945C-4380-9F41-65CE0C898E71&format=JSON&locationName=%E8%87%BA%E5%8D%97%E5%B8%82'
    elif where == "2":
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-4630FA6E-945C-4380-9F41-65CE0C898E71&format=JSON&locationName=%E9%AB%98%E9%9B%84%E5%B8%82'
    else:
        await interaction.response.send_message("Invalid subcommand. Please choose either '1' or '2'.")
        return
    
    data = requests.get(url)   # 取得 JSON 檔案的內容為文字
    data_json = data.json()    # 轉換成 JSON 格式

    location_name = data_json['records']['location'][0]['locationName']
    wx = data_json['records']['location'][0]['weatherElement'][0]['time'][0]['parameter']['parameterName']
    max_temp = data_json['records']['location'][0]['weatherElement'][4]['time'][0]['parameter']['parameterName']
    min_temp = data_json['records']['location'][0]['weatherElement'][2]['time'][0]['parameter']['parameterName']
    pop = data_json['records']['location'][0]['weatherElement'][1]['time'][0]['parameter']['parameterName']

    # 輸出天氣資訊
    output = f"{location_name}未來 8 小時{wx}，最高溫 {max_temp} 度，最低溫 {min_temp} 度，降雨機率 {pop} %"
    await interaction.response.send_message(output)


bot.run("MTEyMDI3MjY3OTQ4MDU5MDM0Ng.GwFs_s.mjwX9UIyRBjg03oArdeF-UN6ixXhaQ0fMa4d5s")
