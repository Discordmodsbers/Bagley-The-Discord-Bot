import discord
from discord.ext import commands
import time
#Some config stuff
intents = discord.intents.All()
allowed_IDs = [123456789, 987654321, ...]
channel = client.get_channel(12324234183172)
bot = commands.Bot(command_prefix='$', intents=intents)
username = os.environ['REPL_OWNER']
Ai_id = 172594 
Key = 'FEo2UNxXAd5PmZkV'
#END

#Functions
@bot.event
async def on_ready():
  print(f"LOGGED INTO: {bot.user}")
  print("ATTEMPTING TO RUN CLUSTER !")
  while True:
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Lovealia"))
    time.sleep(2)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Made by Disaster Aka PlaugeDoctor#3356"))
    time.sleep(2)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Created on: March 1st 2023"))
  

@bot.command()
async def test(ctx):
  await ctx.reply('HAII UWU')


@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
#END

#AI BOT PORTION!!!!!!!
@bot.event
async def on_message(ctx, message):
  if message =='bagley':
    response = requests.get(f'http://api.brainshop.ai/get?bid={Ai_id}&key={Key}&uid={username}&msg={message}')
    data = response.text
    parse_json = json.loads(data)
    response_message = parse_json['cnt']
    await ctx.reply(response_message)
  elif message =='Bagley':
    response = requests.get(f'http://api.brainshop.ai/get?bid={Ai_id}&key={Key}&uid={username}&msg={message}')
    data = response.text
    parse_json = json.loads(data)
    response_message = parse_json['cnt']
    await ctx.reply(response_message)
    
#Owner functions (ONLY FOR PLAUGEDOCTOR AND THE OWNER!)
@bot.command()
async def Announcement(ctx, message):
    if ctx.author.id in allowed_IDs:
        await ctx.reply('POSTED ANNOUCMENT')
        await channel.send(message)
    else:
        #stuff to do if user is not authorized
        ...
#Run Stuff
bot.run('TOKEN')
#END
