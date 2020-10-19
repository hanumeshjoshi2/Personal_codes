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

* Reports the nunmber of lines of code in the files.
'''

# -------------------------------- Source Code --------------------------------

# Required Library Files & Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys

def main(file):
    try:
        comment_lines = 0
        with open(file) as FILE_DATA:
            fd = FILE_DATA.readlines()
            lines = [line.strip() for line in fd]
            print()
            print("LINES : {} nunmber of lines of code in the file ".format(len(lines)))
            LINES = "LINES :"+str(len(lines))+ "nunmber of lines of code in the file "
            print()
            for index in range(len(lines)):
                if re.search("^/\*+.*\*/$",lines[index]):
                    comment_lines += 1
                elif re.search("^/\*+",lines[index]):
                    start_index = index
                elif re.search("\*/$",lines[index]):
                    end_index = index
                    comment_lines += len(lines[start_index : end_index])
                else:
                    continue
            print("COMMENTS : Out of {} lines of code, {} lines comments are there"\
.format(len(lines),comment_lines))
            comments = "COMMENTS : Out of" +str( len(lines))+" lines of code,"+str(comment_lines)+"lines comments are there"
            print()
            return fd,LINES,comments
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
