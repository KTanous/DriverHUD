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

        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80, 
                                    outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80, 
                                    outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80, 
                                    outline="#05f", fill="#05f")            
        canvas.pack(fill=BOTH, expand=1)        


def main():

    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+300+300" % (w, h))
    app = Cross(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  