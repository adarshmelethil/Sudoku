#!/usr/bin/env python

from tkinter import Frame, Label, CENTER, Entry


cell_width = 10
cell_height = 10
class TestFrame(Frame):

  def __init__(self):
    Frame.__init__(self)
    self.grid()

    background = Frame(self, bg="#ff00ff", width=30, height=30)
    background.grid(row=0, column=0)

    Label(background, bg="#dd1b1b", text="Top Left", width=cell_width, height=cell_height).grid(row=0)
    Label(background, bg="#12b916", text="Bottom Left", width=cell_width, height=cell_height).grid(row=1)
    Label(background, bg="#12b916", text="Top Right", width=cell_width, height=cell_height).grid(row=0, column=1)
    Label(background, bg="#dd1b1b", text="Bottom Right", width=cell_width, height=cell_height).grid(row=1, column=1)

    SideBar = Frame(self, bg="#00ff00", width=30, height=30)
    SideBar.grid(row=0, column=1)
    Label(SideBar, bg="#000000", width=cell_height, height=cell_height).grid(row=0, column=0)

    
if __name__ == "__main__":
  TestFrame().mainloop()
