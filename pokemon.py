import time
import math

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

prompt = False
clear = False

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

def msgAnyKey(str):
  lcd.message(str)
  anyKey()
  lcd.clear()

lcd.clear()
lcd.message('Welcome to Text\nPokémon!')
time.sleep(3)
lcd.clear()
lcd.message('Version 0.0.1')
time.sleep(1)
lcd.clear()
msgAnyKey('Press any key...')
msgAnyKey('Welcome to your\nnew home!')
msgAnyKey('Feel free to\nexplore!')
lcd.message('Wait! Pokémon\nmay be hiding in')
lcd.show_cursor(True)
anyKey()
lcd.clear()
lcd.message('the grass!')
