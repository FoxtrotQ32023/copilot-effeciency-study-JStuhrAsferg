import re
file = open("/workspaces/copilot-effeciency-study-JStuhrAsferg/Assignment02/stringmultimatching.in")

lines = file.readlines()
print("lines: " + str(lines))
strippedLines = []

for i in lines:
    #print (str(linenumber) + ":" + i)
    strippedLines.append(i.strip('\n'))

print("lines: " + str(strippedLines))


currentLinenumber = 0
keepRunning = True
while keepRunning:
    if currentLinenumber < len(strippedLines) and int(strippedLines[currentLinenumber]):

        currentSearchStrings = strippedLines[currentLinenumber+1:currentLinenumber+int(strippedLines[currentLinenumber])+1]
        currentSearch = strippedLines[currentLinenumber+int(strippedLines[currentLinenumber])+1]
        currentLinenumber = currentLinenumber + int(strippedLines[currentLinenumber])+2
        print("find: " + str(currentSearchStrings) + " In: " + currentSearch)
        for searchText in currentSearchStrings:
            indexesOfOccurences = [m.start() for m in re.finditer(searchText, currentSearch)]
            print("Indexes of occurences: " + str(indexesOfOccurences))
    else:
        keepRunning = False
 