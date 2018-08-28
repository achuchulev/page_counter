#!/usr/bin/env python

# define count variable
count = 0

def main():
#use the global variable instead of a local one
	global count
#increment count by 1
	count+=1
	return "{}".format(count)

if __name__ == '__main__':
	main()
	print count
#	print "{}".format(count) 
