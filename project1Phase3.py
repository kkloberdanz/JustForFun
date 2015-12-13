# Programmer: Kyle Kloberdanz
# HawkID: 00798167
# Assignment: project1Phase3.py

def strListToIntList(L):
    '''
    Takes a list of strings and converts it to a list of integers
    '''
    i = 0
    while i < len(L):
        j = 0        
        while j < len(L[i]):
            L[i][j] = int(L[i][j])
            j += 1
        i += 1    
    return L

def createDataStructure():
    '''
    This function takes a text file as a parameter and
    converts that file into the string masterLine
    '''
    file = open("miles.dat", "r")
  
    i = 0
  
    cityName = ''
    cityList = []

    stateCode = ''
    stateList = []

    coordinateList = []

    population = ''
    populationList = []

    distance = ''
    distanceList = []

    # This is to account for the distance of the first city to itself, 0
    firstDistance = ['0']
    distanceList.append(firstDistance)

    listofnumbers = []
   
    # Reads to the end of the file
    while True:
       
        # reads the file line by line
        line = file.readline()
       
        i = 0
        cityName = ''
        coordinates = ''
        population = ''
        distance = ''
       
        # exit from while loop when line is empty
        if line == "":
            break
       
        # The following is to get the distances
        if line[0].isdigit():
            while line[0].isdigit():
                i = 0
                while i < (len(line) - 1):
                    distance = distance + line[i]
                    i += 1

                # Spaces the distances apart from eachother when a new line is read
                distance = distance + ' '

                # Reads new line until line[0] is not a digit
                line = file.readline()
                                    
            distance = distance.split()
            distanceList.append(distance)
            
        i = 0
       
        # if line begins with a word/letter
        if line[0].isalpha():

            # x and y coordinates that make up the coordinates
            xco = ''
            yco = ''
          
            # Gets cityName
            while line[i] != ",":
                cityName = cityName + line[i]
                i += 1
              
            # Gets stateCode
            if line[i] == ",":
                stateCode = line[i+2] + line[i+3]
                stateList.append(stateCode)

            # Creates a list of the following: 'CITYNAME STATECODE'
            if cityName != '':
                cityName = cityName + " " + stateCode
                cityList.append(cityName)

                # advances the index to the char after '[' so it can get coordinates later
                i = line.index("[")
                i += 1
 
            # Gets coordinates, and stores them in a list of integers
            while line[i] != ",":
                xco = xco + line[i]
                i += 1
            xco = int(xco)

            # Moves i to the position after ","
            i += 1

            while line[i] != "]":
                yco = yco + line[i]
                i += 1
            yco = int(yco)
            coordinateList.append([xco, yco])
           
            # shifts the index to the char after ']' so it can get population later
            i = line.index("]")
            i += 1
           
            # Gets population
            while i < (len(line) - 1):
                population = population + line[i]
                i += 1
            populationList.append(int(population))

    file.close()
    
    # converts distanceList from a list of strings to a list of integers
    distanceList = strListToIntList(distanceList)
   
    return [cityList, coordinateList, populationList, distanceList]

def getCoordinates(city, data):
    '''
    Takes city (string) and data (list) as parameters.
    Returns the coordinates of the before mentioned city
    '''
    index = data[0].index(city)
    return data[1][index]

def getPopulation(city, data):
    '''
    Takes city <string> and data <list> as parameters.
    Returns the population of the before mentioned city
    '''
    index = data[0].index(city)
    return data[2][index]

def getDistance(city1, city2, data):
    '''
    Takes city1 <string>, city2 <string>, and data <list> as parameters.
    Returns the distance of city1 from city2
    '''
    if city1 == city2:
        return 0
    
    cityindex1 = data[0].index(city1)
    cityindex2 = data[0].index(city2)

    if cityindex1 > cityindex2:
        cityindex = cityindex1
    else:
        cityindex = cityindex2

    numCitiesBetweenIndexes = abs(cityindex1 - cityindex2)

    distance = data[3][cityindex][numCitiesBetweenIndexes - 1]
   
    return distance

def nearbyCities(c, r, data):
    '''
    Takes c <string> (c for city) and r <integer> (r for radius) as parameters
    Returns cities that are within r miles
    '''
    cityList = []

    # Checks the distance of the city, c, with every other city in the list
    # if the city is within the radius, r, then it is appended to cityList
    for i in range(0, len(data[0])):
        distance = getDistance(c, data[0][i], data)
        if distance <= r:
            cityList.append(data[0][i])

    cityList.sort()
       
    return cityList

def mostNearbyCities(distance, data, served):
    '''
    This function takes distance <int>, data <list>, and served <list>
    and returns the city that has the most cities within the radius
    'distance' that has not yet been served.
    '''
    cityList = data[0]
    searchList = []

    for i in range(0, len(served)):
        if served[i] == False:
            searchList.append(cityList[i])
    maxCity = searchList[0]
    maxCities = len(nearbyCities(maxCity, distance, data))

    for candidate in searchList:
        if len(nearbyCities(candidate, distance, data)) > maxCities:
            maxCity = candidate
            maxCities = len(nearbyCities(candidate, distance, data))

    return maxCity

