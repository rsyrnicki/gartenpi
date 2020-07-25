#!/usr/bin/python3

import threading
import time

import appCore
import appTimers

exitFlag = 0

class guiThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      appCore.runGUI()
      print ("Exiting " + self.name)

class timerThread (threading.Thread):
   def __init__(self, threadID, name, counter, btn, start, stop, interv):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.btn = btn
      self.start = start
      self.stop = stop
      self.interv = interv
   def run(self):
      print ("Starting " + self.name)
      appTimers.timedToggles(self.btn, self.start, self.stop, self.interv)
      print ("Exiting " + self.name)

appCore.runGUI()

# Create new threads
#threadGUI = guiThread(1, "Thread-1", 1)
threadTimer1 = timerThread(2, "Thread-2", 2, appCore.buttons[0], 8, 21, 15)
threadTimer1 = timerThread(3, "Thread-3", 3, appCore.buttons[1], 0, 24, 2)

# Start new Threads
#threadGUI.start()
threadTimer1.start()
threadTimer2.start()
#threadGUI.join()
threadTimer1.join()
threadTimer2.join()
print ("Exiting Main Thread")
