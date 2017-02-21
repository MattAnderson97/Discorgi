from ..Command import Command
from ..CommandTools import COMMANDS


class HelpCmd(Command):

    def __init__(self, command, client=None, for_message=None, usage=None, aliases=[], **kwargs):
        super().__init__(command=command, client=client, for_message=for_message, usage=usage, aliases=aliases, **kwargs)

    async def execute(self, client, channel, command, sent_message, sender):
        help_message = ""
        
        for loop_command in COMMANDS:
            help_message += loop_command.get_usage() + "\n"

        await client.send_message(channel, help_message)
