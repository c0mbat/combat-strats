import discord
from discord.ext import commands
import random

#this is the command prefix used to call the bot in Discord
client = commands.Bot(command_prefix = ']')

#when ready the bot will say it is ready and change it's status to helpful info
@client.event
async def on_ready():
    print("Bot user ready")
    game = discord.Game("use ]usage for help.")
    await client.change_presence(status=discord.Status.online, activity=game)

#this is the command for a terrorist random strat
@client.command()
async def t(ctx, level="strats"): #if no argument is given when the bot is called, it will default to strats that work on any map
    t_count = -1
    with open("t_"+level+".txt", 'r') as t_check:    #this counts the amount of lines in the strats.txt files. this is later used
        for line in t_check:                         #when selecting a random line number so that .txt files can be updated and used
            t_count += 1                             #without having to restart the bot and change the line number manually
        
    line = random.randint(0,(t_count)) #this selects a random line number between 0 and the number of lines in the .txt files
    t_strat = open("t_"+level+".txt", "r").readlines()[line] #all files containing strategies are specially named so that the bot can
    await ctx.send(t_strat)                                  #still read all files without being restarted.
 
@client.command()
async def c(ctx, level="strats"):
    c_count = -1
    with open("c_"+level+".txt", 'r') as c_check:          
        for line in c_check:
            c_count += 1
        
    line = random.randint(0,(c_count))
    c_strat = open("c_"+level+".txt", "r").readlines()[line]
    await ctx.send(c_strat)

@client.command()
async def usage(ctx):
    embed = discord.Embed(colour=discord.Colour(0xb800a8), url="https://www.youtube.com/combatrust")

    embed.set_author(name="How to use StratrouletteCS")              #this is a simple Discord embed that displays help on how to use the bot
    embed.set_footer(text="StratrouletteCS by @combat#7871")

    embed.add_field(name="*`]c` or `]t`*", value="   ... will return a random Counter-Terrorist or Terrorist strategy.")
    embed.add_field(name="*Specify a map by adding the map name after the command:*", value="`]c <map name> ` or `]t <map name>`", inline=True)
    embed.add_field(name="*List of supported maps:*", value="none lmao")
    embed.add_field(name="*Use ]invite to generate an invite link for the bot*", value="   ... the bot will come with send message permissions.")

    await ctx.send(embed=embed)

def read_client():
    with open("client.txt", "r") as cID:
        lines = cID.readlines()
        return lines[0].strip()

@client.command()
async def invite(ctx):
    clientID = read_client()    #the client ID is read from a seperate file
    perms = discord.Permissions(permissions=2048)
    inv = discord.utils.oauth_url(clientID, permissions=perms)
    await ctx.send("You can add me to your server by clicking this link:\n\n"+inv)

@client.command()            #this is for debugging, left in because why not
async def ping(ctx):
    await ctx.send("Pong!")    

def read_token():
    with open("token.txt", "r") as tk:     #the bot's token is read from a seperate file named token.txt to avoid accidentally uploading the token to GitHub
        lines = tk.readlines()
        return lines[0].strip()

token = read_token()

client.run(token)
