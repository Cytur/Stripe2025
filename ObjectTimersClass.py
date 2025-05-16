class ObjectTimersClass:
    def __init__(self):
        self.ObjectsDictionary = {}
    
    #Add a new time counter with the specified name and default value
    def addObject(self, objectName, timeValue):
        self.ObjectsDictionary["Name"] = objectName
        self.ObjectsDictionary["DefaultTime"] = timeValue
        self.ObjectsDictionary["CurrentTime"] = timeValue
    
    #Remove a timer from the dictionary
    def removeObject(self, objectName):
        self.ObjectsDictionary.pop(objectName)
    
    #Return the current time value of the object
    def getCurrentValue(self, objectName):
        return self.ObjectsDictionary[objectName]["CurrentTime"]
    
    #Adds a specified to the CurrentTime (much faster than before)
    def addTime(self, objectName, timeToAdd):
        self.ObjectsDictionary[objectName]["CurrentTime"] = self.ObjectsDictionary[objectName]["DefaultTime"] + timeToAdd
        
    #Adds the default time to the CurrentTime         **************************************************
    def addDefaultTime(self, objectName, timeToAdd):
        self.ObjectsDictionary[objectName]["CurrentTime"] = self.ObjectsDictionary[objectName]["DefaultTime"] + timeToAdd
        
    #def setToDefault(self, objectName):
    #    self.ObjectsDictionary[objectName] = self.ObjectsDictionary[objectName]["DefaultTime"]
    
    #Used to reset all time values at the same time
    def setAllDefault(self):
        for i in range(0, len(self.ObjectsDictionary)):
            i["CurrentTime"] = i["DefaultTime"]
        

    