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

han = '0'
hon = '0'
hen = '0'
denne = '0'
den = '0'
det = '0'
denna = '0'
count = '0'

for line in sys.stdin:
	line = line.strip();
	try:
		tweettxt = json.loads(line)
		if(tweettxt['retweet'] == False):
			current = tweettxt['tweet']
			if pro1.search(current) is not None:
				han = '1'
			if pro2.search(current) is not None:
				hon = '1'
			if pro3.search(current) is not None:
				hen = '1'
			if pro4.search(current) is not None:
				denne = '1'
			if pro5.search(current) is not None:
				den = '1'
			if pro6.search(current) is not None:
				det = '1'
			if pro7.search(current) is not None:
				denna = '1'
			count = '1'
	except:
		continue

	print ('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (han,hon,hen,denne,den,det,denna, count))

	han = '0'
	hon = '0'
	hen = '0'
	denne = '0'
	den = '0'
	det = '0'
	denna = '0'
