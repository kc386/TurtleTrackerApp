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

#pretend we read one Line of data from the file 
lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'
#now we want to pull out specific files from the string and build a date dictionary and location dictionary. Each one will have the UID as its key
#So we are going to pull out all the coordinates, uid and date - so focus on a string method that allows us to take out specific values
#We are going to treat this as a delimited file and split 

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

