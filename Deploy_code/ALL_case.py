#/usr/bin/python
#@author: Hanumesh joshi
#date : 01-Sep-2020

#import local modules.
import json
import os
import sys

#import dependency module
import Level_one

def del_files(file_name):
    for i in os.listdir():
        if i.startswith(file_name):
            os.remove(i)
    return


#Open json file and verify drowsiness and distrction fields
def check(file,level,speed,dest_path,t_time,event_time): # function input Arguments (json file), (folder containg file lists),\
                                                            #(level 1..5),(file destination path),(sleep time),(Total event time)
    path = os.getcwd()
    try:
        with open (file,"r") as FH:
            name = file.split('.') #split the file name i.e example.json [example,json]
            fh = json.load(FH)
            drowsiness = fh["drowsiness"]
            distraction = fh["distraction"]
            speed_value = float(fh["Speed"])
            s3 = int(fh["s3_frameCount"])
            s4 = int(fh["s4_frameCount"])
            drowsiness_frames = 0 #for checking 2 sec video if 60 frames there out of 500.
            distraction_frames = 0 #for checking 2 sec video if 60 frames there out of 500.

            #check the drowsiness and distraction fileds and it should not be empty or "No",
            # and if both are empty or No delete the related files.
            if ("" in drowsiness or "No" in drowsiness) and ("" in distraction or "No" in distraction):
                del_files(name[0])
                return
            else:
                for i in drowsiness:
                    frame = i.split('-') #split the frame values i.e 133-200 [133,200]
                    start_frame = int(frame[0])
                    end_frame = int(frame[1])
                    drowsiness_frames += (end_frame - start_frame)

                for i in distraction: 
                    frame = i.split('-') #split the frame values i.e 133-200
                    start_frame = int(frame[0])
                    end_frame = int(frame[1])
                    distraction_frames += (end_frame - start_frame)

                
                # upload if event is present
                if level == 2:
                    #print("level 2")
                    Level_one.Tar_and_upload(file,dest_path,t_time,level)
                    return

                # Upload the set if Speed/GPS and if any Drowsy/Distraction event is present - Event
                elif level == 3:
                    if speed_value >= speed :
                        #print("level 3")
                        Level_one.Tar_and_upload(file,dest_path,t_time,level)
                        return
                    else:
                        del_files(name[0])
                        #print("files deleted")
                        return


                # Upload the set if Speed/GPS+ Event + total duration of event is greater than atleast 2 seconds - TIME
                elif level == 4:
                    if speed_value >= speed :
                        #print("drowsiness_frames",distraction_frames)
                        #print("distraction_frames",distraction_frames) 
                        if drowsiness_frames >= event_time or distraction_frames >= event_time:
                            #print("level 4")
                            Level_one.Tar_and_upload(file,dest_path,t_time,level)
                            return
                        else:
                            del_files(name[0])
                            #print("files deleted")
                            return
                    else:
                        del_files(name[0])
                        #print("files deleted")
                        return

                # Upload the set if Speed/GPS+ Event + TIME + S3/S4 < 80%
                elif level == 5:
                    frame_rate = int((s3//s4))
                    if speed_value >= speed :
                        if drowsiness_frames >= event_time or distraction_frames >= event_time:
                            if frame_rate <= 80:
                                #print("level 5")
                                Level_one.Tar_and_upload(file,dest_path,t_time,level)
                                return
                            else:
                                del_files(name[0])
                                #print("files deleted")
                                return
                        else:
                            del_files(name[0])
                            #print("files deleted")
                            return
                    else:
                        del_files(name[0])
                        #print("files deleted")
                        return
                
    except Exception:
        print(sys.exc_info()[1])
    return
