import stat
import discord
from discord.ext import commands
import youtube_dl
import stat
import os


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Not in a VC")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def dc(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        await self.join(ctx)
        ffmpeg_options = {"before_options": "-reconnect 1 - reconnect_streamed 1 "
                                            "-reconnect_delay_max 5", "options": "vn"}
        ydl_options = {"format": "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            data = ydl.extract_info(url, download=False)
            url2 = data["formats"][0]["url"]
            os.chmod("main.py", stat.S_IWRITE)
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options, executable="C:/FFmpeg/bin")
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused!")

    @commands.command()
    async def unpause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Playing!")


def setup(client):
    client.add_cog(Music(client))
