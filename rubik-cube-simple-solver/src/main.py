from RubikCube import RubikCube

if __name__ == '__main__':
    cube = RubikCube()
    initial_scramble = cube.scramble()
    print("Initial scramble:", initial_scramble)
    cube.draw()
    lbl_solution_moves = cube.solve()
    print("Layer by layer solution:", lbl_solution_moves)
