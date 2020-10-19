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

* Reports the line number that starts with a TAB space.
'''

# -------------------------------- Source Code --------------------------------

# Required Library Files & Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file
def check(file):
    print("*********************\n Checking Tabspace\
\n*********************")
    line_count = 0
    char_count = 0
    flag = False
    for line in file:
        line_count += 1
        char_count = len(line)
        if line.startswith(' '):
            value = '\t'
            testing_array=[]
            testing_array.append(line)
            for i in range(len(testing_array)):
                if value in testing_array[i]:
                    i=len(testing_array)-i
                    if testing_array[i-1].isalnum:
                        print("tabspace ahead of 1st character at line no:"\
                              ,line_count)
                        flag = True
                        
        if line.startswith("\t"):
            print("Rule for tab spaces-section 2.4.1 fails at line"\
                  ,line_count)
            flag = True
    if flag:
        print()
        return True
    else:
        print("No error in TAB SPACE ")
        print()
        return True
def main(file):
    try:
        fd = get_file.main(file)
        check(fd)
    except Exception:
        sys.print(sys.exc_info()[1])
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
