#!/usr/bin/env python

import random

def zoneConflict(grid, zone_x, zone_y):
  z_conflicts = []
  for cell_check_x in range(3):
    coor_check_x = zone_x*3 + cell_check_x
    for cell_check_y in range(3):
      coor_check_y = zone_y*3 + cell_check_y
      # print("{}={}".format(
      #   (coor_check_x, coor_check_y),
      #   grid[coor_check_x][coor_check_y],
      # ))
      for cell_other_x in range(3):
        coor_other_x = zone_x*3 + cell_other_x
        for cell_other_y in range(3):
          coor_other_y = zone_y*3 + cell_other_y
          if coor_check_x == coor_other_x and coor_check_y == coor_other_y:
            continue
          # print("\t{}={}".format(
          #   (coor_other_x, coor_other_y),
          #   grid[coor_other_x][coor_other_y],
          # ))
          if grid[coor_check_x][coor_check_y] == grid[coor_other_x][coor_other_y]:
            z_conflicts.append([(coor_check_x, coor_check_y), (coor_other_x, coor_other_y)])
  return z_conflicts 

def horizontalConflict(grid, row):
  h_conflicts = []
  for y_check in range(9):
    for y_rest in range(y_check+1, 9):
      if grid[row][y_check] == grid[row][y_rest]:
        h_conflicts.append([(row, y_check), (row, y_rest)])
  return h_conflicts

def verticalConflict(grid, col):
  v_conflicts = []
  for x_check in range(9):
    for x_rest in range(x_check+1, 9):
      if grid[x_check][col] == grid[x_rest][col]:
        v_conflicts.append([(x_check,col), (x_rest,col)])
  return v_conflicts

def validGrid(grid):
  conflicts_h = []
  conflicts_v = []
  for i in range(9):
    conflicts_h = horizontalConflict(grid, i)
    if conflicts_h:
      conflicts_h.append(conflicts_h[0])
      conflicts_h.append(conflicts_h[1])
    conflict_v = verticalConflict(grid, i)
    if conflict_v:
      conflicts_v.append(conflict_v[0])
      conflicts_v.append(conflict_v[1])

  conflicts_z = []
  for i in range(3):
    for j in range(3):
      conflict_z = zoneConflict(grid, i, j)
      if conflict_v:
        conflicts_z.append(conflict_z[0])
        conflicts_z.append(conflict_z[1])
  return conflicts_h, conflicts_v, conflicts_z

def randomGrid():
  return [[random.randint(1,9) for _ in range(9)] for _ in range(9)]

def baseGrid():
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

def printGrid(grid):
  for x, row in enumerate(grid):
    if x % 3 == 0:
      print(""," ".join(["-"*3 for _ in range(3)]))
    for y, cell in enumerate(row):
      if y % 3 == 0:
        print("|", end="")
      print(cell, end="")
    print("|")
