import sys
import os

if len(sys.argv) < 3:
	print "Not enough arguments!"
	sys.exit()

letters = sys.argv[1]
count = int(sys.argv[2])

letterList = [l for l in letters]

dictUrl = "/Users/shuozhang/Downloads/english-words-master/words2.txt"

with open(dictUrl) as f:
	content = [line.rstrip('\n') for line in f]

def checkValid(word):
	for letter in word:
		if letter not in letterList:
			return False
	return True

def checkMatch(word):
	for letter in word:
		if word.count(letter) <= letterList.count(letter):
			continue
		else:
			return False
	return True

match = 0

for word in content:
	if len(word) == count :
		if checkValid(word) and checkMatch(word):
			print word
			match += 1

print match