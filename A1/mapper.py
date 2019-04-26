#!/usr/bin/python
""""mapper.py"""
import re
import sys
import json

pro1 = re.recompile('han', re.IGNORECASE)
pro2 = re.recompile('hon', re.IGNORECASE)
pro3 = re.recompile('hen', re.IGNORECASE)
pro4 = re.recompile('denne', re.IGNORECASE)
pro5 = re.recompile('den', re.IGNORECASE)
pro6 = re.recompile('det', re.IGNORECASE)
pro7 = re.recompile('denna', re.IGNORECASE)

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
