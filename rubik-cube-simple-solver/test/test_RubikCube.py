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

    def test_is_solved(self):
        cube = RubikCube()
        self.assertTrue(cube.is_solved())

        cube.move("xyzxpypzpx2xy2z2")
        self.assertTrue(cube.is_solved())

        for i in range(6):
            cube.move("RURpUp")
            if i == 5:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        for i in range(1260):
            cube.move("DRpU2M")
            if i == 1259:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        cube.move("FFpBBpUUpDDpLLpRRpffpbbpuupddpllprrpxxpyypzzpMMpEEpSSp")
        self.assertTrue(cube.is_solved())


if __name__ == '__main__':
    unittest.main()
