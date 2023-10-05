import math

# Input file (_airlinehub.in_) contains several sets of input.  
# Each set consists of a line containing 1 <= _n_ <= 1000, the number of airports.  
# _n_ lines follow, each giving the latitude (between -180 and +180 degrees) and longitude (between -90 and +90 degrees) of an airport.  
# The input floating point numbers will not have more than two digits after the decimal point.  
# Input is terminated by end of file

# For each set of input print the latitude and longitude of the airport that best serves as a hub in a single line.  
# If there is more than one airport that best serves as a hub print the one that appears last in the input of the corresponding input set.  
# Your output should always contain two digits after the decimal point.

# Sample input:
# 3
# 3.2 -15.0
# 20.1 -175
# -30.2 10
# 3
# 52.31 4.76
# 51.96 4.44
# 51.45 5.37

# Sample output:
# 3.20 -15.00
# 52.31 4.76

def findLowestDistance(pointA, pointB, pointC):
    #figure out the distance between all ports and decide the point where there is the least distance between all ports
    #find the average of the distance between all ports
    #find the point where the average is the lowest
    #return the point with the lowest average
    
    #Convert the coordinates to floats
    pointA = [float(pointA[0]), float(pointA[1])]
    pointB = [float(pointB[0]), float(pointB[1])]
    pointC = [float(pointC[0]), float(pointC[1])]

    #distance between pointA and pointB
    distanceAB = math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)
    #distance between pointA and pointC
    distanceAC = math.sqrt((pointC[0] - pointA[0])**2 + (pointC[1] - pointA[1])**2)
    #distance between pointB and pointC
    distanceBC = math.sqrt((pointC[0] - pointB[0])**2 + (pointC[1] - pointB[1])**2)

    #Find the average distance from each port to the connecting port
    averageA = (distanceAB + distanceAC) / 2
    averageB = (distanceAB + distanceBC) / 2
    averageC = (distanceAC + distanceBC) / 2

    #Return whatever port has the lowest average distance to the other ports making sure the coordinates are returned with 2 decimals
    if averageA < averageB and averageA < averageC:
        return [round(pointA[0], 2), round(pointA[1], 2)]
    elif averageB < averageA and averageB < averageC:
        return [round(pointB[0], 2), round(pointB[1], 2)]
    elif averageC < averageA and averageC < averageB:
        return [round(pointC[0], 2), round(pointC[1], 2)]
    else:
        return "error"
    

def runner():  
    inputFile = open("/workspaces/copilot-effeciency-study-JStuhrAsferg/Assignment01/airlinehub.in")
    lines = inputFile.readlines()

    strippedLines = []
    for i in lines:
        #print (str(linenumber) + ":" + i)
        strippedLines.append(i.strip('\n'))


    currentLinenumber = 0
    keepRunning = True
    result = ""
    while keepRunning:
        # if current linenumber is not greater than the number of lines in the file and the current linenumber is not empty and the content of the line on the current linenumber is an integer
        if currentLinenumber < len(strippedLines) and strippedLines[currentLinenumber] and int(strippedLines[currentLinenumber]):
            # set the number of airports to the content of the line on the current linenumber
            numberOfAirports = int(strippedLines[currentLinenumber])
            # create an empty list of airports
            airports = []
            # for each airport in the range of the number of airports
            for airport in range(numberOfAirports):
                listOfAirportCoordinates = strippedLines[currentLinenumber + airport + 1].split(" ")
                # add the airport to the list of airports
                airports.append(listOfAirportCoordinates)
            # set the current linenumber to the current linenumber plus the number of airports plus one
            currentLinenumber = currentLinenumber + numberOfAirports + 1
            resultCoordinates = findLowestDistance(airports[0], airports[1], airports[2])
            # create result string where the coordinates have 2 decimals and are seperated with a space
            resultString = str("{:.2f}".format(resultCoordinates[0])) + " " + str("{:.2f}".format(resultCoordinates[1]))
            # add the result string to the result
            result = result + resultString + "\n"
        else:
            # set keepRunning to false
            keepRunning = False
    return result
        

print(runner())