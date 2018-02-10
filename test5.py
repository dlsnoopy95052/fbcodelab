import re
import argparse

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('word',help='specify word')
	parser.add_argument('fname',help='specify file to search')
	args = parser.parse_args()

	searchF=open(args.fname)
	lineN=0
	for line in searchF.readlines():
		line = line.strip('\n\r')
		lineN+=1
		searchResult = re.search(args.word. line,re.M|re.I)
		if searchResult:
			print(str(lineN)+': "+line')

if __name__ == "__main__":
	Main()
