from toy_robot import ToyRobot
from command_type import CommandType
from errors import *


class RobotSimulator:
    """ Provide Robot simulation through commands
    """
    def __init__(self):
        """
        Pick a ToyRobot object and CommandType (which provide classification of command)
        """
        self.robot = ToyRobot()
        self.cmd_type = CommandType()

    def simulate(self, lines):
        """
        Find out the command type and run on the ToyRobot object
        :param lines: lines could be a generator type or list, which contain all the commands
        :return: Returns result list, produced by REPORT commands
        """
        reports = []
        for line in lines:
            try:
                # Find out the command_type object by parsing the line
                command_type = self.cmd_type.parse(line)
                # run the actual command on ToyRobot and append the result in reports list
                command_type.run(self.robot, reports)
            except UserDefinedError as e:
                # UserDefinedError has different errors, which caught here to skip only invalid line
                print("Command {} skipped, {}".format(line, e))
            except ValueError as e:
                print("Command {} skipped, {}".format(line, e))

        return reports
