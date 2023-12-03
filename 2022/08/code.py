from math import prod
from itertools import product


# FUNCTIONS

def is_visible(x, y, grid):
    visible_dirs = 4

    for i in grid[x][:y]:
        if i >= grid[x][y]:
            visible_dirs -= 1
            break

    for i in grid[x][y + 1:]:
        if i >= grid[x][y]:
            visible_dirs -= 1
            break

    for i in grid[:x]:
        if i[y] >= grid[x][y]:
            visible_dirs -= 1
            break

    for i in grid[x + 1:]:
        if i[y] >= grid[x][y]:
            visible_dirs -= 1
            break

    return visible_dirs


def scenic_score(x, y, grid):
    scores = [0, 0, 0, 0]
    value = grid[x][y]

    # check upwards

    for i in range(x - 1, -1, -1):
        scores[0] += 1

        if grid[i][y] >= value:
            break

    # check rightwards

    for i in range(y + 1, len(grid[0])):
        scores[1] += 1

        if grid[x][i] >= value:
            break

    # check downwards

    for i in range(x + 1, len(grid)):
        scores[2] += 1

        if grid[i][y] >= value:
            break

    # check leftwards

    for i in range(y - 1, -1, -1):
        scores[3] += 1

        if grid[x][i] >= value:
            break

    return prod(scores)




# MAIN

# TASK 1
# How many trees are visible from outside the grid?
#
# TASK 2
# What is the highest scenic score possible for any tree?

def main():
    with open('2022/08/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    inp = [[int(j) for j in list(i)] for i in inp]
    sizey, sizex = len(inp), len(inp[0])

    # PART 1

    visible = 0

    for y in range(sizey):
        for x in range(sizex):
            if is_visible(x, y, inp):
                visible += 1

    print(visible)

    # RESULT: 1776

    # ----------------------------------------------------------------

    # PART 2

    print(max([scenic_score(i[0], i[1], inp) for i in product(range(1, sizex - 1), range(1, sizey - 1))]))

    # RESULT: 234416



if __name__ == '__main__':
    main()
