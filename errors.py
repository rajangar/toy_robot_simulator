"""
All User Defined exceptions to skip the invalid commands
"""


class UserDefinedError(Exception):
    pass


class CommandNotValidError(UserDefinedError):
    pass


class NoPlaceInitiatedError(UserDefinedError):
    pass


class NotValidPositionError(UserDefinedError):
    pass


class NotValidDirectionError(UserDefinedError):
    pass
