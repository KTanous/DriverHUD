#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Visualize steering goals for users of driving simulator

Author: Kyle Tanous
"""

from Tkinter import Tk, Frame, Canvas, BOTH


class Cross(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")   

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Steering Data")
        self.pack(fill=BOTH, expand=1)     


def main():

    root = Tk()
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = 1920, 1080
    # get value from arduino
    pos = 0
    root.geometry("%dx%d+300+300" % (w, h))
    canvas = Canvas(root, width=w, height=h, background="black")
    canvas.create_text(960, 540, text="+", fill="white")  
    canvas.create_rectangle(w/2-75+pos, h/2-20, w/2+75+pos, h/2+20, fill="#05f", outline="#05f")
    canvas.create_rectangle(w/2-20+pos, h/2-75, w/2+20+pos, h/2+75, fill="#05f", outline="#05f")
    canvas.pack() 
          
    app = Cross(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  