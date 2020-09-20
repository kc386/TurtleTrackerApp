#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Kimberly Corcoran (kimberly.corcoran@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------
#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'
#By making this a variable it makes it a parameter
#making the model more dynamic


#Create a file object from the file
file_object = open(file_name, 'r')


#Reading contents of the datafile into a list so we can iterate through list
line_list = file_object.readlines()

#Closing the file 
file_object.close()

#Iterate through all lines in the line list
for lineString in line_list:
    if lineString[0] == "#" or lineString[0] == 'u': 
        continue
    


    #split the string into a list of data items
    lineData = lineString.split()
    
    #Extract Items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara
    print(f"Record {record_id} Indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")

