from ..Command import Command
from discord.errors import HTTPException

import re


class PinCmd(Command):
    def __init__(self, command, client=None, for_message=None, usage=None, aliases=[], **kwargs):
        super().__init__(command=command, client=client, for_message=for_message, usage=usage, aliases=aliases, **kwargs)

    async def execute(self, client, channel, command, sender):
        if len(command.split(" ")) < 2:
            await client.send_message(channel, "Not enough arguments! _usage: " + self.usage + "_")
            return

        if command.startswith(self.command.lower()):
            message_id = command.replace(self.command.lower() + " ", "").split(" ")[0]
        else:
            for cmd in self.aliases:
                if cmd.startswith(cmd.lower()):
                    message_id = command.replace(cmd.lower() + " ", "").split(" ")[0]
                    break

        pattern = r'^[0-9]+$'
        match = re.search(pattern, message_id)

        if match:
            try:
                message = await client.get_message(channel, message_id)
                await client.pin_message(message)
            except HTTPException:
                await client.send_message(channel, "Invalid ID: message not found")
        else:
            await client.send_message(channel, "malformed message ID in command: //pin")
