import re

def findIndexForString():
    inputFile = open("/workspaces/copilot-effeciency-study-JStuhrAsferg/Assignment02/stringmultimatching.in")

    lines = inputFile.readlines()
    inputFile.close()
    print("lines: " + str(lines))
    strippedLines = []

    for i in lines:
        #print (str(linenumber) + ":" + i)
        strippedLines.append(i.strip('\n'))

    print("lines: " + str(strippedLines))

    resultString = ""

    currentLinenumber = 0
    keepRunning = True
    while keepRunning:
        if currentLinenumber < len(strippedLines) and int(strippedLines[currentLinenumber]):

            currentSearchStrings = strippedLines[currentLinenumber+1:currentLinenumber+int(strippedLines[currentLinenumber])+1]
            currentSearch = strippedLines[currentLinenumber+int(strippedLines[currentLinenumber])+1]
            currentLinenumber = currentLinenumber + int(strippedLines[currentLinenumber])+2
            print("find: " + str(currentSearchStrings) + " In: " + currentSearch)
            for searchText in currentSearchStrings:
                indexesOfOccurences = [m.start() for m in re.finditer('(?='+ searchText + ')', currentSearch)]
                print("Indexes of occurences: " + str(indexesOfOccurences))
                strippedIndexes = str(indexesOfOccurences).strip("[").strip("]").replace(",","")
                resultString = resultString + strippedIndexes + "\n"
                print("StrippedIndexes: " + strippedIndexes)

        else:
            keepRunning = False


    print ("Result: " + resultString)
    return resultString

print(str(findIndexForString()))