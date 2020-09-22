import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com16',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.press('space')

    if 'Slow' in incoming:
        pyautogui.hotkey('ctrl','shift', 's')  

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl','shift', 'g') 

    if 'Vup' in incoming:
        pyautogui.scroll(50)
        
    if 'Vdown' in incoming:
        pyautogui.scroll(-100)

    incoming = "";
    
