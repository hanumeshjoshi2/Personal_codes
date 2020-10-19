#/usr/bin/python
#@author: Hanumesh joshi
#date : 01-Sep-2020

#import local modules
import os
import json
import shutil
import tarfile
import sys
import time

#import dependncy module.
import s3_bucket

# tar the  given json file,video file and csv file.
def tardir(pwd, tar_name): # function input Arguments (directry path), (tar file name)
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        #files = os.listdir(pwd)
        for file in os.listdir(pwd):
            tar_handle.add(file)

def check(t_time,dest_path,level): # function input Arguments (sleeptime, file destion path)(level)
    os.chdir(dest_path)
    path = os.getcwd()
    while True:
        json_files = (i for i in os.listdir(path) if i.endswith(".json"))
        upload = False #normal
        for json in json_files:
            Tar_and_upload(json,path,t_time,level)
            upload = True

        if not upload:
            print("waiting")
            time.sleep(60)
        
    else:
        print("no files")
        return

# get the file lists in given directry and filter the json file.
def Tar_and_upload(file,path,t_time,level):# function input Arguments (json file) (folder containg file lists) (file destination path)
    
    os.chdir(path)
    cwd = os.getcwd()
    try:
        with open (file,"r") as FH:
            name = file.split('.') #split the file name i.e example.json [example,json]
            fh = json.load(FH)
            dstfolder = fh["imei"]
            s_name = fh["session"]
            s_date = fh["Date&Time"].split(" ")[0]
            Raw_time = fh["Date&Time"].split(" ")[1]
            current_time = Raw_time.replace(":","")
            dir_name = dstfolder +"_"+current_time+"_"+s_name 
            os.mkdir(dir_name)
            
            #move json file, video file and csv file to directry and done tar file.
            for i in os.listdir():
                if i.startswith(name[0]):
                    shutil.move(i,dir_name)

            os.chdir(cwd+"/"+dir_name) # change directry to created directry.

            pwd = os.getcwd()
            tar_name = "Level_"+str(level)+"_"+dir_name + ".tar.gz" # Based on level create tar file.
            tardir(pwd, tar_name)

            #upload Tar file to the server
            s3_data = s3_bucket.upload(tar_name,pwd, dstfolder, t_time,s_date)
            dictionary ={"s3_upload" : "0","mcp_upload" : "false"}
            print(s3_data)
            if s3_data:
	            dictionary["s3_upload"] = "true"
            else:
	            dictionary["s3_upload"] = "false"
            # Serializing json  
            json_object = json.dumps(dictionary, indent = 4) 
  
            # Writing to sample.json 
            with open("upload_status.json", "w") as outfile: 
                outfile.write(json_object)
            print("done")
            os.chdir(cwd)
            
            """ 
            #delete the tar file
            dir_path = os.path.join(cwd,dir_name)
            shutil.rmtree(dir_path)
            """
            return

    except Exception:
        print(sys.exc_info()[1])
    return
