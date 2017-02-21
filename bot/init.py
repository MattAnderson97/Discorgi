from .commands import HelpCommand, HelloCommand, RollCommand, PinCommand, UnpinCommand
from . import CommandTools


def register_commands(client):
    CommandTools.add_command(HelpCommand.HelpCmd(command="help", usage="help", client=client, aliases=["helpme"]))
    CommandTools.add_command(RollCommand.RollCmd(command="roll", usage="roll <rolls> <sides>", client=client, aliases=["dice"]))
    CommandTools.add_command(HelloCommand.HelloCmd(command="hello", usage="hello", client=client, aliases=["hi", "hey"]))
    CommandTools.add_command(PinCommand.PinCmd(command="pin", usage="pin <message id>", client=client, aliases=[]))
    CommandTools.add_command(UnpinCommand.UnpinCmd(command="unpin", usage="unpin <message id>", client=client, aliases=[]))

