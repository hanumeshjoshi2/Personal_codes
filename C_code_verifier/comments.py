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

* Reports the line number that comments missing
*/
'''

# -------------------------------- Source Code --------------------------------


# Required Library Files &  Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

import re
import sys
import get_file


# checking multiline comments
def find_comment(lines,start,end,idx):
    #print(lines[start])
    #print(lines[end])
    flag = False
    for line in lines[start+1:end]:
        line = line.strip()
        #print(line)
        if line.startswith("*"):
            continue
        else:
            flag = True

    if flag:
        print("from Line number {} to {} is not saticified with Rule for \
comment section 2.4.4".format(start,end))
        print()
        return True
    else:
        print("no error in commenting Multiline comment",idx)
        print()
        return False

def check(file):
    idx = 0
    print("*********************\n Checking Multiline comment\
\n*********************") 
    file_lines = [line.strip() for line in file]
    file_lines = [line.strip("\t") for line in file_lines]
    for index in range(len(file_lines)):
        if re.search("^/\*+.*\*/$",file_lines[index]):
            #print("Ignoring",file_lines[index])
            continue
        elif re.search("^/\*+",file_lines[index]):
            start_index = index
            #print("start index",index)
        elif re.search("\*/$",file_lines[index]):
            if file_lines[index].startswith("*/") or file_lines[index].startswith("* "):
                end_index = index
                #print("end index", index)
                if start_index >=0 and end_index:
                    idx += 1
                    find_comment(file_lines,start_index,end_index,idx)
                    start_index = 0
                    end_index = 0


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
