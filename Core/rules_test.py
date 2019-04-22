import unittest

import Core.rules as rules

class TestSudokuRules(unittest.TestCase):
  game_board = [
    [0,1,0, 0,1,0, 0,1,0],
    [0,1,0, 0,0,0, 0,0,0],
    [0,0,1, 0,0,0, 0,0,0],

    [0,0,1, 1,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [1,0,0, 0,0,0, 0,0,1],

    [0,0,0, 1,0,0, 1,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 1,0,0, 0,0,1],
  ]

  def test_allZeros(self):
  # all zeros
    game_board = [[0 for _ in range(9)] for _ in range(9)]

    vertical_conflict = rules.verticalConflicts(game_board, (0, 0))
    self.assertEqual(vertical_conflict, [])

    horizontal_conflict = rules.horizontalConflicts(game_board, (0, 0))
    self.assertEqual(horizontal_conflict, [])

    zone_conflict = rules.zoneConflicts(game_board, (0, 0))
    self.assertEqual(zone_conflict, [])

  def test_horizontalConflict(self):
    horizontal_conflict = rules.horizontalConflicts(self.game_board, (0, 1))
    self.assertEqual(horizontal_conflict,
      [
        ((0,1),(0, 4)),
        ((0,1),(0, 7)),
      ]
    )
    horizontal_conflict = rules.horizontalConflicts(self.game_board, (0, 4))
    self.assertEqual(horizontal_conflict,
      [
        ((0, 1), (0, 4)),
        ((0, 4), (0, 7)),
      ]
    )
    horizontal_conflict = rules.horizontalConflicts(self.game_board, (1, 1))
    self.assertEqual(horizontal_conflict, [])
    horizontal_conflict = rules.horizontalConflicts(self.game_board, (3, 3))
    self.assertEqual(horizontal_conflict, [((3, 2), (3, 3))])
    horizontal_conflict = rules.horizontalConflicts(self.game_board, (5, 0))
    self.assertEqual(horizontal_conflict, [((5, 0), (5, 8))])

  def test_verticalConflict(self):
    vertical_conflict = rules.verticalConflicts(self.game_board, (0, 1))
    self.assertEqual(vertical_conflict, [((0, 1), (1, 1))])
    vertical_conflict = rules.verticalConflicts(self.game_board, (0, 4))
    self.assertEqual(vertical_conflict, [])
    vertical_conflict = rules.verticalConflicts(self.game_board, (1, 1))
    self.assertEqual(vertical_conflict, [((0, 1), (1, 1))])
    vertical_conflict = rules.verticalConflicts(self.game_board, (3, 3))
    self.assertEqual(vertical_conflict,
      [
        ((3, 3), (6, 3)),
        ((3, 3), (8, 3)),
      ]
    )
    vertical_conflict = rules.verticalConflicts(self.game_board, (5, 0))
    self.assertEqual(vertical_conflict, [])

  def test_zoneConflict(self):
    zone_conflict = rules.zoneConflicts(self.game_board, (0, 1))
    self.assertEqual(zone_conflict,
      [
        ((0, 1), (1, 1)),
        ((0, 1), (2, 2)),
      ]
    )

if __name__ == "__main__":
  unittest.main()