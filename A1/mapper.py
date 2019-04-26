#!/usr/bin/env python3
""""mapper.py"""
import re
import sys
import json

pro1 = re.compile('han', re.IGNORECASE)
pro2 = re.compile('hon', re.IGNORECASE)
pro3 = re.compile('hen', re.IGNORECASE)
pro4 = re.compile('denne', re.IGNORECASE)
pro5 = re.compile('den', re.IGNORECASE)
pro6 = re.compile('det', re.IGNORECASE)
pro7 = re.compile('denna', re.IGNORECASE)

han = 0
hon = 0
hen = 0
denne = 0
den = 0
det = 0
denna = 0
count = 0

for line in sys.stdin:
	line = line.strip()
	if(len(line) > 0):
		tweettxt = json.loads(line)
		
		if('retweeted_status' not in tweettxt):
			current = tweettxt['text']
			if pro1.search(current):
				print ('%s\t%s' % ("han", 1))
			if pro2.search(current):
				print ('%s\t%s' % ("hon", 1))
			if pro3.search(current):
				print ('%s\t%s' % ("hen", 1))
			if pro4.search(current):
				print ('%s\t%s' % ("denne", 1))
			if pro5.search(current):
				print ('%s\t%s' % ("den", 1))
			if pro6.search(current):
				print ('%s\t%s' % ("det", 1))
			if pro7.search(current):
				print ('%s\t%s' % ("denna", 1))
			#count = 1
	


