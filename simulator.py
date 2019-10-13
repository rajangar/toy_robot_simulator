VALID_CMDS = ['PLACE',
              'MOVE',
              'LEFT',
              'RIGHT',
              'REPORT']

VALID_DIRECTIONS = ['NORTH',
                    'WEST',
                    'SOUTH',
                    'EAST']


class RobotSimulator:
    """ Provide Robot simulation through commands
    """

    def __init__(self):
        self.cur_pos = [0, 0, VALID_DIRECTIONS[0]]
        self.output = []

        # self.commands_file = commands_file
        # self.cur_pos = [0, 0, VALID_DIRECTIONS[0]]
        # self.output = []

    def simulate(self, commands):
        """ Simulate the commmands from the file
        And validate if file contain the correct commands
        """

        first_cmd_registered = False
        try:
            for cmd in commands:
                if self.is_valid_cmd(cmd):
                    self.cur_cmd = cmd.rstrip()
                    if not first_cmd_registered:
                        if cmd.split()[0] == VALID_CMDS[0]:
                            first_cmd_registered = True
                        else:
                            print("Command:", self.cur_cmd, "is skipped, as come before valid PLACE command")
                            continue
                    self.run_cmd(cmd)
                else:
                    print("Command:", cmd.rstrip(), "is not a valid command")
        except FileNotFoundError as e:
            print(self.commands_file, "not present, error = ", e)

        return self.output

    def run_cmd(self, command):
        """ Here actual commands are running
        """
        cmd = command.split()[0]
        if cmd == 'PLACE':
            strs = command.split()[1].split(',')
            self.place(strs[0], strs[1], strs[2])
        else:
            getattr(self, cmd.lower())()

    def place(self, row, col, direction):
        """ Place the robot on mentioned place
        """
        self.cur_pos = [int(row), int(col), direction]

    def move(self):
        """ Move the robot one position in the direction it is facing
        OR skip it, if chance of falling down
        """
        if self.cur_pos[2] == 'NORTH':
            self.cur_pos[1] = self.add_one_or_not(self.cur_pos[1])
        elif self.cur_pos[2] == 'SOUTH':
            self.cur_pos[1] = self.minus_one_or_not(self.cur_pos[1])
        elif self.cur_pos[2] == 'WEST':
            self.cur_pos[0] = self.minus_one_or_not(self.cur_pos[0])
        elif self.cur_pos[2] == 'EAST':
            self.cur_pos[0] = self.add_one_or_not(self.cur_pos[0])

    def left(self):
        """ Change the facing of Robot to turn left
        """
        ind = VALID_DIRECTIONS.index(self.cur_pos[2])
        self.cur_pos[2] = VALID_DIRECTIONS[(ind + 1) % 4]

    def right(self):
        """ Change the facing of Robot to turn right
        """
        ind = VALID_DIRECTIONS.index(self.cur_pos[2])
        self.cur_pos[2] = VALID_DIRECTIONS[(ind - 1) % 4]

    def report(self):
        """ Report the current position and facing of Robot to stdout
        And also in output to return back
        """
        print("REPORT:", self.cur_pos)
        self.output.append(self.cur_pos)

    def add_one_or_not(self, val):
        """ Check if it is a valid add to column or row
        """
        if val + 1 > 4:
            print("Command:", self.cur_cmd, "will skip, Robot will fall down")
            return val
        return val + 1

    def minus_one_or_not(self, val):
        """ Check if it is a valid minus to column or row
        """
        if val - 1 < 0:
            print("Command:", self.cur_cmd, "will skip, Robot will fall down")
            return val
        return val - 1

    @staticmethod
    def is_valid_cmd(command):
        """ Check if the command is valid or not as a static method
        """
        if command.strip() in VALID_CMDS[1:]:
            return True

        cmd_str_list = command.split()
        if len(cmd_str_list) == 2 and cmd_str_list[0] == VALID_CMDS[0]:
            if RobotSimulator.is_valid_place(cmd_str_list[1]):
                return True
            else:
                print("Command:", command.rstrip(), "is not a valid PLACE command")

        return False

    @staticmethod
    def is_valid_place(cmd_str):
        """ Check if place command is valid or not
        """
        cmd_strs = cmd_str.split(',')
        if len(cmd_strs) == 3:
            for x in cmd_strs[:2]:
                if int(x) not in range(5):
                    return False
            if cmd_strs[2].strip() in VALID_DIRECTIONS:
                return True

        return False
