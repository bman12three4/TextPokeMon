import time
import math

import Adafruit_CharLCD as LCD
import fnc as fnc

lcd = LCD.Adafruit_CharLCDPlate()
  
#Main Code
print("This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type `show c' for details.")
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
fnc.msgAnyKeyMultiLine('Welcome to my\nlab! Here we','research Pokémon.')
fnc.msgAnyKeyMultiLine('Pokemon are\nusefull for','everyone! you\nshould get one!')
fnc.msgAnyKeyMultiLine('I happen to have\nthree pokemon','That you can\npick from')
fnc.choose('Bulbasaur', 'Squirtle', 'Charmander')
