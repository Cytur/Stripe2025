class ObjectTimersClass:
    def __init__(self):
        self.ObjectsDictionary = {}
    
    def addObject(self, objectName, timeValue):
        self.ObjectsDictionary["Name"] = objectName
        self.ObjectsDictionary["DefaultTime"] = timeValue
        self.ObjectsDictionary["CurrentTime"] = timeValue
        
    def removeObject(self, objectName):
        self.ObjectsDictionary.pop(objectName)
    
    def getCurrentValue(self, objectName):
        return self.ObjectsDictionary[objectName]["CurrentTime"]
    
    #Adds pygame.time.tick to the CurrentTime (faster)
    def addTickTime(self, objectName, pygameTime):
        self.ObjectsDictionary[objectName]["CurrentTime"] = self.ObjectsDictionary[objectName]["DefaultTime"] + pygameTime
        
    def setToDefault(self, objectName):
        self.ObjectsDictionary[objectName] = self.ObjectsDictionary[objectName]["DefaultTime"]
        
    def setAllDefault(self):
        for i in range(0, len(self.ObjectsDictionary)):
            i["CurrentTime"] = i["DefaultTime"]
        

    