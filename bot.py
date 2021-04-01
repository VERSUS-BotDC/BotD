import discord
from discord.ext import commands
import asyncio

client = discord.Client()
prefix = '.'
client = commands.Bot(command_prefix = prefix)
#--console
@client.event
async def on_ready():
  print('Connected')

#--clear 
@client.command(pass_context = True)

async def clear(ctx,amount = 10):
  await ctx.channel.purge(limit = amount + 1)

#--Test
@client.command(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
  muterole = discord.utils.get(ctx.guild.roles,name='Muted')
  emb = discord.Embed(title="Мут",color=0xff0000)
  emb.add_field(name="Модератор",value=ctx.message.author.mention,inline=False)
  emb.add_field(name="Нарушитель",value=member.mention,inline=False)
  emb.add_field(name="Причина",value=reason,inline=False)
  emb.add_field(name="Время",value=time,inline=False)
  await member.add_roles(muterole)
  await ctx.send(embed = emb)
  await asyncio.sleep(time * 60)
  await member.remove_roles(muterole)
  
@client.command(view_audit_log=True)
async def unmute(ctx,member:discord.Member):
  muterole = discord.utils.get(ctx.guild.roles,name='Muted')
  emb = discord.Embed(title="АнМут",color=0xff0000)
  emb.add_field(name="Модератор",value=ctx.message.author.mention,inline=False)
  emb.add_field(name="Нарушитель",value=member.mention,inline=False)
  await ctx.send(embed = emb)
  await member.remove_roles(muterole)


@client.command(view_audit_log=True)
async def kick(ctx,member:discord.Member,reason):
  emb = discord.Embed(title="Кик",color=0xff0000)
  emb.add_field(name="Модератор",value=ctx.message.author.mention,inline=False)
  emb.add_field(name="Нарушитель",value=member.mention,inline=False)
  emb.add_field(name="Причина",value=reason,inline=False)
  await member.kick()
  await ctx.send(embed = emb)
  
  
@client.command(view_audit_log=True)
async def ban(ctx,member:discord.Member,reason):
  emb = discord.Embed(title="Бан",color=0xff0000)
  emb.add_field(name="Модератор",value=ctx.message.author.mention,inline=False)
  emb.add_field(name="Нарушитель",value=member.mention,inline=False)
  emb.add_field(name="Причина",value=reason,inline=False)
  await member.ban()
  await ctx.send(embed = emb)
  
  
#--editmessage
@client.event
async def on_message_edit(before, after):
  if before.content == after.content:
   return
  
  await before.channel.send(f'Сообщение было изменено\n{before.content} -> {after.content}')  

client.run('ODI3MTE5Njk3MTAyMTEwNzIw.YGWZPg.7PYeH9PRpM8J0-c9UU_LRTSkI7U')