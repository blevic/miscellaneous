import unittest
from RubikCube import RubikCube


class TestRubikCube(unittest.TestCase):
    def test_valid_moves(self):
        valid_moves = ["F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"]
        cube = RubikCube()

        for moves in valid_moves:
            try:
                cube.move(moves)
            except ValueError:
                self.fail("move() raised ValueError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
