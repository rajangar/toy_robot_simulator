from command import *
from errors import CommandNotValidError


class CommandType:
    """
    To classify the commands
    """
    def __init__(self):
        self.class_type = {
            "PLACE": PlaceCommand,
            "MOVE": MoveCommand,
            "LEFT": LeftCommand,
            "RIGHT": RightCommand,
            "REPORT": ReportCommand
        }

    def parse(self, line):
        """
        Search the command from class_type dictionary and return object
        :param line: Line contains the command
        :return: Object of classified Command class
        """
        words = line.split()
        command_class = self.class_type.get(words[0], None)

        if not command_class:
            raise CommandNotValidError("Not a valid command")

        return command_class(','.join(words[1:]))
