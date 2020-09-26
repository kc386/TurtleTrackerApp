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
#Ask for user for the search date
user_date = input("Enter date to search for Sara: ")

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

#Create two empty dictionary objects
date_dict = {}
coord_dict = {}

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
    if obs_lc in ("1", "2", "3"):
        #print(f"Record {record_id} Indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
        #CHALLENGE to review in class
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)

#Create empty list to hold matching keys
matching_keys = []


#Loop through items in the date_dict and collect keys for matching ones
for date_item in date_dict.items():
    #Get the key and date of the dictionary item
    the_key, the_date = date_item
    #see if the date matches the user date
    if the_date == user_date:
        #if so, add the key to the list
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} Indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")