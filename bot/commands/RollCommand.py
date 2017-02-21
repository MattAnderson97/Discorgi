from ..Command import Command
import random


class RollCmd(Command):

    def __init__(self, command, client=None, for_message=None, usage=None, aliases=[], **kwargs):
        super().__init__(command=command, client=client, for_message=for_message, usage=usage, aliases=aliases, **kwargs)

    async def execute(self, client, channel, command, sender):
        if len(command.split(" ")) < 3:
            await client.send_message(channel, "Not enough arguments! _usage: " + self.usage + "_")
            return

        if command.startswith(self.command.lower()):
            args = command.replace(self.command.lower() + " ", "").split(" ")
        else:
            for cmd in self.aliases:
                if command.startswith(cmd.lower()):
                    args = command.replace(cmd.lower() + " ", "").split(" ")
                    break

        try:
            rolls = int(args[0])
            sides = int(args[1])
        except ValueError:
            await client.send_message(channel, "Invalid arguments! must be integers, _usage: " + self.usage + "_")
            return

        if rolls < 1:
            await client.send_message(channel, "Amount of rolls too small - must be between 1 and 10 rolls.")
            return

        if rolls > 10:
            await client.send_message(channel, "Amount of rolls too high - must be between 1 and 10 rolls.")
            return

        if sides < 3:
            await client.send_message(channel, "Amount of sides too small - must be at least 3 sides")
            return

        msg = ""

        for count in range(rolls):
            msg += "roll {0}: ".format(count+1) + str(random.randint(1, sides)) + "\n"

        await client.send_message(channel, msg)
