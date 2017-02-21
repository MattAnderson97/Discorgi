import discord
from bot import init, CommandTools
from config import settings

client = discord.Client()


@client.event
async def on_ready():
    print("bot logged in")


@client.event
async def on_message(message):
    msg = message.content.lower()
    channel = message.channel
    if not message.author.bot:
        for command in CommandTools.COMMANDS:
            if command.command.lower() == msg.split(" ")[0] or msg.split(" ")[0] in command.aliases:
                print("Executing command: " + msg.split(" ")[0])
                await command.execute(client, channel, msg, message.author)
                break


if __name__ == "__main__":
    init.register_commands(client)
    client.run(settings.TOKEN)
