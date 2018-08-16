#!/usr/bin/env python3
import getopt
import sys
import urllib.request 
import getopt 
import sys 
opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename ','version']) 
print(opts)
for opt_name,opt_value in opts: 
	print(opt_name)
	print(opt_value)
	if opt_name in ('-h','--help'):
		
		print("[*] Help info") 
		exit() 
if opt_name in ('-v','--version'):
	print("[*] Version is 0.01 ") 
	exit() 
if opt_name in ('-f','--filename'): 
	fileName = opt_value 
	print("[*] Filename is ",fileName) 
# do something 
	exit()
