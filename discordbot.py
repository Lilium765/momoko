from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='*')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは、お兄ちゃん。')
	
@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('NdN形式 N回、N面ダイスで書いてね、お兄ちゃん。')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('お兄ちゃん、それはわからないよ。')

bot.run(token)
