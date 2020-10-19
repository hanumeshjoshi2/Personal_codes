#/usr/bin/python
#@author: Hanumesh joshi
#date : 01-Sep-2020

# import local modules.
import os
import json
import time
import sys

# import dependicy modules.
import ALL_case


# get the file lists in given directry and filter the json file.
def check(t_time,level,speed,dest_path,event_time): # function input Arguments (sleep time),(Level 1,,4),(car spped)

    os.chdir(dest_path)
    path = os.getcwd()
    while True:
        json_files = (i for i in os.listdir() if i.endswith(".json"))
        #print(len(json_files),"files")
        upload = False
        for json in json_files:
            try:
                ALL_case.check(json,level,speed,dest_path,t_time,event_time)
            except Exception:
                print(sys.exc_info()[1])
        if not upload:
            #print("waiting")
            time.sleep(60)
            pass
    else:
        print("no files")
        return

    
