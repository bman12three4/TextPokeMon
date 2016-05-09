import time
import math

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

prompt = False
clear = False

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
  
#For messages with more than three liens
def msgAnyKeyMultiLine(str1, str2):
  msgAnyKey(str1)
  lcd.show_cursor(True)
  msgAnyKey(str2)
  lcd.show_cursor(False)
  
#Main Code
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
msgAnyKeyMultiLine('Wait! Pokémon\nmay be hiding in','the grass!')
