import discord
from discord.ext import tasks
import os
from keep_alive import keep_alive
import seleniumm
from datetime import datetime
import time

client = discord.Client()

@tasks.loop(minutes=30)
async def send():
    channel = client.get_channel(835869225066692668)
  
    data_list=seleniumm.get_data()
    for i in data_list:
      print (i)
      
    time.sleep(5)
    embed = discord.Embed(
        title="Sei Network Explorer",
        url="https://sei.explorers.guru/",
        description="Easisest way to following SEI Blockchain.",
        color=0x109319)
    embed.add_field(name="Latest Block", value=str(data_list[0]), inline=True)
    embed.add_field(name="Block Time", value=str(data_list[3]), inline=True)
    embed.add_field(name="Chain", value=str(data_list[4]), inline=True)
    embed.add_field(name="Online Voting Power",
                    value=str(data_list[5]),
                    inline=True)
    embed.add_field(name="Active Validators",
                    value=str(data_list[6]),
                    inline=True)
    embed.add_field(name="Supply", value=str(data_list[1]), inline=True)
    embed.add_field(name="Community Pool",
                    value=str(data_list[2]),
                    inline=True)
    embed.add_field(name="APR", value=str(data_list[7]), inline=True)
    embed.add_field(name="Inflation", value=str(data_list[8]), inline=True)
    utc_now_dt = datetime.utcnow()
    embed.set_footer(text='Data has taken with Datetime in UTC: ' +
                     str(utc_now_dt))
    await channel.send(embed=embed)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    send.start()

keep_alive()
client.run(os.environ['TOKEN'])