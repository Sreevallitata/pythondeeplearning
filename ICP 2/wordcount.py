inFile = open("sreevalli.txt",'r')

sree = {}

line = inFile.readline()

while line != "":


    line = line.strip('').lower()

    for i in line.split(' '):

        if i in sree.keys():

            sree[i]+=1

        else:

            sree[i]=1

    line = inFile.readline()



for i in sree:

    print (i,':',sree[i])