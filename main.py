  import discord
  from discord.ext import commands
  from keep_alive import keep_alive
  from replit import db
  import os
  import praw
  
  # my_secret = os.environ['lol']
  client = discord.Client()
  reddit_read_only = praw.Reddit(client_id="ur client id", client_secret="ur client secret", user_agent="testscrape")
  subreddit = reddit_read_only.subreddit("subreddit of choice without r/")
  bot = commands.Bot(command_prefix="!")
  
  @client.event
  async def on_message(message):
    global subreddit
    msg = message.content
    if msg.startswith('!top'):
      try:
        numb = int(msg[5:])
        top_memes = subreddit.top("day", limit=numb)
        for submission in top_memes:
          if (numb > 1):
            numb -= 1
            continue
          await message.channel.send(submission.url)
          await message.channel.send("https://www.reddit.com" + submission.permalink)
      except ValueError:
        top_memes = subreddit.top("day", limit=1)
        for submission in top_memes:
          await message.channel.send(submission.url)
          await message.channel.send("https://www.reddit.com" + submission.permalink)
          break
    if msg.startswith('!alltop') and message.author.id == 312759823479472128:
      top_memes = subreddit.top("day", limit=100)
      for submission in top_memes:
        await message.channel.send(submission.url)
        await message.channel.send("https://www.reddit.com" + submission.permalink)
  
  
  
  keep_alive()
  # requires keep_alive.py in repl
  client.run('discord bot token thing')