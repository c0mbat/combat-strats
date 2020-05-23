import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ']')

@client.event
async def on_ready():
    print("Bot user ready")
    game = discord.Game("use ]usage for help.")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command()
async def t(ctx, level="None"):
    if level == ("None"):
        t_count = -1
        with open("t_strats.txt", 'r') as t_check:
            for line in t_check:
                t_count += 1
        
        line = random.randint(0,(t_count))
        t_strat = open("t_strats.txt", "r").readlines()[line]
        await ctx.send(t_strat)

    else:
        t_count = -1
        with open("t_"+level+".txt", 'r') as t_check:
            for line in t_check:
                t_count += 1
        
        line = random.randint(0,(t_count))
        t_strat = open("t_"+level+".txt", "r").readlines()[line]
        await ctx.send(t_strat)
 
@client.command()
async def c(ctx, level="None"):
    if level == ("None"):
        c_count = -1
        with open("c_strats.txt", 'r') as c_check:
            for line in c_check:
                c_count += 1
        
        line = random.randint(0,(c_count))
        c_strat = open("c_strats.txt", "r").readlines()[line]
        await ctx.send(c_strat)

    else:
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

    embed.set_author(name="How to use CS Strats Bot")
    embed.set_footer(text="CS:GO Strats Bot by @combat#7871")

    embed.add_field(name="*`]c` or `]t`*", value="   ... will return a random Counter-Terrorist or Terrorist strategy.")
    embed.add_field(name="*Specify a map by adding the map name after the command:*", value="`]c <map name> ` or `]t <map name>`", inline=True)
    embed.add_field(name="*List of supported maps:*", value="none lmao")

    await ctx.send(embed=embed)




@client.command()
async def ping(ctx):
    await ctx.send("Pong!")    

def read_token():
    with open("token.txt", "r") as tk:
        lines = tk.readlines()
        return lines[0].strip()

token = read_token()

client.run(token)
