# Toy Robot Simulator


## Description

- Toy Robot Simulator to move it on a square tabletop of 5*5 units

- Compatible with Python 3.7 and tested with pytest

## How to run

- To download python 3.7, please refer https://www.python.org/downloads/

- Install required packages:

    `pip install -r requirements.txt`

- Run with main.py and provide input file path with commands as command argument, for example:

    `cd toy_simulator`
    
    `python main.py file://tests/input/first.txt`

- There are 4 options to provide the input:

    `STDIN: stdin`
    
    `File: file://<path_to_file>`
    
    `sftp: sftp://<remote_path_to_file>`
    
    `s3: s3://<Bucket_name>/<Object_name>`
    
    `#sftp or S3 access parameters can be provided by Environment variables or in constants.py`

- Output will be provide in standard output or file by providing option "LOADER_TYPE" in ENV or "constants.py"

## To run test cases

- All test cases are written with pytest

- To install pytest library:

	`pip install -r requirements.txt`

- Run command:

    `cd toy_simulator`
    
     `python -m pytest`

## Design

- Robot class provides the current location of Robot and operations on Table

- Table class provides the Table top matrix and validate the location of Robot on it

- Command class provides different types of commands by inheritance, which provide operations on Robot

- Starting with main class which invoke Extractor, Simulator and Loader

- There are four different type of Extractors included, which can be extended further for different types of extractors by deriving from  base Extractor class

- Similarly Loaders can be extended by deriving from base Loader class. Currently stdout and file type loaders

- Main logic to simulate Robot is invoking from Simulator class which contains Robot and CommandType to find the type of command

- It can be easliy extendable for more:
	- Input types (Extractors)
	- Output types (Loaders)
	- Robots
	- Dimensions of tables
	- Tables
	- Commands to run

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

