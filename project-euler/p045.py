# Find the third triangle number that is also pentagonal and hexagonal.

idx = [1, 1, 1]
count = 0
while True:
    triangle = idx[0] * (idx[0] + 1) // 2
    pentagon = idx[1] * (3 * idx[1] - 1) // 2
    hexagon = idx[2] * (2 * idx[2] - 1)

    values = [triangle, pentagon, hexagon]

    if triangle == pentagon == hexagon:
        count += 1
        if count == 3:
            break

    increment_idx = values.index(min(values))

    idx[increment_idx] += 1

print(triangle)
