import asyncio
from abc import ABC, abstractmethod
from config import settings


class Command:  # class command(abc):

    for_message = None
    client = None

    def __init__(self, command, client, for_message=None, usage=None, aliases=[], **kwargs):
        self.command = settings.PREFIX + command
        self.usage = settings.PREFIX + usage
        self.for_message = for_message

        self.aliases = []
        for alias in aliases:
            self.aliases.append(settings.PREFIX + alias)

    @property
    def message(self):
        return self.for_message

    @asyncio.coroutine
    def send_typing(self, dest=None):
        yield from self.client.send_typing(dest or self.for_message.channel)

    @asyncio.coroutine
    def reply(self, text):
        channel = self.for_message.channel
        yield from self.client.send_message(channel, text)

    def get_usage(self):
        return self.command + " - _" + (self.usage or ' ') + "_" + "\n    Aliases: **" + ", ".join(self.aliases) + "**"

    @abstractmethod
    async def execute(self, client, channel, command, sender):
        pass
