from ..Command import Command
from ..CommandTools import COMMANDS


class HelpCmd(Command):

    def __init__(self, command, client=None, for_message=None, usage=None, aliases=[], **kwargs):
        super().__init__(command=command, client=client, for_message=for_message, usage=usage, aliases=aliases, **kwargs)

    async def execute(self, client, channel, command, sender):
        for loop_command in COMMANDS:
            await client.send_message(channel, loop_command.get_usage())
