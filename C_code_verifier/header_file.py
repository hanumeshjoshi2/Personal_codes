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

* Reports the source file start with header files.
*/
'''

# -------------------------------- Source Code --------------------------------


# Required Library Files &  Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file

comment = 0

# checking multiline comments
def find_comment(lines,start,end,idx):
    #print(lines[start])
    #print(lines[end])
    global comment
    count = end+1
    comment = 1
    flag = False
    regix = re.compile('[@!#$%^&*()<>?/\|., }{~:-]|[a-z][A-Z]|[0-9]|[\+;]')
    while True:
        if (regix.search(lines[count]) == None):
            count += 1
        else:
            if lines[count].startswith("#include") and lines[count].endswith('.h"'):
                flag = True
                break
            elif re.search("^/\*+",lines[count]) or lines[count].startswith("*"):
                count += 1
                continue
            else:
                print("ERROR : file not start with header file")
                break
    if flag:
        print("No error Header files")
        print()
        return True
    else:
        print()
        return True


def check(file):
    idx = 0
    print("*********************\n Checking Header files\
\n*********************") 
    lines = [line.strip() for line in file]
    for index in range(len(lines)):
        #print("comment",comment)
        if comment == 0:
            if re.search("^/\*+.*\*/$",lines[index]):
                #print("Ignoring",lines[index])
                continue
            elif re.search("^/\*",lines[index]):
                if index <= 1:
                    start_index = index
                else:
                    return
            elif re.search("\*/$",lines[index]):
                if lines[index].startswith("*/") or lines[index].startswith("* "):
                    end_index = index
                    if start_index >=0 and end_index:
                        idx += 1
                        find_comment(lines,start_index,end_index,idx)
                        start_index = 0
                        end_index = 0
        else:
            return

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
