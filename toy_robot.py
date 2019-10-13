from table import Table
from constants import *
from errors import *


class ToyRobot:
    """
    Actual ToyRobot which stores the current position, direction and provide all its movements
    """
    def __init__(self):
        """
        Initialize position and direction from none, so that if it is None before place command,
        then exception can be raised
        """
        self._x_coordinate = None
        self._y_coordinate = None
        self._direction = None

    @property
    def x_coordinate(self):
        """
        Getter for x coordinate
        :return: x coordinate
        """
        if self._x_coordinate is None:
            raise NoPlaceInitiatedError("Place is not initiated yet")
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x):
        """
        Setter for x coordinate
        :param x: x
        :return: No
        """
        if not Table.is_valid_horizontal_position(x):
            raise NotValidPositionError("X coordinate is not valid on the table")

        self._x_coordinate = x

    @property
    def y_coordinate(self):
        """
        Getter for y coordinate
        :return: y coordinate
        """
        if self._y_coordinate is None:
            raise NoPlaceInitiatedError("Place is not initiated yet")
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y):
        """
        setter for y coordinate
        :param y: y
        :return: No
        """
        if not Table.is_valid_vertical_position(y):
            raise NotValidPositionError("Y coordinate is not valid on the table")

        self._y_coordinate = y

    @property
    def direction(self):
        """
        Getter for direction
        :return: direction
        """
        if self._direction is None:
            raise NoPlaceInitiatedError("Place is not initiated yet")
        return self._direction

    @direction.setter
    def direction(self, dir):
        """
        setter for direction
        :param dir: direction
        :return: No
        """
        if not Table.is_valid_direction(dir):
            raise NotValidDirectionError("Direction is not valid")

        self._direction = dir

    def place(self, x, y, direction):
        """
        Run the place command by storing the position and direction
        :param x: x
        :param y: y
        :param direction: direction
        :return: No
        """
        self.x_coordinate = x
        self.y_coordinate = y
        self.direction = direction

    def move_one_position(self):
        """
        Move one position on the base of direction
        :return: No
        """
        if self.direction == 'NORTH':
            self.y_coordinate += 1
        elif self.direction == 'SOUTH':
            self.y_coordinate -= 1
        elif self.direction == 'WEST':
            self.x_coordinate -= 1
        elif self.direction == 'EAST':
            self.x_coordinate += 1

    def turn_left(self):
        """
        Turn left by just subtracting 1 from the DIRECTION index
        :return: No
        """
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index - 1) % 4]

    def turn_right(self):
        """
        Turn right by just adding 1 to the DIRECTION index
        :return: No
        """
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index + 1) % 4]

    def report(self):
        """
        REPORT command
        :return: Return the current position and direction in list format
        """
        return [self.x_coordinate, self.y_coordinate, self.direction]