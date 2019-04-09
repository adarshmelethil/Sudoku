#!/usr/bin/env python

from tkinter import Frame, Label, CENTER
import logging

import UI.constants as c
import UI.logic as l

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def defaultKeyDown(grid_values, event):
  logger.debug("Pressed the key {}".format(event.char))
def defaultMouseClick(grid_values, event):
  logger.debug("Clicked a {}".format(type(event.widget)))

class GameGrid(Frame):
  def __init__(self, initFunc=None, keyDownFunc=defaultKeyDown, mouseClickFunc=defaultMouseClick):
    Frame.__init__(self)
    self.grid()

    self.master.title("Sudoku")
    self.master.bind("<Key>", self.keyDown)
    self.keypress_callback = keyDownFunc
    self.master.bind('<Button-1>', self.mouseClick)
    self.mouseclick_callback = mouseClickFunc

    # Numbers
    self.grid_values = l.baseGrid()
    if initFunc is not None:
      initFunc(self.grid_values)
    # Labels
    self.grid_cells = []

    self.history = []

    self.updateGrid()

  def initGrid(self):
    background = Frame(
      self, 
      bg=c.BACKGROUND_COLOR_GAME,
      width=c.WIDTH,
      height=c.HEIGHT,
    )
    background.grid()

    game_background = Frame(
      backgroud,
      bg=c.BACKGROUND_COLOR_GAME,
      width=c.WIDTH/2,
      height=c.HEIGHT,
    )

    zones = []
    for i in range(3):
      h_zones = []
      for j in range(3):
        zone = Frame(
          game_background,
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

  def mouseClick(self, event):
    if self.mouseclick_callback:
      self.mouseclick_callback(self.grid_values, event)
    self.updateGrid()

  def keyDown(self, event):
    if self.keypress_callback:
      self.keypress_callback(self.grid_values, event)
    self.updateGrid()

if __name__ == "__main__":
  g = GameGrid()
  g.mainloop()
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
  # a = [
  #   [1, 2, 3, 7, 8, 9, 4, 5, 6],
  #   [8, 5, 6, 1, 2, 3, 7, 4, 9],
  #   [7, 8, 9, 4, 5, 6, 1, 2, 3],
  #   [3, 1, 2, 9, 7, 4, 6, 8, 5],
  #   [6, 4, 5, 3, 1, 2, 9, 7, 8],
  #   [9, 7, 8, 6, 4, 5, 3, 1, 2],
  #   [2, 3, 1, 8, 9, 7, 5, 6, 4],
  #   [5, 6, 4, 2, 3, 1, 8, 9, 7],
  #   [4, 9, 7, 5, 6, 8, 2, 3, 1],
  # ]
  # GameGrid.printGrid(a)
  # conflicts = GameGrid.zoneConflict(a, 2, 0)
  # print(conflicts)
