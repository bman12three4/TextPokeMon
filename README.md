# TextPokeMon
for the adafruit 16x2 LCD

The goal of this project is to get a playable version of Pokémon Blue that can be played with just text. It will have have some animations, but only very simple ones, such as a loading screen, or a battle animation with little circles. Perhaps in the future I will look into makeing custom characters for better animations using bitmaps, but for now regular ASCII will do the trick.

The pokemon.py is the main file with all of the code that is run by the raspberry pi. The fnc.py is the code with all of the modules in it that are run by the main program. If any modules are added, they are added to fnc.py, and are used by doing fnc.*, with * being the name of your module in fnc.py.

Currently all of the functions are for displaying text, and one is used for a basic loading animation, with an elipses that grows and deletes itself. Most modules have a comment explaining what they do, but their names are somewhat intuitive.

Hope you have fun,
  ~bman12three4
