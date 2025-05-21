# ObjectTimersClass is meant to replace the "end_time_xyz" system we had before, since it was confusing and had a large margin for human error
class ObjectTimersClass:
    def __init__(self):
        self.ObjectsDictionary = {}
    
    #Add a new time counter with the specified name and default value
    def addObject(self, objectName, defaultTime):
        self.ObjectsDictionary[objectName] = {
            "Name": objectName,
            "DefaultTime": defaultTime,
            "CurrentTime": defaultTime
        }
    
    #Remove an object from the dictionary
    def removeObject(self, objectName):
        self.ObjectsDictionary.pop(objectName)
    
    #Return the current time value of the object
    def getCurrentValue(self, objectName):
        return self.ObjectsDictionary[objectName]["CurrentTime"]
    
    #Adds a specified to the CurrentTime (much faster than before)
    def addTime(self, objectName, timeToAdd):
        obj = self.ObjectsDictionary[objectName]
        obj["CurrentTime"] = timeToAdd
        
    #def setToDefault(self, objectName):
    #    self.ObjectsDictionary[objectName] = self.ObjectsDictionary[objectName]["DefaultTime"]
    
    #Used to reset all time values at the same time
    def setAllDefault(self):
        for obj in self.ObjectsDictionary.values():
            obj["CurrentTime"] = obj["DefaultTime"]
