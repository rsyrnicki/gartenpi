from tkinter import *
import tkinter.font
from functools import partial

import RPi.GPIO as GPIO

## Hardware ##
# 8 10 11 12 13 15 16 18
relayPins = [14, 15, 17, 18, 27, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for i in range(8):
	GPIO.setup(relayPins[i], GPIO.OUT)

## CONNECT BLUETOOTH ##
# Tutorial 1: http://www.python-exemplary.com/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/bluetooth.inc.php

# Or try PyBlueZ
# https://people.csail.mit.edu/albert/bluez-intro/c212.html

## TOGGLE VARIABLES ##
control = [True, True, True, True, True, True, True, True];
names = ["Basen", "Oczko", "Wtyczka_1", "Wtyczka_2", "Wtyczka_3", "Wtyczka_4", "Wtyczka_5", "Wtyczka_6"]
fullScreen = True;

## GUI Settings ##
root = Tk()
root.title("Automatyczny Ogrod")
font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes("-fullscreen", True)

## EVENT FUNCTIONS ##
def toggle(i):
    if control[i]:
        control[i] = False
        buttons[i]["text"] = "Wlacz " + names[i]
        GPIO.output(relayPins[i], GPIO.LOW)
    else:
        control[i] = True
        buttons[i]["text"] = "Wylacz " + names[i]
        GPIO.output(relayPins[i], GPIO.HIGH)
def close():
    RPi.GPIO.cleanup();
    root.destroy()
        

## WIDGETS ##
buttons = []
for i in range(8):
    button = Button(root, text = names[i], font=font, bg = "lightblue", height = h//5//10, width = w//4//10)
    buttons.append(button)
    toggle(i)
    buttons[i]["command"] = partial(toggle, i)
    if (i <= 3):
        button.grid(row = 2, column = i)
    else:
        button.grid(row = 4, column = i - 4)

exitButton =   Button(root, text = "Zakoncz", command = close, font=font, bg = "red", height = 1, width = w//4//10)
exitButton.grid(row = 5, column = 3)

root.protocol("WM_DELETE_WINDOW", close) # exit cleanly

#root.mainLoop()
