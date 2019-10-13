import sys
from extract_input_type import ExtractInputType
from loader_type import LoaderType
from simulator import RobotSimulator


class Main:
    """ Main class to get input type or file with commands
    Call Robot simulator to run the commands
    And run loader to load the results in file or stdout
    """
    def __init__(self, arg):
        """
        Pick the input argument
        :param arg: input type or/and file name
        """
        self.arg = arg

    def run(self):
        """
        Extract the commands, run for Robot and load
        :return: Return the result list
        """
        extract_obj = ExtractInputType.extract_type(self.arg)
        lines = extract_obj.extract(self.arg)

        # Main simulation happens here
        results = RobotSimulator().simulate(lines)

        LoaderType.loader_type().load(results)

        return results


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
