import unittest
import main

class TestRobotSimulator(unittest.TestCase):

	def test_first_case(self):
		""" Test first sample test case given in Problem.md
		"""
		output = main.Main(['input/first.txt']).run()
		exp_out = [[0, 1, 'NORTH']]
		self.assertTrue(output == exp_out)

	def test_second_case(self):
		""" Test second sample test case given in Problem.md
		"""
		output = main.Main(['input/second.txt']).run()
		exp_out = [[0, 0, 'WEST']]
		self.assertTrue(output == exp_out)

	def test_third_case(self):
		""" Test third sample test case given in Problem.md
		"""
		output = main.Main(['input/third.txt']).run()
		exp_out = [[3, 3, 'NORTH']]
		self.assertTrue(output == exp_out)

	def test_empty_file(self):
		""" Test Empty file
		"""
		output = main.Main(['input/empty.txt']).run()
		exp_out = []
		self.assertTrue(output == exp_out)

	def test_extra_spaces(self):
		""" Test file, which contain extra space after or before commands
		"""
		output = main.Main(['input/extra_spaces.txt']).run()
		exp_out = [[3, 3, 'NORTH']]
		self.assertTrue(output == exp_out)

	def test_first_place_faulty(self):
		""" Test file with first and only PLACE command as faulty
		"""
		output = main.Main(['input/first_place_faulty.txt']).run()
		exp_out = []
		self.assertTrue(output == exp_out)

	def test_invalid_cmd(self):
		""" Test file which contain invalid command
		"""
		output = main.Main(['input/invalid_cmd.txt']).run()
		exp_out = [[2, 3, 'NORTH']]
		self.assertTrue(output == exp_out)

	def test_cmds_before_place(self):
		""" Test file which has some commands before PLACE command
		"""
		output = main.Main(['input/cmds_before_place.txt']).run()
		exp_out = [[3, 3, 'NORTH']]
		self.assertTrue(output == exp_out)

	def test_large_cmd_file(self):
		""" Test file which has many commands
		"""
		output = main.Main(['input/large_cmd_file.txt']).run()
		exp_out = [[2, 4, 'WEST']]
		self.assertTrue(output == exp_out)

	def test_cmd_file_not_present(self):
		""" Test file which is not present
		"""
		try:
			main.Main(['input/abc.txt']).run()
		except FileNotFoundError:
			self.assertTrue(True)

	def test_multiple_report(self):
		""" Test file which has multiple reports
		"""
		output = main.Main(['input/multiple_report.txt']).run()
		exp_out = [[3, 3, 'NORTH'], [1, 3, 'WEST']]
		self.assertTrue(output == exp_out)

	def test_y_coordinate_faulty(self):
		output = main.Main(['input/check_y_coordinate.txt']).run()
		exp_out = []
		self.assertTrue(output == exp_out)

if __name__ == '__main__':
	unittest.main()
