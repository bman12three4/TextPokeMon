import time
import math

import Adafruit_CharLCD as LCD
import fnc as fnc

lcd = LCD.Adafruit_CharLCDPlate()

prompt = False
clear = False
counter = 0
  
#Main Code
lcd.clear()
msgWait('Welcome to Text\nPokémon, 3)
msgWait('Version 0.0.2')
msgAnyKey('Press any key...')
msgAnyKey('Welcome to your\nnew home!')
msgAnyKey('Feel free to\nexplore!')
msgAnyKeyMultiLine('Wait! Pokémon\nmay be hiding in','the grass!')
msgAnyKeyMultiLine('I am professor\noak,','Pokémon Trainer')
msgAnyKeyMultiLine('I am a pokemon\nresearcher.)
msgAnyKeyMultiLine('Come to my Lab\nand let me show','you the world\nof PokéMon')
travelling(2)
