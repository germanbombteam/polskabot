#Polskabot made by Borkductions.

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("Horace, thanks for making me alive!")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
#development
@bot.command(pass_context=True)
async def facepalm(ctx, user: discord.Member):
    await bot.say("Ouch! :sob: Do not of hittings Polska plox!") 

@bot.command(pass_context=True)
async def anschluss(ctx):
    await bot.say("Kurwa!")
    pass

@bot.command(pass_context=True)
async def syskey(ctx):
    await bot.say("**I am not a scammer!**")
    pass

@bot.command(pass_context=True)
async def space(ctx):
    await bot.say("Poland can into space? **Into space!**")
    pass

@bot.command(pass_context=True)
async def introduce(ctx):
    await bot.say("Hello. I am Polskabot. Kurwa!")
    await bot.say("I was created by **Horace Leung** in Hong Kong using the Python programming language. Thanks Horace for making me alive")
    await bot.say("I was designed to imitate **Polandball**, a character in a type of comic in the same name.")
    pass


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

bot.run("Mzk3NjA4NDM0NDk0ODY1NDE4.DSyj1Q.a9OsjMSJpXBdP4A207DJ0peiPrQ")