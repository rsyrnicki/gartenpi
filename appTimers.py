import appCore
import time

def timedToggles(button, startH, endH, interval):
	toggled = True
	
	while True:
		t = time.localtime()
		hours = int(time.striftime("%H", t))
		minutes = int(time.strftime("%M", t))
		seconds = int(time.strftime("%S", t))
		# Potentiall error, because I might have messed something up
		if (minutes%interval == 0 && hours >= startH && hours <= endH && !toggled):
			button.invoke()
			toggled = True
		# Potentiall error, because I might have messed something up
		elif (minutes%interval == 0 && hours >= startH && hours <= endH && toggled):
			toggled = True
		else:
			toggled = False