def locateFacilities(data, r):
    """
    Creates a list of cities that one could put a facility in that
    can service all of the cities from the data structure. Uses a
    greedy algorithm to reduce the number of facilities needed.
    """
    cityList = data[0]
    candidateList = []
    
    # Creates a list that denotes which city is served
    served = list(range(len(cityList)))
    for i in range(len(served)):
        served[i] = False
    
    while False in served:                 
        candidate = mostNearbyCities(r, data, served)  
        nearCities = nearbyCities(candidate, r, data)

        # marks all of the near cities as served
        for i in range(0, len(nearCities)):
            served[cityList.index(nearCities[i])] = True

        candidateList.append(candidate)

    candidateList.sort()
    return candidateList

def closestFacility(city, facilities):
    """
    Compares the parameter, city, with each facility to determine
    which facility it is closest to.
    """
    shortest = getDistance(facilities[0], city, data)
    nearFacility = facilities[0]
    for i in range(len(facilities)):
        if getDistance(facilities[i], city, data) < shortest:
            nearFacility = facilities[i]
            shortest = getDistance(facilities[i], city, data)
            
    return nearFacility 

def display(facilities, data):

    neighborsList = []

    # Creates a data strucute that contains the cities that each facility
    # can service. facilities[i] corresponds with neighborsList[i]
    for i in range(len(facilities)):
        nearFacilityList = []
        for j in range(len(data[0])):
            if facilities[i] == closestFacility(data[0][j], facilities):
                nearFacilityList.append(data[0][j])
        neighborsList.append(nearFacilityList)

    f = open("visualization800.kml", "w")
    
    # Header for the kml file
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    f.write('<Document>\n<Style id="smallLine">\n<LineStyle>\n<color>7f00007f</color>\n')
    f.write('<width>4</width>\n</LineStyle>\n<PolyStyle>\n<color>7f00007f</color>\n')
    f.write('</PolyStyle>\n</Style>\n\n')
    
    for i in range(len(facilities)):
 
        # Gets the coordniates of facilities[1], and adjusts the coordinates
        # to conform with the standard for the kml file
        cityName = facilities[i]
        population = str(data[2][data[0].index(cityName)])

        tmpXco = data[1][data[0].index(cityName)][0]
        tmpYco = data[1][data[0].index(cityName)][1]
        
        xco = '-' + str(tmpYco//100) + '.' + str(tmpYco%100)
        yco = str(tmpXco//100) + '.' + str(tmpXco%100)
        
        coordinates = xco + ',' + yco + ',0'
        
        # Adjusts the name of the city to conform with the 
        # formatting for a kml file
        city = facilities[i]
        state = city[len(city) - 2:]
        city = city[:len(city) - 3]        
        cityState = city + ', ' + state

        # writes to the kml file
        f.write('  <Placemark>\n')
        
        f.write('    <name>')
        f.write(cityState)
        f.write('</name>\n')
        
        f.write('    <description> Population as of 1949 ') 
        f.write(population)
        f.write('</description>\n')
        
        f.write('    <Point>\n')
        f.write('      <coordinates>')
        f.write(coordinates)
        f.write('</coordinates>\n')
        
        f.write('    </Point>\n')
        f.write('  </Placemark>\n\n')

        # This part is for the path line
        f.write('<Placemark>\n')
        f.write('<name>')
        f.write('Cities serviced by ')
        f.write(cityState)
        f.write('</name>\n')
        f.write('<description>')
        f.write('Path from ') 
        f.write(cityState)
        f.write(' to near cities')
        f.write('</description>\n')
        f.write('<styleUrl>#smallLine</styleUrl>\n<LineString>\n<extrude>1</extrude>\n')
        f.write('<tessellate>1</tessellate>\n<altitudeMode>absolute</altitudeMode>\n')
        f.write('<coordinates>\n')  

        # Uses the coordinates of each city to create the path from
        # facility[i] to each of the cities that it can service.
        nearCities = neighborsList[i]
        for j in range(0, len(nearCities)):
            nearCity = nearCities[j]
                        
            tmpNearXco = data[1][data[0].index(nearCity)][0]
            tmpNearYco = data[1][data[0].index(nearCity)][1]
            # Formats the coordinates to conform with the kml standards
            nearXco = '-' + str(tmpNearYco//100) + '.' + str(tmpNearYco%100)
            nearYco = str(tmpNearXco//100) + '.' + str(tmpNearXco%100)
            
            nearCo = nearXco + ',' + nearYco + ',0'
            
            f.write(nearCo)
            f.write('\n')
            
        # closing for path line
        f.write('</coordinates>\n</LineString>\n</Placemark>\n\n')

    f.write('</Document></kml>')
    f.close()
    # End of function "Display"
    
# Main
# Run with python3
# This program outputs a file called 'visualization800.kml'
data = createDataStructure()
facilities = locateFacilities(data, 800)
display(facilities, data)

