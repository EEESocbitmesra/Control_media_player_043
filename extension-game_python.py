import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com16',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    
    if 'JUMP' in incoming:
	pyautogui.press('up')

    if 'RIGHT' in incoming:
	pyautogui.press('right')
  

    if 'LEFT' in incoming:
	pyautogui.press('left')

    if 'SKID' in incoming:
	pyautogui.press('down')

        
    incoming = "";
    
