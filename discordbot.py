from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='*')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('お兄ちゃん、それはわからないよ。')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
	

class Roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def roll(self,ctx):
        embed = discord.Embed(color=0x0080ff)
        embed.add_field(name='roll num a b n',value='a~bの範囲の値をn個表示するよ。',inline=False)
        embed.add_field(name='roll key n 候補1 候補2 … 候補a', value='a個の候補の中からn個選ぶよ。',inline=False)
        await ctx.send(embed=embed)

    @roll.command()
    async def num(self,ctx,a,b,n):
        a = int(a)
        b = int(b)
        n = int(n)
        embed = discord.Embed(color=0x0080ff)

        if a>b:
            a,b = b,a
        if b - a < n:
            embed.add_field(name='ERROR',value='個数が多すぎるよ、お兄ちゃん。')
        else:
            li = [i for i in range(a,b+1)]
            res = random.sample(li,n)
            embed.add_field(name="roll結果", value=sorted(res), inline=False)
        await ctx.send(embed=embed)

    @roll.command()
    async def key(self,ctx,n,*key):
        n = int(n)
        embed = discord.Embed(color=0x0080ff)
        if len(key)<n:
            embed.add_field(name='ERROR',value='個数が多すぎるよ、お兄ちゃん。')
        else:
            res = ' '.join(random.sample(key,a))
            embed.add_field(name="roll結果", value=res, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Roll(bot))


bot.run(token)
