import discord
import os
from discord.commands.core import slash_command

intents = discord.Intents.default()

bot = discord.Bot(
  intents=intents,
  debug_guilds=[1251165789705207911]
)



@bot.slash_command(desctiption="You will be told what to expect")
async def leaks(ctx):
  embed = discord.Embed(
    title="Leaks at Server!" ,
    description="There is free access to some channels on the leak server. If that isn't enough, you can purchase videos. Have a wonderful time in the server!",
    color=0x627657
  )
  embed.set_footer(text="Made by Uga")
  await ctx.respond(embed=embed)
    

@bot.event
async def on_member_join(member):
  embed = discord.Embed(
    title="Welcome to the Server!",
    description=f"Welcome to the Uga Leak Server, have fun {member.montion}!",
    color=0x627657

  )
  embed.set_thumbnail(url=member.avatar.url)
  embed.set_footer(text="Made by Uga")
  channel = bot.get_channel(1251168158643912704)
  await channel.send(f"Welcome to the Uga Leak Server {member.mention}")

                  




bot.run(os.environ['TOKEN'])
