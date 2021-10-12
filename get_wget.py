import os
link=[]
for i in range(int(input("How many links ?= "))):
	l=str(input("Enter the link :: "))
	link.append(l)
for i in link:	
	command="wget"+" "+i
	os.system(command)
