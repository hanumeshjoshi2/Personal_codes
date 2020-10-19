Follow the Steps mentioned below.
pre-conditions
1. All Dependency file should be in same directry
2. config file should be in same directry.

setps
1. open the config.json

2. set the parameters.

"Level" : 1 to 5 // based on levels script will upload the files and delete the files.

"SleepTimeInMin" : 5 //Upload to cloud with sleep every 5 mins.(edit when you want less sleep time or more)

"SpeedValueInKMPH" : 20 // define the car speed based on value file will be upload.(edit when you check more speed or less)

"EventTimeInSec" : 60 // set the total duration of event is 2 seconds. 60 when 30fps. 120 when 15fps.

"FilePath" : "/home/root/data/" // video files path in system(edit when you run locally).

3. once set the parameters save config file and Run the json_parsing.py

code flow

json_paring.py call the  main() function
main function call the get_config_data(file)// it will return config parameters.
case 1
if level parameter is 1
call the Level_one.check(t_time,dest_path,level) function.
in that funtion list the json files and done tar and upload to cloud and delete the related files.
login the cloud and check its uploded.

case 2
if level parameter is more that 1
call other_level.check function.
in that function list the json files and call All_case.check funtion.
in that function parse the json file and validate parameters based on configured level
if its match with conditions call the Level_one.tar_and_upload() function, else delete the related files.
done a tar and upload to cloud and delete the related files.
login the cloud and check its uploded.
