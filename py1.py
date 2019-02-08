#!usr/bin/python3
import os
var=int(input("Enter 1 for date, 2 for calender, 3 for poweroff, 4 for "))
if(var==1):
	os.system('date')
elif(var==2):
	os.system('cal')
elif(var==3):
	os.system('poweroff')
else:
	print("Nothing Found")
