#!/usr/bin/env python

def baseGrid():
  '''
  Creates a valid sudoku grid. Used as the starting point.
  '''
  grid_cells = [[0 for _ in range(9)] for _ in range(9)]
  for block_x in range(3):
    for block_y in range(3):
      for cell_x in range(3):
        cell_x_ofset = (cell_x + block_y)%3
        coor_x = block_x*3 + cell_x_ofset
        for cell_y in range(3):
          cell_y_ofset = (cell_y + block_x)%3
          coor_y = block_y*3 + cell_y_ofset
          grid_cells[coor_x][coor_y] = (cell_x*3 + cell_y)+1
  return grid_cells
