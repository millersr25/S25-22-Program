#-----------------------------------------------
# GUI to turn ON/OFF Solar Energy Harvester
# and Monitor the LIPO Battery voltage
#-----------------------------------------------
import tkinter as tk
from pyfirmata import Arduino
import time
#===============================================
# Functions
#-----------
def SendStartUpVoltage():
    board.digital[2].write(1)   # turn Digital Pin 2 ON
    time.sleep(3)   # 3 seconds
    board.digital[2].write(0)   # turn Digital Pin 2 OFF
def StartCharging():
    board.digital[3].write(1)   # turn Digital Pin 3 ON
def StopCharging():
    board.digital[3].write(0)   # turn Digital Pin 3 OFF
#===============================================
# Arduino board connected to serial port COM3
board = Arduino("COM3")

# Root widget to create window
win = tk.Tk()
# initialize window with title & minimum size
win.title("L E D")
win.minsize(200,60)