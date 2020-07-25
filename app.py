#!/usr/bin/python3

import threading
import time

import appCore
import appTimers

exitFlag = 0

class timerThread (threading.Thread):
   #def __init__(self, threadID, name, counter, btn, start, stop, interv):
	def __init__(self, threadID, name, counter, btn, start, stop, interv):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      #self.btn = btn
      #self.start = start
      #self.stop = stop
      #self.interv = interv
   def run(self):
      print ("Starting " + self.name)
      #appTimers.timedToggles(self.name, self.btn, self.start, self.stop, self.interv)
      appTimers.timedToggles(self.name, appCore.buttons[1], 0, 24, 2)
      print ("Exiting " + self.name)

# Create new threads
#threadTimer1 = timerThread(1, "Thread-1", 1, appCore.buttons[0], 8, 21, 15)
#threadTimer2 = timerThread(2, "Thread-2", 2, appCore.buttons[1], 0, 24, 2)
testThread = timerThread(1, "Thread-1", 1)

# Start new Threads
#threadTimer1.start()
#threadTimer2.start()
#threadTimer1.join()
#threadTimer2.join()
testThread.start()
testThread.join()

appCore.runGUI()

print ("Exiting Main Thread")
