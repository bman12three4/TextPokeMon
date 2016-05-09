import time
import math

import Adafruit_CharLCD as LCD
import fnc as fnc

lcd = LCD.Adafruit_CharLCDPlate()
  
#Main Code
lcd.clear()
fnc.msgWait('Welcome to Text\nPokémon, 3)
fnc.msgWait('Version 0.0.3')
fnc.msgAnyKey('Press any key...')
fnc.msgAnyKey('Welcome to your\nnew home!')
fnc.msgAnyKey('Feel free to\nexplore!')
fnc.msgAnyKeyMultiLine('Wait! Pokémon\nmay be hiding in','the grass!')
fnc.msgAnyKeyMultiLine('I am professor\noak,','Pokémon Trainer')
fnc.msgAnyKeyMultiLine('I am a pokemon\nresearcher.)
fnc.msgAnyKeyMultiLine('Come to my Lab\nand let me show','you the world\nof PokéMon')
fnc.travelling(2)
