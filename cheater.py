# -*- coding: utf-8 -*-
import sys
import os
import requests

if len(sys.argv) < 3:
	print "Not enough arguments!"
	sys.exit()

letters = sys.argv[1]
count = int(sys.argv[2])
letterList = [l for l in letters]
dictUrl = "./words2.txt"
match = 0

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

for word in content:
	if len(word) == count and checkValid(word) and checkMatch(word):
		url = "http://fanyi.youdao.com/openapi.do?keyfrom=4Pics1WordCheater&key=1630335074&type=data&doctype=json&version=1.1&q=%s" % word
		r = requests.get(url)
		response = r.json()
		
		explains = ""
		if 'basic' in response and 'explains' in response['basic']:
			for explain in response['basic']['explains']:
				explains += (explain + '\n')
		else:
			continue
		
		print word
		print explains
		print ""
		match += 1

print match