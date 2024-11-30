# Unit 16 - Object-Oriented Programming
# Assignment 2
# Submission 1

# If you are attempting to open this file from file explorer by double clicking it,
# this does not work everytime for some reason and you must open a terminal window and run
    # python trafficLights.py

import os
import sys
import time

try:
    import customtkinter as ctk
except:
    sys.exit(" Install customtkinter with Python3.10 pip or above")

from datetime import datetime

# If python version is less than 3.10
if sys.version_info[0] != 3 or sys.version_info[1] < 10:
    sys.exit(" Python 3.10 at least is required") # light.ctrl() -> match/case is >3.10


# Class for main graphical user interface rendering
class gui:
    def __init__(self):
        self.window = ctk.CTk()
        # UI colours
        self.black = "#151515"
        self.grey = "#656565"
        self.white = "#F9F9F9"
        self.red = "#AD1818"

    def build(self, accessMain):
        self.window.title("U16-A2-S1 // Object-Oriented Programming")
        self.window.geometry("450x280")
        self.window.protocol("WM_DELETE_WINDOW", self.close) # Custom close action on window X button
        self.window.resizable(False, False)
        ctk.set_appearance_mode("dark")
        self.toggleBtn = ctk.CTkButton(master=self.window, text="Force Toggle", command=accessMain.forceToggle, corner_radius=5, width=350,
                                       fg_color=self.grey, text_color=self.black, hover_color=self.red)
        self.lightHousing = ctk.CTkFrame(self.window, width=100, height=200, fg_color=self.black, corner_radius=5, border_color=self.grey, border_width=1)
        self.lightHousing2 = ctk.CTkFrame(self.window, width=100, height=200, fg_color=self.black, corner_radius=5, border_color=self.grey, border_width=1)

    def pack(self):
        self.toggleBtn.place(relx=0.1, rely=0.825)     # Magic numbers
        self.lightHousing.place(relx=0.1, rely=0.04)   # lmaoooooooooo
        self.lightHousing2.place(relx=0.65, rely=0.04) # this is so fun

    def close(self):
        os._exit(0) # Forced termination to avoid tkinter buffer on close


# Class for controlling and rendering bulbs
class light():
    def __init__(self):
        # Access to gui()'s CTK window controller
        self.windowAccess = None
        # Which light to control
        self.controlling = None
        # Bulb status
        self.status = {"TOP": False, "MIDDLE": False, "BOTTOM": False}
        # Bulb state
        self.state: None
        # Bulb colours
        self.bulbR = {True: "#f21f1f", False: "#500D0D"}
        self.bulbA = {True: "#f5a214", False: "#412D0B"}
        self.bulbG = {True: "#54f018", False: "#133009"} # fg_color=self.bulbG[self.status["TOP"]] # True/False - #54f018/#133009
        # Bulb co-ordinate
        self.x = None
    
    def start(self, winCtrl: None, who: int, state: int):
        self.windowAccess = winCtrl
        self.controlling = who
        self.state = state
        if self.controlling == 1:
            self.x = 0.155
        if self.controlling == 2:
            self.x = 0.705
        self.set(forced=True)

    def set(self, forced: bool):
        match self.state:
            case 1:
                self.status["TOP"] = True
                self.status["MIDDLE"] = False
                self.status["BOTTOM"] = False
            case 2:
                self.status["TOP"] = True
                self.status["MIDDLE"] = True
                self.status["BOTTOM"] = False
            case 3:
                self.status["TOP"] = False
                self.status["MIDDLE"] = False
                self.status["BOTTOM"] = True
            case 4:
                self.status["TOP"] = False
                self.status["MIDDLE"] = True
                self.status["BOTTOM"] = False
        if not forced:
            self.cycle(forced=False)
        self.update()
    
    def cycle(self, forced: bool):
        self.state = self.state + 1
        if self.state > 4:
            self.state = 1
        if forced:
            self.set(forced=True)
    
    def update(self):
        print(f" [{datetime.now().strftime('%H:%M:%S')}]-[L{self.controlling}]-[Top: {self.status['TOP']}]-[Middle: {self.status['MIDDLE']}]-[Bottom: {self.status['BOTTOM']}]")
        # Config bulb activity
        self.top = ctk.CTkFrame(self.windowAccess, width=50, height=50, fg_color=self.bulbR[self.status["TOP"]], bg_color="#151515", corner_radius=30)
        self.middle = ctk.CTkFrame(self.windowAccess, width=50, height=50, fg_color=self.bulbA[self.status["MIDDLE"]], bg_color="#151515", corner_radius=30)
        self.bottom = ctk.CTkFrame(self.windowAccess, width=50, height=50, fg_color=self.bulbG[self.status["BOTTOM"]], bg_color="#151515", corner_radius=30)
        # Render new bulbs config
        self.top.place(relx=self.x, rely=0.1)
        self.middle.place(relx=self.x, rely=0.3)
        self.bottom.place(relx=self.x, rely=0.5)
        

# Main run loop
class main:
    def __init__(self):
        # Instances of classes
        self.L1 = light()
        self.L2 = light()
        self.ui = gui()
        # Variables
        self.stamp = time.time().__round__()
        self.output = None

    def start(self):
        self.ui.build(self)
        self.ui.pack()
        self.L1.start(self.ui.window, 1, 1) # Light 1 - State 1 (Top: Off / Middle: Off / Bottom: On)
        self.L2.start(self.ui.window, 2, 3) # Light 2 - State 3 (Top: On / Middle: Off / Bottom: Off)
        self.main()

    def main(self):
        while True:
            self.ui.window.update()
            if time.time().__round__() >= self.stamp + 4:
                self.L1.set(forced=False)
                self.L2.set(forced=False)
                self.stamp = time.time().__round__()
            time.sleep(0.033) # 33 millisecond sleep to limit programme to 30 frames per second

    def forceToggle(self):
        self.L1.cycle(forced=True)
        self.L2.cycle(forced=True)
        print(f" [{datetime.now().strftime('%H:%M:%S')}]-[++]-[Force toggled lights]")


try:
    if "__main__" == __name__:
        main().start()
except KeyboardInterrupt:
    sys.exit(" CTRL+C Pressed")