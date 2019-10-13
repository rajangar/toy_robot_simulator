import sys
from extract_command_type import ExtractCommandType
from loader_type import LoaderType
from simulator import RobotSimulator


class Main:
    """ Main class to get input file with commands
    And call Robot simulator to run the commands
    """
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        """ Calling Simulator to run commands
        """
        extract_obj = ExtractCommandType.extract_type(self.arg)
        commands = extract_obj.extract(self.arg)

        results = RobotSimulator().simulate(commands)

        LoaderType.loader_type().load(results)


if __name__ == '__main__':
    try:
        if not sys.argv[1:]:
            print("Provide input type in command arguments:\n"
                  "\tFor STDIN input: STDIN\n"
                  "\tFor S3 input: s3://<Bucket name>/<Object name>\n"
                  "\tFor file input: file://<path_to_file>\n"
                  "\tFor file input from remote: sftp://<remote_path_to_file>:\n"
                  "\tFor sftp and s3 inputs, access information should be there in environment variables")
            raise Exception
        main = Main(sys.argv[1])
        main.run()
    except Exception as e:
        print("An error occurred, error = ", e)
