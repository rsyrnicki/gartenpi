import tkinter as tk
import tkinter.font
from functools import partial

import time
import threading
import sys
import RPi.GPIO as GPIO

## Hardware ##
# 8 10 11 12 13 15 16 18
relayPins = [14, 15, 17, 18, 27, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for i in range(8):
	GPIO.setup(relayPins[i], GPIO.OUT)


## TOGGLE VARIABLES ##
control = [True, True, True, True, True, True, True, True];
names = ["Basen", "Oczko", "Wtyczka_1", "Wtyczka_2", "Wtyczka_3", "Wtyczka_4", "Wtyczka_5", "Wtyczka_6"]


## GUI Settings ##
root = tk.Tk()
root.title("Automatyczny Ogrod")
font = tkinter.font.Font(family = "Helvetica", size = 36, weight = "bold")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


## EVENT FUNCTIONS ##
def toggle(i):
    if control[i]:
        control[i] = False
        buttons[i]["text"] = "Wlacz " + names[i]
        buttons[i]["bg"] = "red"
        buttons[i]["activebackground"] = "red"
        GPIO.output(relayPins[i], GPIO.HIGH)
    else:
        control[i] = True
        buttons[i]["text"] = "Wylacz " + names[i]
        buttons[i]["bg"] = "green"
        buttons[i]["activebackground"] = "green"
        GPIO.output(relayPins[i], GPIO.LOW)
    
def close():
	GPIO.cleanup();
	root.destroy()
	sys.exit()
 
       
## WIDGETS ##
buttons = []
for i in range(8):
	button = tk.Button(root, text = names[i], font=font, bg = "red", height = 9, width = 17)
	buttons.append(button)
	toggle(i)
	buttons[i]["command"] = partial(toggle, i)
	if (i <= 3):
		button.grid(row = 2, column = i)
	else:
		button.grid(row = 4, column = i - 4)

exitButton = tk.Button(root, text = "Zakoncz", command = close, font=font, bg = "red", height = 1, width = 17)
exitButton.grid(row = 5, column = 3)

root.protocol("WM_DELETE_WINDOW", close) # exit cleanly


## TIMER FUNCTION ##
def timedToggles(threadName, button, startH, endH, interval):
	toggled = True
	
	while True:
		print("Timer Thread")
		global exitFlag
		hours = int(time.localtime()[3])
		minutes = int(time.localtime()[4])
		seconds = int(time.localtime()[5])
		if (minutes%interval == 0 and hours >= startH and hours <= endH and not toggled):
			button.invoke()
			toggled = True
			print("A button has been pressed automaticaly!")
		elif (minutes%interval == 0 and hours >= startH and hours <= endH and toggled):
			toggled = True
		else:
			toggled = False
		time.sleep(30)
		
		
## MULTITHREADING ##
class timer1Thread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting " + self.name)
		timedToggles(self.name, buttons[0], 8, 21, 15)
		print ("Exiting " + self.name)

print("Loading classes")

class timer2Thread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting " + self.name)
		timedToggles(self.name, buttons[1], 8, 22, 1)
		print ("Exiting " + self.name)
		
# Create new threads
threadTimer1 = timer1Thread(1, "Thread-1", 1)
threadTimer2 = timer2Thread(2, "Thread-2", 2)


## START THREADS ##
threadTimer1.daemon = True
threadTimer2.daemon = True
threadTimer1.start()
threadTimer2.start()
root.mainloop()