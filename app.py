import appCore
import appTimers

import thread

try:
	# Start Threads
	thread.start_new_thread(appCore.runGUI)
	thread.start_new_thread(appTimers.timedToggles(appCore.buttons[0], 8, 21, 15))
	thread.start_new_thread(appTimers.timedToggles(appCore.buttons[0], 0, 24, 1))
except:
	print("A Thread failed")

while True:
	pass
