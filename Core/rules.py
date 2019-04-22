#!/usr/bin/env python

import random

def horizontalConflicts(game_board, coor):
  '''
  Returns a list of ordered unique coordinate pairs that conflict with each other horizontally with 'coor'
  '''
  if game_board[coor[0]][coor[1]] == 0:
    return []

  conflicts = set()
  for i in range(9):
    if i == coor[1]:
      continue
    if game_board[coor[0]][coor[1]] == game_board[coor[0]][i]:
      conflict = [coor, (coor[0], i)]
      conflict.sort()
      conflicts.add(tuple(conflict))
  conflicts = list(conflicts)
  conflicts.sort()
  return conflicts

def verticalConflicts(game_board, coor):
  '''
  Returns a list of ordered unique coordinate pairs that conflict with each other vertically with 'coor'
  '''
  if game_board[coor[0]][coor[1]] == 0:
    return []

  conflicts = set()
  for i in range(9):
    if i == coor[0]:
      continue
    if game_board[coor[0]][coor[1]] == game_board[i][coor[1]]:
      conflict = [coor, (i, coor[1])]
      conflict.sort()
      conflicts.add(tuple(conflict))
  conflicts = list(conflicts)
  conflicts.sort()
  return conflicts

def zoneConflicts(game_board, coor):
  '''
  Returns a list of ordered unique coordinate pairs that conflict with each other zonally with 'coor'
  '''
  if game_board[coor[0]][coor[1]] == 0:
    return []
  conflicts = set()
  zone_base = ((coor[0]//3)*3, (coor[1]//3)*3)
  for i in range(zone_base[0], zone_base[0]+3):
    for j in range(zone_base[1], zone_base[1]+3):
      if i == coor[0] and j == coor[1]:
        continue
      if game_board[coor[0]][coor[1]] == game_board[i][j]:
        conflict = [coor, (i, j)]
        conflict.sort()
        conflicts.add(tuple(conflict))
  conflicts = list(conflicts)
  conflicts.sort()
  return conflicts

def conflicts(game_board, coor):
  '''
  Aggregate all conflicts caused by 'coor'
  '''
  pass

def totalConflicts(game_board):
  '''
  Aggregates all the conflicts in game_board.
  '''
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
