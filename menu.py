#! /usr/bin/python3

print("Content-type: text/html")
print()

import os
import sys
import subprocess
import cgi 

cmd = cgi.FieldStorage()
value = cmd.getvalue('cmd')

flag = True

#choice 1:
choice = value
if (('docker' in choice.lower())or('container' in choice.lower())) and ('start' in choice.lower() or 'launch' in choice.lower() or 'open' in choice.lower()):
	ret = subprocess.getoutput('sudo systemctl start docker')
	print("Docker Service is Started at the server side...")

elif (('docker' in choice.lower())or('container' in choice.lower())) and ('stop' in choice.lower() or 'disable' in choice.lower() or 'shut' in choice.lower()):
	ret = subprocess.getoutput('sudo systemctl stop docker')
	print("Docker Service is been terminated...")

elif ('text' in choice.lower())or('notepad' in choice.lower()) or ('editor' in choice.lower()) or ('document' in choice.lower()) or ('write' in choice.lower())or('doc' in choice.lower()):
	print("A Text Editor was opened at the server side, Now it got closed..")
	ret = subprocess.getoutput('sudo gedit')
	print(ret)

elif ('date' in choice.lower())or('what is today' in choice.lower()):
	ret = subprocess.getoutput('date')
	print(f"Today's Date is --> {ret}")
	
elif ('calender' in choice.lower())or('cal' in choice.lower()) or ('month' in choice.lower())or('day' in choice.lower()):
	ret = subprocess.getoutput('cal')
	print(f"This Month Calender --> {ret}")
	
elif (('firewall' in choice.lower())or('firewalld' in choice.lower())) and ('start' in choice.lower() or 'launch' in choice.lower() or 'enable' in choice.lower()):
	ret = subprocess.getoutput('sudo systemctl start firewalld')
	print("We have started the firewall for you...")

elif (('firewall' in choice.lower())or('firewalld' in choice.lower())) and ('stop' in choice.lower() or 'shut' in choice.lower() or 'disable' in choice.lower()):
	ret = subprocess.getoutput('sudo systemctl stop firewalld')
	print("We have stopped the firewall for you...")
	
else:
	print("we can't quite understand you...")
	#cho = str(input("do you want to quit??"))
	#if cho == ('yes' or "True" or 'y' or 'Y'):
	#	flag = False
