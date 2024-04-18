import keyboard
import time

palavra = ''

while True:
    keyboard.press("o")
    time.sleep(2)
    keyboard.release("o")
    palavra += "o"
    time.sleep(2)
    keyboard.press("l")
    time.sleep(2)
    keyboard.release("l")
    palavra += "l"
    time.sleep(2)
    keyboard.press("a")
    time.sleep(2)
    keyboard.release("a")
    palavra += "a"

    if palavra == "ola":
        print(palavra, ' mundo!')
        break 
