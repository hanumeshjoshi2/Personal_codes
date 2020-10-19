'''
------------------------------ Program Information ----------------------------

Encoding Standard                : UTF-8

Supported Operating System       : Microsoft Windows/unix

Programming Language || Version  : CPython || 3.7.5

Input                            : .C File or Cpp file or header file

Output                           : Summary report for rules defined in 
                                   PathPartner Coding Guidelines document v1.30

--------------------------------- Functionality -------------------------------

To Check For The Mandatory Guidelines To Be Followed While Coding

* Reports the static function variable declaration and intialization error.
'''

# -------------------------------- Source Code --------------------------------

# Required Library Files & Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file

def check(file):
    print("*********************\n Checking static function declarition\
\n*********************")
    line_count = 0
    flag = False
    lines = [line.strip("\t") for line in file]
    lines = [line.strip(" ") for line in lines]
    for line in lines:
        var = line.split(" ")
        line_count += 1
        if re.search("^static ", line):
            if len(var) >= 3:
                if not var[2].startswith("s"):
                    flag = True
                    print("ERROR in LINE {} : static function variable is not prefix with 's'"\
                    .format(line_count))
                else:
                    continue
     
        
    if not flag:
        print("No error in static function declarition")
        print()
        return True
    else:
        print()
        return True

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
    
