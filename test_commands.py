import pytest
from command import *
from toy_robot import ToyRobot


class TestCommands:

    def test_move_command(self):
        """ Test move command
        """
        robot = ToyRobot()
        robot.place(0, 0, 'NORTH')
        MoveCommand("").run(robot)
        assert robot.report() == [0, 1, 'NORTH']

    def test_place_command(self):
        """ Test place command
        """
        robot = ToyRobot()
        robot.place(0, 0, 'NORTH')
        assert robot.report() == [0, 0, 'NORTH']

    def test_report_command(self):
        """ Test report command
        """
        robot = ToyRobot()
        robot.place(0, 0, 'NORTH')
        assert robot.report() == [0, 0, 'NORTH']

    def test_left_command(self):
        """ Test left command
        """
        robot = ToyRobot()
        robot.place(0, 0, 'NORTH')
        LeftCommand("").run(robot)
        assert robot.report() == [0, 0, 'WEST']

    def test_right_command(self):
        """ Test right command
        """
        robot = ToyRobot()
        robot.place(0, 0, 'NORTH')
        RightCommand("").run(robot)
        assert robot.report() == [0, 0, 'EAST']
