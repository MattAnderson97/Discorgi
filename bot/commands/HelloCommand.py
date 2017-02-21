from ..Command import Command


class HelloCmd(Command):

    def __init__(self, command, client=None, for_message=None, usage=None, aliases=[], **kwargs):
        super().__init__(command=command, client=client, for_message=for_message, usage=usage, aliases=aliases, **kwargs)

    async def execute(self, client, channel, command, sent_message, sender):
        await client.send_message(channel, "Hi, {0}!".format(sender.mention))
