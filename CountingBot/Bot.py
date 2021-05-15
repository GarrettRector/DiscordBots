import discord

client = discord.Client()


@client.event
async def on_message(ctx):
    if ctx.channel.id == COUNTING CHANNEL:
        number = open("Number.txt", "r")
        num = number.read()
        print(num)
        if ctx.content != num:
            await ctx.delete()
        else:
            nums = int(num) + 1
            nums = str(nums)
            numbs = open("Number.txt", "w")
            numbs.write(nums)


client.run(TOKEN)
