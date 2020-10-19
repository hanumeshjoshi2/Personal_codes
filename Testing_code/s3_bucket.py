#/usr/bin/python
#@author: Hanumesh joshi
#date : 01-Sep-2020

#import local modules.
import time
from time import gmtime, strftime
import os

#import external modules.(use pip to install below modules)
from boto3 import session
from botocore.client import Config
from botocore.exceptions import EndpointConnectionError


ACCESS_ID = '' #write server Access ID
SECRET_KEY = '' #write secret key of server

# sleep 5 min once file succesfully uplode.
def sleep_time(start_time,end_time,t_time):# function input Arguments (start time before upload) (end time after upload)(sleep time)
    print("entered sleep mode")
    time_diff = (end_time - start_time)//60
    print(time_diff)
    if time_diff <=1 or time_diff >=6 :
        time.sleep(t_time*60)
        print("sleep",t_time," min")
        return 
    elif time_diff >=2 and time_diff <=5:
        time.sleep((t_time - time_diff) * 60)
        return
    
# upload to the cloud.
def upload(file,path,dstfolder,t_time,s_date):# function input Arguments (tar file)(destination path)(ime number)(sleep time)
    print("Initiate uploading process")
    # Initiate session
    sess = session.Session()
    client = sess.client('s3',
                            region_name='nyc3',
                            endpoint_url='https://ppdms.nyc3.digitaloceanspaces.com',
                            aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY)


    source_path = path +"/"+file
    #space_name = imeino_macno
    try:
        start_time = int(strftime("%H%M%S",gmtime()))
        responce = client.upload_file(source_path, dstfolder,(s_date+"/"+ file))
        print("upload done")
        end_time = int(strftime("%H%M%S",gmtime()))
        sleep_time(start_time, end_time,t_time)
        return True
    except EndpointConnectionError as error:
        print(error)
        return False

#cwd = os.getcwd()
#name = "123"
#upload("encode_2.json",cwd,name)
