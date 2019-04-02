#!/usr/bin/env python

from tkinter import Frame, Label, CENTER

import constants as c
import logic as l

class GameGrid(Frame):

  def __init__(self):
    Frame.__init__(self)
    self.grid()

    self.master.title("Sudoku")
    self.master.bind("<Key>", self.keyDown)
    
    self.master.bind('<Button-1>', self.mouseClick)

    # Numbers
    self.grid_values = l.baseGrid()
    # Labels
    self.grid_cells = []
    

    self.swap_state = {
      "mode": None,
      "values": None,
    }

    self.history = []

    self.initGrid()
    self.updateGrid()

  def initGrid(self):
    background = Frame(self, 
      bg=c.BACKGROUND_COLOR_GAME,
      width=c.SIZE,
      height=c.SIZE,
    )
    background.grid()
    zones = []
    for i in range(3):
      h_zones = []
      for j in range(3):
        zone = Frame(background,
          bg=c.BACKGROUND_ZONE[(i+j)%2],
          width=c.SIZE/3,
          height=c.SIZE/3,
        )
        zone.grid(
          row=i,
          column=j,
        )
        h_zones.append(zone)
      zones.append(h_zones)

    for i in range(9):
      grid_row = []
      for j in range(9):
        cell = Frame(zones[i//3][j//3], 
          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
          width=c.SIZE/9,
          height=c.SIZE/9,
        )
        cell.grid(
          row=i,
          column=j,
          padx=c.GRID_PADDING,
          pady=c.GRID_PADDING,
        )
        t = Label(master=cell, 
          text="",
          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
          justify=CENTER, font=c.FONT, 
          width=c.LABEL_WIDTH, height=c.LABEL_HEIGHT
        )
        t.cell = (i, j)
        t.grid()
        grid_row.append(t)
      self.grid_cells.append(grid_row)

  def updateGrid(self):
    print("Updating Grid")
    hc, vc, zc = l.validGrid(self.grid_values)
    for i in range(9):
      for j in range(9):
        if self.grid_values[i][j] == 0:
          self.grid_cells[i][j].configure(
            text="",
            bg=c.BACKGROUND_COLOR_CELL_EMPTY,
          )
        else:
          if self.swap_vals[0] == (i, j) or self.swap_vals[1] == (i, j):
            backgroundColor = c.BACKGROUND_SELECT
          else:
            if (i, j) in hc:
              backgroundColor = c.COLOR_ERROR[0]
            elif (i, j) in vc:
              backgroundColor = c.COLOR_ERROR[1]
            elif (i, j) in zc:
              backgroundColor = c.COLOR_ERROR[2]
            else:
              backgroundColor = c.BACKGROUND_COLOR_NUM[self.grid_values[i][j]-1]
          self.grid_cells[i][j].configure(
            text=str(self.grid_values[i][j]),
            bg=backgroundColor,
            fg=c.CELL_COLOR,
          )
    self.update_idletasks()

  def swapVal(self, undo=False):
    if self.swap_state["mode"] is None:
      print("Missing swap mode")
      return
    if self.swap_state["values"] is None:
      print("Missing values")
      return
    
    

    if self.swap_vals[0] is None or self.swap_vals[1] is None:
      print("selcect values to swap")
      return

    conflict = None
    if self.swap_vals[0][0] == self.swap_vals[1][0]:
      if not undo:
        self.history.append([self.swap_vals[0], self.swap_vals[1]])
      conflict = l.hSwapVal(self.grid_values, self.swap_vals[0], self.swap_vals[1])
      if conflict is None:
        print("No conflict")
        self.swap_vals = [None, None]
        self.updateGrid()
        return

      otherVal = self.grid_values[self.swap_vals[0][0]][self.swap_vals[0][1]]
      otherCoor = None
      for i in range(9):
        if i == self.swap_vals[0][1]:
          continue
        if self.grid_values[conflict[0]][i] == otherVal:
          otherCoor = (conflict[0], i)
      if otherCoor is None:
        print("could not find other val '{}' in row '{}'".format(otherVal, conflict[0]))
        self.swap_vals = [None, None]
      self.swap_vals = [conflict, otherCoor]

    elif self.swap_vals[0][1] == self.swap_vals[1][1]:
      if not undo:
        self.history.append([self.swap_vals[0], self.swap_vals[1]])
      conflict = l.vSwapVal(self.grid_values, self.swap_vals[0], self.swap_vals[1])
      if conflict is None:
        print("No conflict")
        self.swap_vals = [None, None]
        self.updateGrid()
        return

      otherVal = self.grid_values[self.swap_vals[0][0]][self.swap_vals[0][1]]
      otherCoor = None
      for i in range(9):
        if i == self.swap_vals[0][1]:
          continue
        if self.grid_values[i][conflict[1]] == otherVal:
          otherCoor = (i, conflict[1])
      if otherCoor is None:
        print("could not find other val '{}' in col '{}'".format(otherVal, conflict[1]))
        self.swap_vals = [None, None]
        self.updateGrid()
        return
      self.swap_vals = [conflict, otherCoor]
    else:
      print("Swap not implemented")
    
    self.updateGrid()

    print("conflict: {}".format(self.swap_vals))
    # l.printGrid(self.grid_values)

  def mouseClick(self, event):
    if type(event.widget) is Label:
      label = event.widget
      if self.swap_vals[0] is None:
        self.swap_vals = [(label.cell[0], label.cell[1]), None]
      elif self.swap_vals[1] is None:
        if self.swap_vals[0] != (label.cell[0], label.cell[1]):
          self.swap_vals[1] = (label.cell[0], label.cell[1])
      else:
        self.swap_vals = [(label.cell[0], label.cell[1]), None]
      print('{}'.format(self.swap_vals))
      self.updateGrid()

  def keyDown(self, event):
    key = event.char
    if key == 's':
      print("Swaping")
      self.swapVal()
    elif key == 'z':
      if self.history:
        undoVal = self.history.pop()
        self.swap_vals = undoVal
        print("Undo: {}".format(self.swap_vals))
        self.swapVal(undo=True)
        self.swap_vals = undoVal
        self.updateGrid()

    elif key == 'h':
      print(self.history)
    elif key == 'e':
      rows = []
      for i in range(9):
        row = "["+", ".join([str(c) for c in self.grid_values[i]])+"]"
        rows.append(row)
      print("[\n"+",\n".join(rows)+",\n]")

if __name__ == "__main__":
  # baseGrid = l.baseGrid()
  # l.printGrid(baseGrid)

  # for i in range(9):
  #   print(l.horizontalConflict(baseGrid, i))
  #   print(l.verticalConflict(baseGrid, i))

  # print("-"*20)

  # randGrid = /.randomGrid()
  # l.printGrid(randGrid)

  # for i in range(9):
  #   print("H:", /.horizontalConflict(randGrid, i))
  #   print("V:", /.verticalConflict(randGrid, i))

  # for i in range(3):
  #   for j in range(3):
  #     print("Z({},{}):".format(i,j), /.zoneConflict(randGrid, i, j))
  a = [
    [1, 2, 3, 7, 8, 9, 4, 5, 6],
    [8, 5, 6, 1, 2, 3, 7, 4, 9],
    [7, 8, 9, 4, 5, 6, 1, 2, 3],
    [3, 1, 2, 9, 7, 4, 6, 8, 5],
    [6, 4, 5, 3, 1, 2, 9, 7, 8],
    [9, 7, 8, 6, 4, 5, 3, 1, 2],
    [2, 3, 1, 8, 9, 7, 5, 6, 4],
    [5, 6, 4, 2, 3, 1, 8, 9, 7],
    [4, 9, 7, 5, 6, 8, 2, 3, 1],
  ]
  GameGrid.printGrid(a)
  conflicts = GameGrid.zoneConflict(a, 2, 0)
  print(conflicts)
