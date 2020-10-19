'''
*------------------------------ Program Information ----------------------------

Encoding Standard                : UTF-8

Supported Operating System       : Microsoft Windows/unix

Programming Language || Version  : CPython || 3.7.5

Input                            : .C File or Cpp file or header file

Output                           : Summary report for rules defined in 
                                   PathPartner Coding Guidelines document v1.30

*--------------------------------- Functionality -------------------------------

To Check For The Mandatory Guidelines To Be Followed While Coding
/*
* Reports the line number that comments missing
* Reports the line number that starts with a TAB.
* Reports the line number having more than 80 Characters.
* Report the line number worng comment.
* Report the error in worong comments.
* Report the error in beginning comments.
* Report the error in header files.
* Report the error in define and constant declaration.
* Report the error in variable declaration and intialization.
* Report the error in static function declaration.
* Report the error in function declaration.
* Report the error in space after a comma in argument list.
*/

'''

# -------------------------------- Source Code --------------------------------


# Required Library Files &  Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import datetime
import os
import time
import get_file
import wrong_comments
import tab_space
import eighty_char
import comments
import beginning_comments
import header_file
import define_constant
import variable_declare
import static_func
import func_declare
import comma_space

# Get the local date.
def GetlocalDate():
    LocalTime = time.localtime()
    Date = str(LocalTime[0]) + str(LocalTime[1]) + str(LocalTime[2])
    sDate = str(LocalTime[0]) + "/" + str(LocalTime[1]) + "/" + str(LocalTime[2])
    return Date, sDate

def GetLocalTime():
    LocalTime = time.localtime()
    Time = str(LocalTime[3]) + str(LocalTime[4]) + str(LocalTime[5])
    StandardTimeFormat = str(LocalTime[3]) + ":" + str(LocalTime[4]) + ":" + str(LocalTime[5])
    return Time, StandardTimeFormat

def LogfileFormat():
    EXT = ".log"
    Time, sTime = GetLocalTime()
    Date, sDate = GetlocalDate()
    LOG_FILE = "D" + Date + "_" + "T" + Time + EXT
    return LOG_FILE

def check(file,LINES,COMMENT):

    csvfile = LogfileFormat()
    # Create Reports directory
    cwd = os.getcwd()
    #print(cwd + '/Reports')
    if not os.path.exists(cwd + '/Reports'):
        try:
            os.makedirs(cwd + '/Reports')
        except OSError:
            print('Not able to create report directory.\n')
    else:
        print('Reports directory has been created already.\n')

    cwd = os.getcwd()
    cwd = cwd + '/Reports'
    with open(cwd + '/' + csvfile, 'w')as FD:

        beginning_comments.check(file)
        header_file.check(file)
        wrong_comments.check(file)
        comments.check(file)
        define_constant.check(file)
        variable_declare.check(file)
        tab_space.check(file)
        eighty_char.check(file)
        static_func.check(file)
        func_declare.check(file)
        comma_space.check(file)
        FD.write(LINES)
        FD.write("\n")
        FD.write(COMMENT)
        FD.write("\n")
        FD.write("finished")
    
def main(file):
    try:
        fd,LINES,COMMENT = get_file.main(file)
        check(fd,LINES,COMMENT)
    except Exception:
        print(sys.exc_info()[1])
    return


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("insufficient input !!!")
            print("usage :")
            print("pythone execution code : example.py\
input file : example.c/.h/.cpp")
            print("python file_open.py c-file.c")
        else:
            print()
            print("input file Name",sys.argv[1])
            main(sys.argv[1])
            sys.exit(0)
    except Exception:
        print(sys.exc_info()[1])
