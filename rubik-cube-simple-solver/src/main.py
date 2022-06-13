from RubikCube import RubikCube

if __name__ == '__main__':
    rubik = RubikCube()
    print(rubik.scramble(steps=50, cube_rotations=True))
    rubik.draw()

    print("SOLVING...")

    print(rubik.solve())
    rubik.draw()
