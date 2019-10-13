# toy_robot
===========

## Description

- Toy Robot Simulator to move it on a sqaure tabletop of 5*5 units

- Compatible with Python 3.7 and tested with pytest

## How to run

- Run with main.py and provide input file path with commands as command argument, for example:

	python main.py file://input/first.txt

- There are 4 options to provide the input:

    STDIN: stdin
    File: file://<path_to_file>
    sftp: sftp://<remote_path_to_file>
    s3: s3://<Bucket_name>/<Object_name>
    #sftp or S3 access parameters can be provided by Environment variables or in constants.py

- To download python 3.7, please refer https://www.python.org/downloads/

- Output will be provide in standard output or file by providing option "LOADER_TYPE" in ENV or "constants.py"

## To run test cases

- All test cases are written with pytest

- To install unittest library:

	pip install -r requirements.txt

- Run command:

	pytest

## Problem Description

* The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units
* There are no other obstructions on the table surface
* The robot is free to roam around the surface of the table, but must be prevented from falling to destruction
* Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed

Create an application that can read in commands of the following form -

    PLACE X,Y,F
    MOVE
    LEFT
    RIGHT
    REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

The origin (0,0) can be considered to be the SOUTH WEST most corner.

The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.

MOVE will move the toy robot one unit forward in the direction it is currently facing.

LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.

A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and REPORT commands.

Input can be from a file, or from standard input, as the developer chooses.

Provide test data to exercise the application.

## Constraints

The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.

## Example Input/Output

    a) PLACE 0,0,NORTH
    MOVE
    REPORT
    Output: 0,1,NORTH

    b) PLACE 0,0,NORTH
    LEFT
    REPORT
    Output: 0,0,WEST

    c) PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    Output: 3,3,NORTH

