#
# hello_kid.py -- Display a text-based "Hello, World!" message on a
# WaveShare RP2040 Touch LCD 1.28B running MicroPython. 
#
# 2024 - Jon Eby - https://github.com/kaff1

# This part of the file is called our 'imports'. It's how we tell
# this Python file about other files or pieces of the MicroPython
# platform we need it to know about for our code to work.

import rp2040lcd

# Here we're going to set how bright we want the screen to be and
# then get access to the LCD screen from the rp2040lcd.py file that
# we imported above. If you look at ViperIDE's file manager on the
# left you can see where rp2040lcd.py is stored and look at the
# code yourself!
STARTING_BRIGHTNESS = 45055
LCD = rp2040lcd.LCD_1inch28()
LCD.set_bl_pwm(STARTING_BRIGHTNESS)

# Now that we've set the screen's brightness let's do some setup
# for the text we're going to display on the screen:
CHARS_PER_LINE = 14
MAX_LINES = 7

LINE_HEIGHT = 20
CHAR_WIDTH = 8

BACKGROUND_COLOUR = LCD.black
TEXT_COLOUR = LCD.white

# We just want our device to do the same thing forever, so we'll tell it
# to keep running all the code from after the 'while' statement below. 
# A 'while' statement is a way for us to say "Keep 
# doing this as long as Condition A is equal to Condition B". The 'while True:'
# statement below is a shortcut to say "Do this as long as True is equal to True".
# This statement will always be true, so the code will just keep running.
while True:
    # Before we try to display any text, let's set the screen to black:
    LCD.fill_rect(0,0,240,240,LCD.black)

    # Here's the text we'll display on the screen. How can we customize it?
    LCD_TEXT = "Hello, Kid!"

    # What does all this even mean?! What are those numbers? Let's look
    # at line 375 of rp2040lcd.py to find out!
    LCD.write_text(LCD_TEXT, 0, 112, 2, TEXT_COLOUR)

    LCD.show()