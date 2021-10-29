from os import environ as env
from dotenv import load_dotenv
import reddit_mod
import random
from discord.ext import commands

load_dotenv()

bot = commands.Bot(description="test", command_prefix="!")

@bot.command()
async def meme(ctx):
    print(ctx)
    r = reddit_mod.RedditSubreddit('ProgrammerHumor',limit=100)
    post_to_pick = random.randint(1, 99)
    post = r.posts[post_to_pick]

    if post.preview == None:
        u = post.link
    else:
        u = post.preview

    txt = f'{post.title}\n{u}'
    await ctx.channel.send(txt)


bot.run(env['TOKEN'])
