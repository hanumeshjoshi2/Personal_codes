'''
/*
------------------------------ Program Information ----------------------------

Encoding Standard                : UTF-8

Supported Operating System       : Microsoft Windows/unix

Programming Language || Version  : CPython || 3.7.5

Input                            : .C File or Cpp file or header file

Output                           : Summary report for rules defined in 
                                   PathPartner Coding Guidelines document v1.30

--------------------------------- Functionality -------------------------------

To Check For The Mandatory Guidelines To Be Followed While Coding

* Reports the line number that space after commas.
*/
'''

# -------------------------------- Source Code --------------------------------


# Required Library Files &  Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file

flag = False
def find_comment(lines,index):
    global flag
    var = lines[index].split(',')
    del var[0]
    for i in var:
        if not i.startswith(' '):
            flag = True
            print("ERROR in Line  {} is not given space after comma in argument list"\
            .format(index+1))
            return
            

def check(file):
    global flag
    idx = 0
    print("*********************\n Checking comma in argument list\
\n*********************") 
    file_lines = [line.strip() for line in file]
    file_lines = [line.strip("\t") for line in file_lines]
    for index in range(len(file_lines)):
        if re.search("^/\*+.*\*/$",file_lines[index]):
            continue
        elif re.search("^/\*",file_lines[index]):
            continue
        elif re.search("\*/$",file_lines[index]) and file_lines[index].startswith("*/"):
            continue
        elif file_lines[index].startswith("*") or file_lines[index].startswith('//') \
        or file_lines[index].endswith(","):
            continue
        elif ',' in file_lines[index]:
            find_comment(file_lines,index)
           
    if not flag:
        print("No error in space appear after comma in argument list ")
        print()
        return True
    else:
        print()
        return False


def main(file):
    try:
        fd = get_file.main(file)
        check(fd)
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
            main(sys.argv[1])
            sys.exit(0)
    except Exception:
        print(sys.exc_info()[1])
