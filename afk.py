from pynput.keyboard import Key, Controller, Listener
from win32 import win32gui
import keyboard
import time
from random import randrange
import random


def intervalo():
    interval = (random.randint(10,20))
    print(interval)
    return interval


def antiafk():
    
    whnd = win32gui.FindWindow( None, 'World of Warcraft',)
    print(whnd)
    time.sleep(2)
    win32gui.SetForegroundWindow(whnd)
    win32gui.SetActiveWindow(whnd)

    keyboard = Controller()

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press('/')
    keyboard.release('/')
    time.sleep(1)
    keyboard.press('d')
    keyboard.release('d')
    time.sleep(1)
    keyboard.press('a')
    keyboard.release('a')
    time.sleep(1)
    keyboard.press('n')
    keyboard.release('n')
    time.sleep(1)
    keyboard.press('c')
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('e')
    keyboard.release('e')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


while True:
    antiafk()
    numero = intervalo()
    time.sleep(numero)  
   
    

