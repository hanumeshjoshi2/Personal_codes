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

* Reports the  line number function declaration missmatch with coding guidlines.
'''

# -------------------------------- Source Code --------------------------------

# Required Library Files & Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file
def check(file):
    print("*********************\n Checking function declaration statements\
\n*********************")
    line_count = 0
    char_count = 0
    flag = False
    regix = re.compile('[@!#$%^&*()<>?/\|., }{~:-]|[a-z][A-Z]|[0-9]|[\+;]')
    sample_line = [line.strip(" ") for line in file]
    sample_line = [line.strip("\t") for line in sample_line]
    sample_line = [line.strip("\n") for line in sample_line]
    for line in file:
        line_count += 1
        if line.startswith("int ") or line.startswith("bool ") or line.startswith("void ")\
             or line.startswith("float ") or line.startswith("char ") :
            if ";" not in line and "main" not in line:
                if (regix.search(file[line_count-2]) == None):
                    if "*/"  not in file[line_count-3]:
                        flag = True
                        print("ERROR in line : {} function declaration in missing"\
                        .format(line_count))
                elif "*/"  not in file[line_count-2]:
                    flag = True
                    print("ERROR in line : {} function declaration in missing"\
                    .format(line_count))
            else:
                continue

    if not flag:
        print("No error in function declarion")
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
