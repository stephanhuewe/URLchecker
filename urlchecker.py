#!/usr/bin/env python

import sys
import os
import getopt

try:
	import requests
except:
	print "Request library not found, please install it before proceeding\n"
	sys.exit()


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print " -------------------"
print "| URLchecker v. 0.1 |"
print "| By Ben Sooter     |"
print " -------------------"

def usage():

	comm = os.path.basename(sys.argv[0])

	if os.path.dirname(sys.arg[0]) == os.getcwd():
		comm = "./" + comm

	print "Usage: urlchecker -options \n"
	print "		-s: List of URLs to test against"
	print "		-o: Ouput file (CSV)"


def start(argv):
	if len(sys.argv) < 4:
		usage()
		sys.exit()
	try:
		opts, args = getopt.getopt(argv, "s:o")
	except getopt.GetoptError:
		usage()
		sys.exit()
	sitelists = ""
	filename = ""
	for opt, arg in opts:
		if opt == '-s':
			sitelists = arg
		elif opt == '-o':
			filename = arg
		else:
			usage()
			sys.exit()


#res = requests.get('http://'+'google.com', timeout=5)
#topsites = open("topsites.txt", "r")
#urlfoo = topsites.readlines()
#resultfile = open('results.txt','w')
with open(sitelists) as f:
	mylist = f.read().splitlines()
results = "init"
#with open('results.txt', 'w') as resultfile:
for line in mylist:
	resultfile = open(filename,'a')
	bob = 'http://'+line
	try:
	#bob = 'http://'+line
	#print "normal one"
	#res2 = requests.get('http://google.com', timeout=5)
	#print "normal one worked"
	#print "list one"
		res = requests.get(bob, timeout=6,verify=False)
		results = line + ",PASS,0"
	#print "Pass!"
	except requests.exceptions.ReadTimeout as e:
		results = line + ",FAIL,1"
	except requests.exceptions.ConnectionError as e:
		results = line +",FAIL,2"
	except requests.exceptions.TooManyRedirects as e:
		results = line +",FAIL,3"
	except requests.exceptions.ChunkedEncodingError as e:
		results = line +",FAIL,4"
	print results
	resultfile.write(results+"\n")
	resultfile.close()
#resultfile.close()
