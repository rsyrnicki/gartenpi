import tkinter as tk
import tkinter.font
from functools import partial

import time

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
font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

## EVENT FUNCTIONS ##
def toggle(i):
    if control[i]:
        control[i] = False
        buttons[i]["text"] = "Wlacz " + names[i]
        buttons[i]["bg"] = "red"
        buttons[i]["activeforeground"] = "red"
        GPIO.output(relayPins[i], GPIO.HIGH)
    else:
        control[i] = True
        buttons[i]["text"] = "Wylacz " + names[i]
        buttons[i]["bg"] = "green"
        buttons[i]["activeforeground"] = "green"
        GPIO.output(relayPins[i], GPIO.LOW)

def close():
    GPIO.cleanup();
    root.destroy()
    
## WIDGETS ##
buttons = []
for i in range(8):
    button = tk.Button(root, text = names[i], font=font, bg = "red", height = h//5//10, width = w//4//10)
    buttons.append(button)
    toggle(i)
    buttons[i]["command"] = partial(toggle, i)
    if (i <= 3):
        button.grid(row = 2, column = i)
    else:
        button.grid(row = 4, column = i - 4)

exitButton = tk.Button(root, text = "Zakoncz", command = close, font=font, bg = "red", height = 1, width = w//4//10)
exitButton.grid(row = 5, column = 3)

root.protocol("WM_DELETE_WINDOW", close) # exit cleanly

# Potentiall error, because I don't fully understand how it works
def runGUI():
	while True:
		root.update_idletasks()
		root.update()
