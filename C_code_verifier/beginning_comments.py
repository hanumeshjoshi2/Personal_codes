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

* Reports the error in  if becomments are missing
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
    comment = 1
    Copyright = False
    file_info = False
    version = False
    for line in lines[start+1:end]:
        line = line.strip()
        if re.search(r'Copyright',line):
            Copyright = True
            continue
        elif re.search(r'@file',line):
            file_info = True
            continue
        elif re.search(r'version',line):
            version = True
            continue

    if Copyright == False:
        print("ERROR : Copyright information is missing in the Beginning comments")
        print()
        #return True

    if file_info == False:
        print("ERROR : file discription is missing in the Beginning comments")
        print()
        #return True

    if version == False:
        print("ERROR : version infomation is missing in the Beginning comments")
        print()
        #return True
    else:
        print("no error in Beginning comments")
        print()
        return True

def check(file):
    idx = 0
    print("*********************\n Checking Beginning comment\
\n*********************") 
    lines = [line.strip() for line in file]
    for index in range(len(lines)):
        #print("comment",comment)
        if comment == 0:
            if re.search("^/\*+.*\*/$",lines[index]):
                print("Ignoring",lines[index])
                continue
            elif re.search("^/\*+",lines[index]):
                if index <= 1:
                    start_index = index
                else:
                    print("Begging comments are missing in the start of the file.")
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
