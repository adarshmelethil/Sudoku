#!/usr/bin/env python

from tkinter import Frame, Label, CENTER, Entry

class TestFrame(Frame):

  def __init__(self):
    Frame.__init__(self)
    self.grid()

    Label(self, bg="#dd1b1b", text="Top Left", width=10, height=10).grid(row=0)
    Label(self, bg="#12b916", text="Bottom Left", width=10, height=10).grid(row=1)
    Label(self, bg="#12b916", text="Top Right", width=10, height=10).grid(row=0, column=1)
    Label(self, bg="#dd1b1b", text="Bottom Right", width=10, height=10).grid(row=1, column=1)
    
    
if __name__ == "__main__":
  TestFrame().mainloop()
