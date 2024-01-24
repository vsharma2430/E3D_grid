import os 

def readLineByLine (fileLocation) : 
    readLines = []
    if(fileLocation!=None and fileLocation!='' and os.path.exists(fileLocation)):
        file1 = open(fileLocation, 'r')
        Lines = file1.readlines()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            readLines.append(line.strip())
            #print("Line{}: {}".format(count, line.strip()))
        file1.close()
    return readLines