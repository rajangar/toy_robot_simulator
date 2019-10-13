from constants import *


class Table:
    """
    Table provide the dimensions of tabletop and validate the positions
    """
    @staticmethod
    def is_valid_horizontal_position(x):
        """
        Find out the valid horizontal position
        :param x: x coordinate
        :return: True, if valid or False
        """
        if x not in range(HORIZONTAL_SIZE):
            return False

        return True

    @staticmethod
    def is_valid_vertical_position(y):
        """
        Find out the valid vertical position
        :param y: y coordinate
        :return: True, if valid or False
        """
        if y not in range(VERTICAL_SIZE):
            return False

        return True

    @staticmethod
    def is_valid_direction(dir):
        """
        Find out the valid direction
        :param dir: direction
        :return: True, if valid or False
        """
        if dir in DIRECTIONS:
            return True

        return False
