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

* Reports the variable declaration and intialization erooe.
'''

# -------------------------------- Source Code --------------------------------

# Required Library Files & Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file

def check(file):
    print("*********************\n Checking variable intialization and declarition\
\n*********************")
    line_count = 0
    flag = False
    lines = [line.strip("\t") for line in file]
    lines = [line.strip(" ") for line in lines]
    for line in lines:
        var = line.split(" ")
        line_count += 1
        if line.startswith("int ") or line.startswith("enum "):
            if ";" in line:
                if "=" in line:
                    flag = True
                    print("WARNING!! in line {} : 'int' variable intialization and declarion in same line"\
                    .format(line_count))
                if not var[1].startswith("n"):
                    if "*" in var[1]:
                        if not var[1].startswith("*p"):
                            flag = True
                            print("WARNING!! in line {} : 'int or enum' pointer variable  name is not prefix with 'p'"\
                            .format(line_count))
                    else:
                        flag = True
                        print("WARNING!! in line {} : 'int or enum' variable  name is not prefix with 'n'"\
                        .format(line_count))
        
        elif line.startswith("float ") or line.startswith("double "):
            if ";" in line:
                if "=" in line:
                    flag = True
                    print("WARNING!! in line {} : 'float or double' variable intialization and declarion in same line"\
                    .format(line_count))
                if not var[1].startswith("f"):
                    if "*" in var[1]:
                        if not var[1].startswith("*p"):
                            flag = True
                            print("WARNING!! in line {} : 'float or double' pointer variable  name is not prefix with 'p'"\
                            .format(line_count))
                    else:
                        flag = True
                        print("WARNING!! in line {} : 'float or double' variable  name is not prefix with 'f'"\
                        .format(line_count))

        elif line.startswith("char "):
            if ";" in line:
                if "=" in line:
                    flag = True
                    print("WARNING!! in line {} : 'char' variable intialization and declarion in same line"\
                    .format(line_count))
                if not var[1].startswith("c"):
                    if "*" in var[1]:
                        if not var[1].startswith("*p"):
                            flag = True
                            print("WARNING!! in line {} : 'char' pointer variable  name is not prefix with 'p'"\
                            .format(line_count))
                    else:
                        flag = True
                        print("WARNING!! in line {} : 'char' variable  name is not prefix with 'c'"\
                        .format(line_count))
        
        elif line.startswith("bool "):
            if ";" in line:
                if "=" in line:
                    flag = True
                    print("WARNING!! in line {} : 'bool' variable intialization and declarion in same line"\
                    .format(line_count))
                if not var[1].startswith("b"):
                    if "*" in var[1]:
                        if not var[1].startswith("*p"):
                            flag = True
                            print("WARNING!! in line {} : 'bool' pointer variable  name is not prefix with 'p'"\
                            .format(line_count))
                    else:
                        flag = True
                        print("WARNING!! in line {} : 'bool' variable  name is not prefix with 'b'"\
                        .format(line_count))
        
    if not flag:
        print("No error in variable intialization and declarition")
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
    
