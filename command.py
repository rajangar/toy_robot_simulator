from errors import CommandNotValidError


class Command:
    """
    Base class of all type of commands
    """
    def __init__(self, *args):
        """
        Base init function to find out if arg string is not empty, then skip the command
        Checking for all commands except PLACE
        :param args: remaining string else then command
        """
        if not self.if_arg_string_empty(args[0]):
            raise CommandNotValidError("Command is not valid")

    @staticmethod
    def if_arg_string_empty(string):
        """
        staticmethod to find arg string is empty or not
        :param string: string
        :return: boolean
        """
        if string == "":
            return True

        return False


class PlaceCommand(Command):
    """
    To run PLACE command
    """
    def __init__(self, *args):
        """
        Check if remaining string is empty, then not a valid PLACE command
        And find out all the coordinates from the string
        :param args: contain all coordinates including direction
        """
        if self.if_arg_string_empty(args[0]):
            raise CommandNotValidError("Place command is not valid")

        strings = args[0].split(',')
        self.x = int(strings[0])
        self.y = int(strings[1])
        self.dir = strings[2]

    def run(self, robot, *args):
        """
        run the place command
        :param robot: ToyRobot object
        :param args: Not using
        :return: No return
        """
        robot.place(self.x, self.y, self.dir)


class MoveCommand(Command):
    """
    To run MOVE command
    """
    def __init__(self, *args):
        """
        Call base class init
        :param args: Remaining string
        """
        super().__init__(*args)

    def run(self, robot, *args):
        """
        Run Move command
        :param robot: ToyRobot object
        :param args: Not using
        :return: No
        """
        robot.move_one_position()


class LeftCommand(Command):
    """
    To run LEFT command
    """
    def __init__(self, *args):
        """
        Call base class init
        :param args: Remaining string
        """
        super().__init__(*args)

    def run(self, robot, *args):
        """
        Run Robot's turn_left function
        :param robot: Robot's Object
        :param args: Not using
        :return: No
        """
        robot.turn_left()


class RightCommand(Command):
    """
    To run RIGHT command
    """
    def __init__(self, *args):
        """
        Call base class init
        :param args: Remaining string
        """
        super().__init__(*args)

    def run(self, robot, *args):
        """
        Run Robot's turn_right function
        :param robot: Robot's Object
        :param args: Not using
        :return: No
        """
        robot.turn_right()


class ReportCommand(Command):
    """
    To run REPORT command
    """
    def __init__(self, *args):
        """
        Call base class init
        :param args: Remaining string
        """
        super().__init__(*args)

    def run(self, robot, reports):
        """
        Append robot's report list into end reports
        :param robot: Robot Object
        :param reports: reports list to save
        :return: No return
        """
        reports.append(robot.report())
