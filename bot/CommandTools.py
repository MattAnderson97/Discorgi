from .Command import Command
from utils import Out

COMMANDS = []


def add_command(command):
    if isinstance(command, Command):
        COMMANDS.append(command)
    else:
        Out.error("Command not valid type").output_message()


def del_command(command):
    if isinstance(command, Command):
        if command in COMMANDS:
            COMMANDS.remove(command)
        else:
            Out.error("Command not found").output_message()
    else:
        Out.error("Command not valid type").output_message()