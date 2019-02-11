#!/usr/bin/python3
import os
import sys
import webbrowser
var=int(input("Enter 1 for date, 2 for calender, 3 for poweroff, 4 for IP, 5 for All ip, 6 for google search"))
if(var==1):
	os.system('date')
elif(var==2):
	os.system('cal')
elif(var==3):
	os.system('shutdown -H -T -30')
elif(var==4):
	os.system('hostname -I')
elif(var==5):
	os.system('ifconfig')
elif(var==6):
	se = input("Enter Keywords ")
	webbrowser.open_new_tab('https://www.google.com/search?q={}.format(se)')
else:
	print("Nothing Found")
