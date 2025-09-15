import RPi.GPIO as GPIO
from pad4pi import rpi_gpio
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Setup keypad layout
KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

# Define GPIO pins for rows and columns
ROW_PINS = [5, 6, 13, 19]  # BCM numbers
COL_PINS = [26, 16, 20]    # BCM numbers

# Initialize GPIO and keypad
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# Function to handle password input (including * key and 0.5s delay between key presses)
def getData1():
    container = ""
    print("Enter password (Press '#' to finish): ", end="")
    while True:
        key = keypad.getKey()
        if key is not None:
            if key == '#':  # '#' to end input
                break
            elif key.isdigit() or key == '*':  # Accept digits and '*' key
                container += key
                print(key, end="", flush=True)  # Display key in terminal
            else:
                # Ignore non-numeric, non-* keys
                pass
            time.sleep(0.5)  # Add a 0.5s delay after each key press
    print()  # For a clean line after password input
    return container  # Return the entered password
