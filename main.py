from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='$')


@bot.command()
async def sell(ctx, good, price, img):
    channel = bot.get_channel(829711304230961174)
    emojis = ['👍', '👎']
    OP = ctx.author.id
    global message, im
    message = await channel.send(f"item for sale: {good}\nSeller: <@{ctx.author.id}>\nPrice (USD): {price}\n{img}")
    await asyncio.sleep(.1)
    await ctx.channel.purge(limit=1)
    for emoji in emojis:
        await message.add_reaction(emoji)

    @bot.event
    async def on_reaction_add(reaction, user):
        emoji = reaction.emoji
        user = user.id
        client = await bot.fetch_user(OP)
        if (emoji == "👍") & (user != OP & 829903933329244170):
            await client.send(f'<@{OP}>, <@{user}> would like to purchase your item, "{good}" for {price} USD. You can get in touch with them through the @ mention')
        elif (emoji == "👎") & (user == OP):
            await message.remove_reaction("👎", client)
        elif (emoji == "👍") & (user == OP):
            await client.send("You can't buy your own item, dummy")
            await message.remove_reaction("👍", client)

@bot.command()
async def buy(ctx, good, price):
    channel = bot.get_channel(829711304230961174)
    emojis = ['👍', '👎']
    OP = ctx.author.id
    global message, im
    message = await channel.send(f"Buy request for: {good}\nBuyer: <@{ctx.author.id}>\nDesired price (USD): {price}")
    await asyncio.sleep(.1)
    await ctx.channel.purge(limit=1)
    for emoji in emojis:
        await message.add_reaction(emoji)

    @bot.event
    async def on_reaction_add(reaction, user):
        emoji = reaction.emoji
        user = user.id
        client = await bot.fetch_user(OP)
        if (emoji == "👍") & (user != OP & 829903933329244170):
            client = await bot.fetch_user(OP)
            await client.send(f'User <@{user}> has your item, "{good}", and wants {price} for it')
        elif (emoji == "👎") & (user == OP):
            await message.remove_reaction("👎", client)
        elif (emoji == "👍") & (user == OP):
            await client.send("You can't buy your own item, dummy")
            await message.remove_reaction("👍", client)


@bot.command()
async def bothelp(ctx):
    await ctx.send(f"dababy bot is a bot that allows you to list items for sale and to trade with other people.\nTo get started just type $sell Item, Price and it will list your item in the #listings channel")


@bot.event
async def on_ready():
    print("ready")


bot.run("TOKEN")
