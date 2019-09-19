import discord
from discord.ext.commands import Bot, has_permissions, CheckFailure
from benny import quotes

bot = Bot(command_prefix = '!')
bot.remove_command('help')

benny = quotes()

@bot.event
async def on_ready():
    benny.load()

@bot.command()
async def quote(ctx):
    if benny.count >= benny.length:
        benny.shuffle()
    benny.rotate()
    await ctx.send(benny.quotes[0])

@bot.command()
@has_permissions(administrator=True)
async def add(ctx, *newquote):
    benny.add(newquote)
    benny.load()
    await ctx.send('new quote added')

@add.error
async def add_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.send('you do not have permission to add quotes')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title = 'b3nnyb0t', description = 'bot that performs benny-related functions', color = 0xeee657)
    embed.add_field(name = 'github', value = '[repo](https://github.com/martinibiscotti/b3nnyb0t)')
    embed.add_field(name = 'invite', value = '[link](https://discordapp.com/oauth2/authorize?client_id=id_placeholder&scope=bot)')
    await ctx.send(embed = embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='b3nnyb0t', description = 'bot that performs benny-related functions', color = 0xeee657)
    embed.add_field(name = '!add', value = 'adds new quote', inline = False)
    embed.add_field(name = '!quote', value = 'sends benny quote', inline = False)
    await ctx.send(embed = embed)

bot.run('token placeholder')