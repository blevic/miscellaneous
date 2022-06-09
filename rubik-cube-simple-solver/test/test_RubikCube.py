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

    def test_invalid_moves(self):
        invalid_moves = ["F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"]
        cube = RubikCube()

        for moves in invalid_moves:
            with self.assertRaises(ValueError):
                cube.move(moves)


if __name__ == '__main__':
    unittest.main()
