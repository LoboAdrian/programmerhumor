import reddit_mod
import random
from discord.ext import commands

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


bot.run('OTAzMzU3MTg5NzI3NjA0Nzk2.YXry8Q.whqmSrfryPIVppB_esObGYD0gxw')
