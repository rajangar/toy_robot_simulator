import pytest
import os
from toy_simulator.main import Main


class TestRobotSimulator:

    def setup_method(self, method):
        self.cur_path = os.path.dirname(os.path.abspath( __file__ ))

    def test_first_case(self):
        """ Test first sample test case given in Problem.md
        """
        output = Main("file://{}/input/first.txt".format(self.cur_path)).run()
        exp_out = [[0, 1, 'NORTH']]
        assert output == exp_out

    def test_second_case(self):
        """ Test second sample test case given in Problem.md
        """
        output = Main("file://{}/input/second.txt".format(self.cur_path)).run()
        exp_out = [[0, 0, 'WEST']]
        assert output == exp_out

    def test_third_case(self):
        """ Test third sample test case given in Problem.md
        """
        output = Main("file://{}/input/third.txt".format(self.cur_path)).run()
        exp_out = [[3, 3, 'NORTH']]
        assert output == exp_out

    def test_empty_file(self):
        """ Test Empty file
        """
        output = Main("file://{}/input/empty.txt".format(self.cur_path)).run()
        exp_out = []
        assert output == exp_out

    def test_extra_spaces(self):
        """ Test file, which contain extra space after or before commands
        """
        output = Main("file://{}/input/extra_spaces.txt".format(self.cur_path)).run()
        exp_out = [[3, 3, 'NORTH']]
        assert output == exp_out

    def test_first_place_faulty(self):
        """ Test file with first and only PLACE command as faulty
        """
        output = Main("file://{}/input/first_place_faulty.txt".format(self.cur_path)).run()
        exp_out = []
        assert output == exp_out

    def test_invalid_cmd(self):
        """ Test file which contain invalid command
        """
        output = Main("file://{}/input/invalid_cmd.txt".format(self.cur_path)).run()
        exp_out = [[2, 3, 'NORTH']]
        assert output == exp_out

    def test_cmds_before_place(self):
        """ Test file which has some commands before PLACE command
        """
        output = Main("file://{}/input/cmds_before_place.txt".format(self.cur_path)).run()
        exp_out = [[3, 3, 'NORTH']]
        assert output == exp_out

    def test_large_cmd_file(self):
        """ Test file which has many commands
        """
        output = Main("file://{}/input/large_cmd_file.txt".format(self.cur_path)).run()
        exp_out = [[2, 4, 'WEST']]
        assert output == exp_out

    def test_cmd_file_not_present(self):
        """ Test file which is not present
        """
        try:
            Main("file://{}/input/abc.txt".format(self.cur_path)).run()
        except FileNotFoundError:
            assert True

    def test_multiple_report(self):
        """ Test file which has multiple reports
        """
        output = Main("file://{}/input/multiple_report.txt".format(self.cur_path)).run()
        exp_out = [[3, 3, 'NORTH'], [1, 3, 'WEST']]
        assert output == exp_out

    def test_y_coordinate_faulty(self):
        """ Test file which has faulty y coordinate
        """
        output = Main("file://{}/input/check_y_coordinate.txt".format(self.cur_path)).run()
        exp_out = []
        assert output == exp_out
