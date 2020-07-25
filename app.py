import appCore
import appTimers

import _thread

try:
	# Start GUI Thread
	_thread.start_new_thread(appCore.runGUI)
except:
	print("A GUI Thread failed")
	
try:
	# Start Timer Threads
	_thread.start_new_thread(appTimers.timedToggles, appCore.buttons[0], 8, 21, 15)
	_thread.start_new_thread(appTimers.timedToggles, appCore.buttons[0], 0, 24, 2)
except:
	print("A Timer Thread failed")

while True:
	pass
