'''
/*
------------------------------ Program Information ----------------------------

Encoding Standard                : UTF-8

Supported Operating System       : Microsoft Windows/unix

Programming Language || Version  : CPython || 3.7.5

Input                            : file directry

Output                           : Summary report for rules defined in 
                                   PathPartner Coding Guidelines document v1.30

--------------------------------- Functionality -------------------------------

To Check For The Mandatory Guidelines To Be Followed While Coding

* Reports the path and file name is not following PathPartner coding guide lines.
*/
'''

# -------------------------------- Source Code --------------------------------


# Required Library Files &  Internal/External Modules To Execute The Program

# In-Built Library Files, Which Is Available At Python's Standard Library

from tkinter import filedialog
from tkinter import *
import os
import re

def pattern_check(line):
    regex = re.compile('[@!#$%^&*()<>?/\|., }{~:-]|[A-Z]|[0-9]|[\+;]')
    if (regex.search(line) == None):
        return True
    else:
        return False
def main():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    print("folder_selected",folder_selected)
    directry_name = []
    file_name = []
    for (root,dirs,files) in os.walk(folder_selected):
        for i in dirs:
            flag = pattern_check(i)
            if flag :
                pass
            else:
                print("error in {} path folder and folder name is ('{}')".format(os.path.join(root, i),i))
        for i in files:
            lst = i.split('.')
            flag = pattern_check(lst[0])
            if flag:
                pass
            else:
                print("error in {} path folder and file name is ('{}')".format(os.path.join(root,i),i))

if __name__ == "__main__":
    try:
        if len(sys.argv) != 1:
            print("insufficient input !!!")
            print("usage :")
            print("pythone execution code : example.py")
            print("python file_open.py")
        else:
            main()
            sys.exit(0)
    except Exception:
        print(sys.exc_info()[1])


