"""
Pokemon Text Adventure
Copyright (C) 2016  Byron Lathi
"""

#defines functions for use in the other files.
import time
import math

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

prompt = False
clear = False
counter = 0

prompt = False
clear = False
counter = 0

#Pauses the program until any of the keys are pressed.
def anyKey():
  prompt = True
  while prompt:
    if lcd.is_pressed(LCD.SELECT):
     prompt = False
    if lcd.is_pressed(LCD.UP):
     prompt = False
    if lcd.is_pressed(LCD.DOWN):
      prompt = False
    if lcd.is_pressed(LCD.LEFT):
      prompt = False
    if lcd.is_pressed(LCD.RIGHT):
      prompt = False
return

#Lists one screen (two lines) and waits for any of the 5 keys to be pressed
def msgAnyKey(str):
  lcd.message(str)
  anyKey()
  lcd.clear()
  
#lists one screen and waits for the input seconds
def msgWait(str, int):
  lcd.message(str)
  time.sleep(int)
  lcd.clear()
  
#For messages with more than three liens
def msgAnyKeyMultiLine(str1, str2):
  msgAnyKey(str1)
  lcd.show_cursor(True)
  msgAnyKey(str2)
  lcd.show_cursor(False)

#says travelling followed by an elipses that grows and then deletes itself. Time is one second times input.
def travelling(int):
  counter = 0
  while counter < int:
    lcd.message('Travelling')
    time.sleep(0.25)
    lcd.message('.')
    time.sleep(0.25)
    lcd.message('.')
    time.sleep(0.25)
    lcd.message('.')
    time.sleep(0.25)
    lcd.clear()
    counter = counter + 1
