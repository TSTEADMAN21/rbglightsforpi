#Program asks for user input to determine color to shine.

import time, sys
# import RPi.GPIO as GPIO

leds = [
    {
        "red": [11], 
        "green": [13], 
        "blue": [15], 
        "yellow":[11, 13], 
        "cyan": [13, 15], 
        "magenta": [11, 15], 
        "white": [11, 13, 15]
    },
    {
        "red": [37], 
        "green": [35], 
        "blue": [33], 
        "yellow":[37, 35], 
        "cyan": [35, 33], 
        "magenta": [37, 33], 
        "white": [37, 35, 33]
    }
]

def togglePin(color, number, power):
    if not number.isnumeric():
        print("Invalid number")
        return

    num = int(number)
    
    if num >= len(leds) or num < 0:
        print("Invalid led number")
        return

    if color not in leds[num]:
        print("Invalid color")
        return

    pinNumbers = leds[num][color]

    if (power == "on"):
        blink(pinNumbers)
    elif (power == "off"):
        turnOff(pinNumbers)
    else:
        print("Invalid power command")


def blink(pins):
    for pin in pins:
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(pin, GPIO.OUT)
        # GPIO.output(pin, GPIO.HIGH)
        print("blink pin number: " + str(pin))

    
def turnOff(pins):
    for pin in pins:
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(pin, GPIO.OUT)
        # GPIO.output(pin, GPIO.LOW)
        print("turn off pin number: " + str(pin))
    
print("""Ensure the following GPIO connections: R-11, G-13, B-15
Colors: Red, Green, Blue, Yellow, Cyan, Magenta, and White
Use the format: color on/color off""")

def main():
    while True:
        cmd = input("-->")

        if cmd == "quit":
            break
        
        inputs = cmd.split()

        if len(inputs) == 3:
            color = inputs[0]
            number = inputs[1]
            power = inputs[2]
            togglePin(color, number, power)
        else:
            print("Invalid command")
    
    print("Program ended")

main()