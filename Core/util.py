
def printGrid(grid):
  for x, row in enumerate(grid):
    if x % 3 == 0:
      print(""," ".join(["-"*3 for _ in range(3)]))
    for y, cell in enumerate(row):
      if y % 3 == 0:
        print("|", end="")
      print(cell, end="")
    print("|")
