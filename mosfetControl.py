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
def ReadLIPOVoltage(): 
    rawValue = board.analog[0].read() # directly read from the A0 pin
    if rawValue is not None:
        lipoVoltage = rawValue * 5.0 
        return lipoVoltage
    else:
        return None
#===============================================
# Arduino board connected to serial port COM3
board = Arduino("COM3")

# Root widget to create window
win = tk.Tk()
# initialize window with title & minimum size
win.title("Solar Harvester Program")
win.minsize(200,60)

# Label widget
label = tk.Label(win, text="click to turn ON/OFF")
label.grid(column=1, row=1)

# Button widget
ONbtn = tk.Button(win, bd=4, text="LED ON", command=SendStartUpVoltage)
ONbtn.grid(column=1, row=2)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=StopCharging)
OFFbtn.grid(column=2, row=2)

# start & open window continously
win.mainloop()
