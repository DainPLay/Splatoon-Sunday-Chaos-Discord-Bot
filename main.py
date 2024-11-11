import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import random

intent_used = discord.Intents.all()

prefixes = ["!", "/"]
bot = commands.Bot(command_prefix=prefixes, intents=intent_used)

TOKEN = 'token'

player_names = ["SoSou", "Clyde", "Vinogradka", "FBK Asri", "Михаил", "ах~покпок~", "DainPLayST", "CyM4aTbIu", "Hanroher", "DblCookies", "Nermon", "Crowley", "silly!Bird", "DerlinST", "Чукча", "jEeo", "Миха", "NovohArt", "Summer23", "Mister245", "Marie_simp", "Darth_Mike", "rdrgs", "ykino", "Пальццверх", "nyaroru", "miitara", "Nikita.I", "Aloha", "InIRachelR", "Notus", "Колбасен", "akito_crab", "o", "pokpok096", "средненько"]
player_tags = ["344395442697666563", "654722816586809344", "1141271187398336513", "553653885110321192", "860613155888562216", "787706077331980299", "354304520240758804", "317394240210599936", "290436004018520065", "229636674215346176", "467053520982376469", "451829283334258695", "867483082214473729", "358338873824378890", "765232045617053706", "1024694754618900490", "743051426996944896", "580449625597542430", "468791673619742720", "396959340545835008", "878219609386414130", "279931620574756865", "705321818218692648", "236879839196479488", "681185803346640907", "343847758119043073", "324214008326520833", "532155957413675018", "529946353732943881", "1040995870579109958", "257180284443688961", "338035621945802762", "432536871189610499", "273808847930654730", "662311028725514240", "488339055856189470"]
player_ids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

@bot.event
async def on_ready():
    print("Online!")
    await bot.change_presence(activity=discord.Game('Ищу где делать ставки ан Splatoon Sunday'))


@bot.command()
async def start(ctx):
    if str(ctx.author) == 'munaat#0':
        print('yup')
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')


