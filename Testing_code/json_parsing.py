#/usr/bin/python
#@author: Hanumesh joshi
#date : 01-Sep-2020


#import local modules.
import json
import sys
import os

# import dependicy modules.
import Level_one
import other_level

#Open the congif file and extrct the required parameters.

def Get_config_data(file): # function input Arguments config file(confg.json) 
    try:
        with open (file,"r") as FH:
            fh = json.load(FH)
            #print(fh)
            return fh["Level"],fh["SleepTimeInMin"],fh["SpeedValueInKMPH"],fh["FilePath"],fh["EventTimeInSec"]
    except Exception:
        print(sys.exc_info()[1])
    return

# call a required module based on configaration in congig.json.
def main():
    try:
        level,sleep_time,speed,dest_path,event_time = Get_config_data("config.json") # take level, sleep time, zip limit, spped value.
        t_time = sleep_time #take value in sleep time.
        #print(level)
        if level == 1:
            Level_one.check(t_time,dest_path,level)
        elif level >=2 and level <= 5:
            other_level.check(t_time,level,speed,dest_path,event_time)   
        else:
            print("System can't find mentioned Level ")
            

    except Exception:
        print(sys.exc_info()[1])

    return

# code start from here   
main()
