#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Visualize steering goals for users of driving simulator

Author: Kyle Tanous & Aaron Richards
"""

from Tkinter import Tk, Frame, Canvas, BOTH
import serial, time

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")   

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Steering Data")
        self.pack(fill=BOTH, expand=1)     
        
class Incrementer:
    def __init__(self, val):
        self.val = val
        
    def inc(self):
        self.val = self.val + 1

    
i = Incrementer(0) 

def main():
    root = Tk()
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = 960, 540
    # get value from arduino
    # ser = serial.Serial('/dev/tty.usbserial', 9600)
    pos = 0
    root.overrideredirect(1)
    root.focus_set()
    root.bind("<Escape>", lambda e: e.widget.quit())
    root.geometry("%dx%d+300+300" % (w, h))
    canvas = Canvas(root, width=w, height=h, background="black")
    rect0 = canvas.create_rectangle(w/2-75, h/2-20, w/2+75, h/2+20, fill="#05f", outline="#05f")
    rect1 = canvas.create_rectangle(w/2-20, h/2-75, w/2+20, h/2+75, fill="#05f", outline="#05f")
    canvas.pack() 
    
    while (True):
        # gets angle and moves accordingly
        # pos = ser.readline()
        canvas.move(rect0, 1, 0)
        canvas.move(rect1, 1, 0)
        root.update()
        root.after(30)
      
    app = App(root)
    time.sleep(0.5)
    root.mainloop()  


if __name__ == '__main__':
    main()  