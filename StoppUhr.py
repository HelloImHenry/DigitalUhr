
class StoppUhr:
    timeFormat = ""
    time = [0,0,0]
    active = True
    def __init__(self):
        None
    def updateTime(self):
        #Der Code zum aktualisieren der Zeit wird nur ausgeführt, wenn der Timer aktiv ist.
        if self.active == True:
            if self.time[2] >= 59:
                self.time[2] = 0
                if self.time[1] == 59:
                    if self.time[0] >= 99:
                        self.time[0] = 0
                    else:
                        self.time[0]+=1
                        self.time[1] = 0
                else:
                    self.time[1]=self.time[1]+1
            else:
                self.time[2]=self.time[2]+1
        self.timeFormat = ""
        for x in range(len(self.time)):
            if self.time[x] < 10:
                self.timeFormat = self.timeFormat + "0" + str(self.time[x])+":"
            else:
                self.timeFormat = self.timeFormat + str(self.time[x])+":"
        #Der letzte char wird entfernt, da er ein Doppelpunkt ist und zu viel ist :)
        self.timeFormat = self.timeFormat[:-1]
    def resumeStoppuhr(self):
        self.active = True
    def pauseStoppuhr(self):
        self.active = False
    """def resumeStoppuhr(self):
        self.active = True
        while not self.stopped.wait(0.5):
            print("my thread")
            self.updateTime()"""
    def setTime(self, array):
        self.time[0] = array[0]
        self.time[1] = array[1]
        self.time[2] = array[2]
    """def pauseStoppuhr(self):
        self.active = False
        stopFlag = Event()
        thread = StoppUhr(stopFlag)
        thread.start()
        # this will stop the timer
        stopFlag.set()"""
    def resetStoppuhr(self):
        self.time = 0
    
   
    
    
    