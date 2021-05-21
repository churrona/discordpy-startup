# Discord.pyのライブラリを読み込む。必須。
import discord
from discord.ext import tasks
import datetime
import os
import traceback

# Bot自身のデータをclientに格納する。
# 必須では無いが後々使えるので入れておくが吉。
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


# @client.event
# async def on_ready():
# Botが起動した際に1回だけ走る。
# 起動時のメッセージ等表示させたい場合はココに仕込む

# @client.event
# async def on_reaction_add(reaction, user):
# 自分の送信したメッセージに対してリアクションが付く度に走る。
# 新規ユーザーに対して、サーバー規約の同意を求めるためにリアクションを使用する際に使える。
# Botとの意思疎通(YES,NOクエスチョン)などでリアクションを使用するのにも使える。

# @client.event
# async def on_message(message):
# 誰かがメッセージを発言する度に走る。これが無いとBotが始まらない。
# 特定のメッセージを受けたら〇〇をするためにに使う。

@tasks.loop(seconds=60)
async def timeloop():
    print(str(datetime.datetime.now().hour) + "時" + str(datetime.datetime.now().minute) + "分")
    if datetime.datetime.now().hour == 16 and datetime.datetime.now().minute == 14:
        # 時報
        # 任意のチャンネルIDを記述
        ch_id = 575801338617921546
        # 入力されたチャンネルIDからチャンネル情報を取得してchannelに格納する。
        channel = client.get_channel(ch_id)
        # channelに指定されたワードをポストする。
        await channel.send("アイテムのリクエストが済んだぞ。またお腹が空いた。")
    return


# 無くても動く。seconds=60により60secに1回走る。
# timeloopは別の名前に変えてもOK。
# 定時で喋る時報とか実装するのに使える。

# 上記で作成したtimeloop(仮名)を動かし始めるのに必要。使わない場合は要らない。
timeloop.start()

# Discord Developer Portalで取得したTOKENを記述しておく。必須。
client.run(token)
