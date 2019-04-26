#!/usr/bin/env python3
"""reducer.py"""


from operator import itemgetter
import sys

#current_word = None
#current_count = 0
#word = None
word2count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

   # parse the input we got from mapper.py
	word, count = line.split('\t', 1)

    # convert count (currently a string) to int
	try:
		count = int(count)

	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
		continue
# this IF-switch only works because Hadoop sorts map output
   # by key (here: word) before it is passed to the reducer
#== word:
#		current_count += count
#	else:
#		if current_word:
#			print('%s\t%s' % (current_word, current_count))
#		current_count = count
#		current_word = word
         # write result to STDOUT
#if current_word == word:
#	print('%s\t%s' % (current_word, current_count))
	try: 
		word2count[word] = word2count[word]+count
	except:
		word2count[word] = count

for word in word2count.keys():
	print('%s\t%s' % (word, word2count[word]))
