import appCore
import time

def timedToggles(threadName, button, startH, endH, interval):
	toggled = True
	
	while True:
		if appCore.exitFlag:
			threadName.exit()
		t = time.localtime()
		hours = int(time.striftime("%H", t))
		minutes = int(time.strftime("%M", t))
		seconds = int(time.strftime("%S", t))
		# Potentiall error, because I might have messed something up
		if (minutes%interval == 0 and hours >= startH and hours <= endH and not toggled):
			button.invoke()
			toggled = True
			print("Invoked a button!")
		# Potentiall error, because I might have messed something up
		elif (minutes%interval == 0 and hours >= startH and hours <= endH and toggled):
			toggled = True
		else:
			toggled = False
		time.wait(15)