@bot.command()
async def r1s(ctx):
    if str(ctx.author) == 'dain_play#0':
        random.shuffle(player_ids)
        with open('r1_teams.txt', 'w') as f:
            for line in player_ids:
                f.write("%s\n" % line)
        games = [0,0,0,0]
        with open('r1_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
        for i in range(4):
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            edit(img, 'r1_teams.txt', 8*i, i+1, 0, 2)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r1_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'w') as s:
            for line_number, line in enumerate(f, 1):
                if line_number > 32:
                    s.write(line)
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2s(ctx):
    if str(ctx.author) == 'dain_play#0':
        f = open('r2_teams.txt')
        r2_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r2_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r2_teams)
        with open('r2_teams.txt', 'w') as f:
            for line in r2_teams:
                f.write("%s\n" % line)
        games = [0,0,0]
        with open('r2_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
        for i in range(2):
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            edit(img, 'r2_teams.txt', 8*i, i+5, 0, 2)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            await ctx.send('<@' + player_tags[r2_teams[i*8]] + '> <@' + player_tags[r2_teams[i*8+1]] + '> <@' +
            player_tags[r2_teams[i*8+2]] + '> <@' + player_tags[r2_teams[i*8+3]] + ">\n# против\n<@" +
            player_tags[r2_teams[i*8+4]] + '> <@' + player_tags[r2_teams[i*8+5]] + '> <@' +
            player_tags[r2_teams[i*8+6]] + '> <@' + player_tags[r2_teams[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
            #Лузера
        f = open('r2_losers.txt')
        r2_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r2_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r2_teams)
        with open('r2_losers.txt', 'w') as f:
            for line in r2_teams:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'r2_losers.txt', 8 * i, i + 7, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[r2_teams[i * 8]] + '> <@' + player_tags[r2_teams[i * 8 + 1]] + '> <@' +
                       player_tags[r2_teams[i * 8 + 2]] + '> <@' + player_tags[
                           r2_teams[i * 8 + 3]] + ">\n# против\n<@" +
                       player_tags[r2_teams[i * 8 + 4]] + '> <@' + player_tags[r2_teams[i * 8 + 5]] + '> <@' +
                       player_tags[r2_teams[i * 8 + 6]] + '> <@' + player_tags[r2_teams[i * 8 + 7]] + '>',
                       file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3s(ctx):
    if str(ctx.author) == 'dain_play#0':
        f = open('r3_teams.txt')
        r3_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r3_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r3_teams)
        with open('r3_teams.txt', 'w') as f:
            for line in r3_teams:
                f.write("%s\n" % line)
        games = [0,0,0]
        with open('r3_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'r3_teams.txt', 8*i, i+8, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[r3_teams[i*8]] + '> <@' + player_tags[r3_teams[i*8+1]] + '> <@' +
        player_tags[r3_teams[i*8+2]] + '> <@' + player_tags[r3_teams[i*8+3]] + ">\n# против\n<@" +
        player_tags[r3_teams[i*8+4]] + '> <@' + player_tags[r3_teams[i*8+5]] + '> <@' +
        player_tags[r3_teams[i*8+6]] + '> <@' + player_tags[r3_teams[i*8+7]] + '>',
        file=discord.File(f'images/Requests/result{i}.png'))
            #Лузера
        f = open('r3_losers.txt')
        r3_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r3_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r3_teams)
        with open('r3_losers.txt', 'w') as f:
            for line in r3_teams:
                f.write("%s\n" % line)
        for i in range(2):
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            edit(img, 'r3_losers.txt', 8 * i, i + 9, 0, 2)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            await ctx.send('<@' + player_tags[r3_teams[i * 8]] + '> <@' + player_tags[r3_teams[i * 8 + 1]] + '> <@' +
                       player_tags[r3_teams[i * 8 + 2]] + '> <@' + player_tags[
                           r3_teams[i * 8 + 3]] + ">\n# против\n<@" +
                       player_tags[r3_teams[i * 8 + 4]] + '> <@' + player_tags[r3_teams[i * 8 + 5]] + '> <@' +
                       player_tags[r3_teams[i * 8 + 6]] + '> <@' + player_tags[r3_teams[i * 8 + 7]] + '>',
                       file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4s(ctx):
    if str(ctx.author) == 'dain_play#0':
        f = open('r4_teams.txt')
        r4_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r4_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r4_teams)
        with open('r4_teams.txt', 'w') as f:
            for line in r4_teams:
                f.write("%s\n" % line)
        games = [0,0,0]
        with open('r4_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'r4_teams.txt', 8*i, i+11, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[r4_teams[i*8]] + '> <@' + player_tags[r4_teams[i*8+1]] + '> <@' +
        player_tags[r4_teams[i*8+2]] + '> <@' + player_tags[r4_teams[i*8+3]] + ">\n# против\n<@" +
        player_tags[r4_teams[i*8+4]] + '> <@' + player_tags[r4_teams[i*8+5]] + '> <@' +
        player_tags[r4_teams[i*8+6]] + '> <@' + player_tags[r4_teams[i*8+7]] + '>',
        file=discord.File(f'images/Requests/result{i}.png'))
            #Лузера
        f = open('r4_losers.txt')
        r4_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r4_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r4_teams)
        with open('r4_losers.txt', 'w') as f:
            for line in r4_teams:
                f.write("%s\n" % line)
        for i in range(2):
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            edit(img, 'r4_losers.txt', 8 * i, i + 12, 0, 2)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            await ctx.send('<@' + player_tags[r4_teams[i * 8]] + '> <@' + player_tags[r4_teams[i * 8 + 1]] + '> <@' +
                       player_tags[r4_teams[i * 8 + 2]] + '> <@' + player_tags[
                           r4_teams[i * 8 + 3]] + ">\n# против\n<@" +
                       player_tags[r4_teams[i * 8 + 4]] + '> <@' + player_tags[r4_teams[i * 8 + 5]] + '> <@' +
                       player_tags[r4_teams[i * 8 + 6]] + '> <@' + player_tags[r4_teams[i * 8 + 7]] + '>',
                       file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r5s(ctx):
    if str(ctx.author) == 'dain_play#0':
        games = [0]
        with open('r5_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
            #Лузера
        f = open('r5_losers.txt')
        r5_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r5_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r5_teams)
        with open('r5_losers.txt', 'w') as f:
            for line in r5_teams:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'r5_losers.txt', 8 * i, i + 14, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[r5_teams[i * 8]] + '> <@' + player_tags[r5_teams[i * 8 + 1]] + '> <@' +
                   player_tags[r5_teams[i * 8 + 2]] + '> <@' + player_tags[
                       r5_teams[i * 8 + 3]] + ">\n# против\n<@" +
                   player_tags[r5_teams[i * 8 + 4]] + '> <@' + player_tags[r5_teams[i * 8 + 5]] + '> <@' +
                   player_tags[r5_teams[i * 8 + 6]] + '> <@' + player_tags[r5_teams[i * 8 + 7]] + '>',
                   file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r6s(ctx):
    if str(ctx.author) == 'dain_play#0':
        games = [0]
        with open('r6_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
            #Лузера
        f = open('r6_losers.txt')
        r6_teams = []
        for line in f.readlines():
            fields = line.split('\n')
            r6_teams.append(int(fields[0]))
        f.close()
        random.shuffle(r6_teams)
        with open('r6_losers.txt', 'w') as f:
            for line in r6_teams:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'r6_losers.txt', 8 * i, i + 15, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[r6_teams[i * 8]] + '> <@' + player_tags[r6_teams[i * 8 + 1]] + '> <@' +
                   player_tags[r6_teams[i * 8 + 2]] + '> <@' + player_tags[
                       r6_teams[i * 8 + 3]] + ">\n# против\n<@" +
                   player_tags[r6_teams[i * 8 + 4]] + '> <@' + player_tags[r6_teams[i * 8 + 5]] + '> <@' +
                   player_tags[r6_teams[i * 8 + 6]] + '> <@' + player_tags[r6_teams[i * 8 + 7]] + '>',
                   file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r7s(ctx):
    if str(ctx.author) == 'dain_play#0':
        games = [0]
        with open('final_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
            #Лузера
        f = open('final_teams.txt')
        final_losers = []
        for line in f.readlines():
            fields = line.split('\n')
            final_losers.append(int(fields[0]))
        f.close()
        g = open('final_losers.txt')
        for line in g.readlines():
            fields = line.split('\n')
            final_losers.append(int(fields[0]))
        g.close()
        with open('final_losers.txt', 'w') as f:
            for line in final_losers:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'final_losers.txt', 8 * i, i + 16, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[final_losers[i * 8]] + '> <@' + player_tags[final_losers[i * 8 + 1]] + '> <@' +
                   player_tags[final_losers[i * 8 + 2]] + '> <@' + player_tags[
                       final_losers[i * 8 + 3]] + ">\n# против\n<@" +
                   player_tags[final_losers[i * 8 + 4]] + '> <@' + player_tags[final_losers[i * 8 + 5]] + '> <@' +
                   player_tags[final_losers[i * 8 + 6]] + '> <@' + player_tags[final_losers[i * 8 + 7]] + '>',
                   file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r8s(ctx):
    if str(ctx.author) == 'dain_play#0':
        games = [0]
        with open('final_games.txt', 'w') as f:
            for line in games:
                f.write("%s\n" % line)
            #Лузера
        f = open('final_teams.txt')
        final_losers = []
        for line in f.readlines():
            fields = line.split('\n')
            final_losers.append(int(fields[0]))
        f.close()
        g = open('final_losers.txt')
        for line in g.readlines():
            fields = line.split('\n')
            final_losers.append(int(fields[0]))
        g.close()
        random.shuffle(final_losers)
        with open('final_losers.txt', 'w') as f:
            for line in final_losers:
                f.write("%s\n" % line)
        i=0
        img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
        edit(img, 'final_losers.txt', 8 * i, i + 17, 0, 2)
        img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
        await ctx.send('<@' + player_tags[final_losers[i * 8]] + '> <@' + player_tags[final_losers[i * 8 + 1]] + '> <@' +
                   player_tags[final_losers[i * 8 + 2]] + '> <@' + player_tags[
                       final_losers[i * 8 + 3]] + ">\n# против\n<@" +
                   player_tags[final_losers[i * 8 + 4]] + '> <@' + player_tags[final_losers[i * 8 + 5]] + '> <@' +
                   player_tags[final_losers[i * 8 + 6]] + '> <@' + player_tags[final_losers[i * 8 + 7]] + '>',
                   file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r1c1(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r1_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        if games[0] < 3:
            games[0] = games[0]+1
            with open('r1_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            i=0
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[0], 0)
            else:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[0], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r1_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1c2(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r1_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        if games[1] < 3:
            games[1] = games[1]+1
            with open('r1_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            i=1
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 0)
            else:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r1_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1c3(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r1_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        if games[2] < 3:
            games[2] = games[2]+1
            with open('r1_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            i=2
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 0)
            else:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r1_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1c4(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r1_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        if games[3] < 3:
            games[3] = games[3]+1
            with open('r1_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            i=3
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 0)
            else:
                edit(img, 'r1_teams.txt', 8*i, i+1, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r1_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r2c5(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r2_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r2_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r2_teams.txt', 8*i, i+5, games[i], 0)
            else:
                edit(img, 'r2_teams.txt', 8*i, i+5, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r2_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2c6(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r2_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=1 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r2_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r2_teams.txt', 8*i, i+5, games[i], 0)
            else:
                edit(img, 'r2_teams.txt', 8*i, i+5, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r2_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2c7(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r2_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=2 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r2_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r2_losers.txt', 0, i+5, games[i], 0)
            else:
                edit(img, 'r2_losers.txt', 0, i+5, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r2_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            i=0
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result2.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r3c8(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r3_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r3_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r3_teams.txt', 8*i, i+8, games[i], 0)
            else:
                edit(img, 'r3_teams.txt', 8*i, i+8, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r3_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3c9(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r3_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=1 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r3_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r3_losers.txt', 0, i+8, games[i], 0)
            else:
                edit(img, 'r3_losers.txt', 0, i+8, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r3_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            i=0
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result1.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3c10(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r3_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=2 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r3_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r3_losers.txt', 8, i+8, games[i], 0)
            else:
                edit(img, 'r3_losers.txt', 8, i+8, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r3_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            i=1
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result2.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r4c11(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r4_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 5:
            games[i] = games[i]+1
            with open('r4_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 5:
                edit(img, 'r4_teams.txt', 8*i, i+11, games[i], 0)
            else:
                edit(img, 'r4_teams.txt', 8*i, i+11, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r4_teams.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result{i}.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4c12(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r4_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=1 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r4_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r4_losers.txt', 0, i+11, games[i], 0)
            else:
                edit(img, 'r4_losers.txt', 0, i+11, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r4_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            i=0
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result1.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4c13(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r4_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=2 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r4_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r4_losers.txt', 8, i+11, games[i], 0)
            else:
                edit(img, 'r4_losers.txt', 8, i+11, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r4_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            i=1
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result2.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r5c14(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r5_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 3:
            games[i] = games[i]+1
            with open('r5_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 3:
                edit(img, 'r5_losers.txt', 0, i+14, games[i], 0)
            else:
                edit(img, 'r5_losers.txt', 0, i+14, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r5_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result0.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r6c15(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('r6_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 5:
            games[i] = games[i]+1
            with open('r6_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 5:
                edit(img, 'r6_losers.txt', 0, i+15, games[i], 0)
            else:
                edit(img, 'r6_losers.txt', 0, i+15, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('r6_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result0.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r7c16(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('final_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 5:
            games[i] = games[i]+1
            with open('final_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 5:
                edit(img, 'final_losers.txt', 0, i+16, games[i], 0)
            else:
                edit(img, 'final_losers.txt', 0, i+16, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('final_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result0.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r8c17(ctx):
    if str(ctx.author) == 'dain_play#0':
        g = open('final_games.txt')
        games = []
        for line in g.readlines():
            fields = line.split('\n')
            games.append(int(fields[0]))
        g.close()
        i=0 # Игра-1
        if games[i] < 5:
            games[i] = games[i]+1
            with open('final_games.txt', 'w') as f:
                for line in games:
                    f.write("%s\n" % line)
            img = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/back.png')
            if games[i] == 5:
                edit(img, 'final_losers.txt', 0, i+17, games[i], 0)
            else:
                edit(img, 'final_losers.txt', 0, i+17, games[i], 1)
            img.save(f'C:/Users/Даниил/PycharmProjects/TWR/images/Requests/result{i}.png')
            f = open('final_losers.txt')
            data = []
            for line in f.readlines():
                fields = line.split('\n')
                data.append(int(fields[0]))
            f.close()
            await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
            player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# против\n<@" +
            player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
            player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + '>',
            file=discord.File(f'images/Requests/result0.png'))
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r1f1_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r2_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f1_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r2_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f2_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r2_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f2_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r2_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f3_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=2 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f3_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=2 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r2_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f4_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=3 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r3_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r1f4_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=3 #Матч-1
        f = open('r1_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r1_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r1_teams.txt', 'r') as f, open('r3_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r2f5_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r2_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_teams.txt', 'r') as f, open('r3_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r2_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2f5_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r2_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_teams.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r2_teams.txt', 'r') as f, open('r3_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2f6_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r2_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_teams.txt', 'r') as f, open('r4_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r2_teams.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2f6_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r2_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_teams.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        with open('r2_teams.txt', 'r') as f, open('r4_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2f7_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r2_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_losers.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r2f7_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r2_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r2_losers.txt', 'r') as f, open('r3_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r3f8_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r3_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_teams.txt', 'r') as f, open('r4_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r3_teams.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3f8_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r3_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_teams.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r3_teams.txt', 'r') as f, open('r4_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3f9_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r3_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_losers.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3f9_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r3_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_losers.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3f10_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r3_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_losers.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r3f10_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r3_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r3_losers.txt', 'r') as f, open('r4_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r4f11_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r4_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_teams.txt', 'r') as f, open('final_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r4_teams.txt', 'r') as f, open('r6_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4f11_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r4_teams.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_teams.txt', 'r') as f, open('r6_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i:
                    if line_number <= i+4:
                        s.write(line_)
        with open('r4_teams.txt', 'r') as f, open('final_teams.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i+5:
                    if line_number < i+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4f12_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r4_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_losers.txt', 'r') as f, open('r5_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4f12_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r4_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_losers.txt', 'r') as f, open('r5_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4f13_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r4_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_losers.txt', 'r') as f, open('r5_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r4f13_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=1 #Матч-1
        f = open('r4_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r4_losers.txt', 'r') as f, open('r5_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r5f14_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r5_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r5_losers.txt', 'r') as f, open('r6_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r5f14_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r5_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r5_losers.txt', 'r') as f, open('r6_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')

@bot.command()
async def r6f15_1(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r6_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r6_losers.txt', 'r') as f, open('final_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+1:
                    if line_number <= i*8+4:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8]] + '> <@' + player_tags[data[i*8+1]] + '> <@' +
        player_tags[data[i*8+2]] + '> <@' + player_tags[data[i*8+3]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')
@bot.command()
async def r6f15_2(ctx):
    if str(ctx.author) == 'dain_play#0':
        i=0 #Матч-1
        f = open('r6_losers.txt')
        data = []
        for line in f.readlines():
            fields = line.split('\n')
            data.append(int(fields[0]))
        f.close()
        with open('r6_losers.txt', 'r') as f, open('final_losers.txt', 'a') as s:
            for line_number, line_ in enumerate(f, 1):
                if line_number >= i*8+5:
                    if line_number < i*8+9:
                        s.write(line_)
        await ctx.send('<@' + player_tags[data[i*8+4]] + '> <@' + player_tags[data[i*8+5]] + '> <@' +
        player_tags[data[i*8+6]] + '> <@' + player_tags[data[i*8+7]] + ">\n# победили!")
    else:
        await ctx.send('У нас не было времени делать бота user-friendly, так что во избежание поломок, эту команду могут испольльзовать только те, кто шарит. К сожалению, ты не шаришь. Мне жаль.')



@bot.command()
async def reroll(ctx):
    await ctx.reply(file=discord.File(get_weapon()))

def edit(img, filename, startline, match, game, turfs=1):
    draw_weapons(img)
    draw_maps(img, turfs)
    draw_title(img, match, game)
    draw_teams(img, filename, startline)

def get_weapon():
    x = random.randint(1, 90)
    return "C:/Users/Даниил/PycharmProjects/TWR/images/Weapons/{0}.png".format(x)


def draw_weapons(img):
    w1 = Image.open(get_weapon())
    w2 = Image.open(get_weapon())
    w3 = Image.open(get_weapon())
    w4 = Image.open(get_weapon())
    w5 = Image.open(get_weapon())
    w6 = Image.open(get_weapon())
    w7 = Image.open(get_weapon())
    w8 = Image.open(get_weapon())
    img.paste(w1, (-11, 150), w1)
    img.paste(w2, (649, 150), w2)
    img.paste(w3, (1309, 150), w3)
    img.paste(w4, (1969, 150), w4)
    img.paste(w5, (1309, 1878), w5)
    img.paste(w6, (1969, 1878), w6)
    img.paste(w7, (2629, 1878), w7)
    img.paste(w8, (3289, 1878), w8)


def draw_maps(img, turfs):
    if turfs == 1:
        x = random.randint(1, 5)
        y = random.randint(1, 18)
        stage = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Stages/{0}.png'.format(y))
        img.paste(stage, (38, 2085), stage)
        mode = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Modes/{0}.png'.format(x))
        img.paste(mode, (0, 1669), mode)
    elif turfs == 2:
        x = 1
        y = random.randint(1, 18)
        stage = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Stages/{0}.png'.format(y))
        img.paste(stage, (38, 2085), stage)
        mode = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Modes/{0}.png'.format(x))
        img.paste(mode, (0, 1669), mode)
    elif turfs == 0:
        x = random.randint(2, 5)
        y = random.randint(1, 18)
        stage = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Stages/{0}.png'.format(y))
        img.paste(stage, (38, 2085), stage)
        mode = Image.open('C:/Users/Даниил/PycharmProjects/TWR/images/Modes/{0}.png'.format(x))
        img.paste(mode, (0, 1669), mode)


def draw_title(img, match, game):
    fontS = ImageFont.truetype('C:/Users/Даниил/PycharmProjects/TWR/fonts/splatfont.otf', size=160)
    fontM = ImageFont.truetype('C:/Users/Даниил/PycharmProjects/TWR/fonts/splatfont.otf', size=320)
    draw_text = ImageDraw.Draw(img)
    if (match == 16):
        draw_text.text(
            (1227 + 1180-draw_text.textlength(f'Финал', font=fontM), 1105),
            f'Финал',
            font=fontM,
            fill='#161616')
    elif (match == 17):
        draw_text.text(
            (1227 + 1180-draw_text.textlength(f'Финал', font=fontM), 1105),
            f'Финал',
            font=fontM,
            fill='#161616')
        draw_text.text(
            (2493 + 1300-draw_text.textlength(f'Брекет ресет!', font=fontS), 1091),
            f'Брекет ресет!',
            font=fontS,
            fill='#FFFFFF')
    else:
        draw_text.text(
            (1307 + 1180-draw_text.textlength(f'Матч {match}', font=fontM), 1105),
            f'Матч {match}',
            font=fontM,
            fill='#161616')
    if (game == 0):
        draw_text.text(
            (1515 + 1180 - draw_text.textlength('Разминка', font=fontM), 1395),
            f'Разминка',
            font=fontM,
            fill='#161616')
    else:
        draw_text.text(
            (1257 + 1180 - draw_text.textlength(f'Игра {game}', font=fontM), 1395),
            f'Игра {game}',
            font=fontM,
            fill='#161616')


def draw_teams(img, filename, startline):
    f = open(filename)
    data = []
    for line in f.readlines():
        fields =line.split('\n')
        data.append(int(fields[0]))
    f.close()

    W = 604
    fontP = ImageFont.truetype('C:/Users/Даниил/PycharmProjects/TWR/fonts/Splatfont2.ttf', size=112)
    draw_text = ImageDraw.Draw(img)
    w = draw_text.textlength(player_names[data[0+startline]], font=fontP)
    draw_text.text(
        (-11 + ((W - w) / 2), 917),
        player_names[data[0+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[1+startline]], font=fontP)
    draw_text.text(
        (649 + ((W - w) / 2), 917),
        player_names[data[1+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[2+startline]], font=fontP)
    draw_text.text(
        (1309 + ((W - w) / 2), 917),
        player_names[data[2+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[3+startline]], font=fontP)
    draw_text.text(
        (1969 + ((W - w) / 2), 917),
        player_names[data[3+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[4+startline]], font=fontP)
    draw_text.text(
        (1309 + ((W - w) / 2), 2645),
        player_names[data[4+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[5+startline]], font=fontP)
    draw_text.text(
        (1969 + ((W - w) / 2), 2645),
        player_names[data[5+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[6+startline]], font=fontP)
    draw_text.text(
        (2629 + ((W - w) / 2), 2645),
        player_names[data[6+startline]],
        font=fontP,
        fill='#ffffff')
    w = draw_text.textlength(player_names[data[7+startline]], font=fontP)
    draw_text.text(
        (3289 + ((W - w) / 2), 2645),
        player_names[data[7+startline]],
        font=fontP,
        fill='#ffffff')


#@bot.command()
#async def rwt(ctx):
#    # await ctx.send(ctx.author)
#    flag = False
#    for i in range(len(teams)):
#        if flag:
#            break
#        for j in teams[i].players:
#            if j == str(ctx.author):
#                flag = True
#                im = Image.open('C:/Users/teras/PycharmProjects/TWR/images/bot_background.png')
#                edit(im, i)
#                im.save('C:/Users/teras/PycharmProjects/TWR/images/Requests/result.png')
#                await ctx.send(teams[i].roleid, file=discord.File('images/Requests/result.png'))
#                break
#    if not flag:
#        await ctx.send("Бот пока что ещё только в разработке!")
    # if str(ctx.author) == 'munaat#3923':
    #    await ctx.send(file=discord.File('images/maid.jpg'))
    # elif str(ctx.author) == 'Dain_PLay#4851':
    #    await ctx.send(file=discord.File('images/rock.jpg'))


bot.run(TOKEN)
