from itertools import product


# FUNCTIONS

def get_adiacents(pos, size):
    rangex = range(max(pos[0] - 1, 0), min(pos[0] + 2, size))
    rangey = range(max(pos[1] - 1, 0), min(pos[1] + 2, size))

    adiacents = list(product(rangex, rangey))
    adiacents.remove(pos)

    return adiacents


def flash(grid, x, y):
    flashes = 0

    if grid[x][y] > 9:
        grid[x][y] = 0
        flashes += 1

        for i in get_adiacents((x, y), len(grid)):
            if grid[i[0]][i[1]] != 0:
                grid[i[0]][i[1]] += 1

            if grid[i[0]][i[1]] > 9:
                flashes += flash(grid, i[0], i[1])

    return flashes




# MAIN

# TASK 1
# calculate the number of flashes happened in 100 steps
#
# TASK 2
# find the first step during which all octopuses flash

def main():
    with open('2021/11/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    grid = [[int(j) for j in i] for i in inp]

    # PART 1

    steps = 100
    flashes = 0

    for _ in range(steps):
        grid = [[j + 1 for j in i] for i in grid]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                flashes += flash(grid, x, y)

    print(flashes)

    # RESULT: 1721

    # ----------------------------------------------------------------

    # PART 2

    # NOTE: steps is already 100 and the grid already changed 100 times

    while True:
        steps += 1

        grid = [[j + 1 for j in i] for i in grid]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                flash(grid, x, y)

        if all([i == 0 for i in sum(grid, [])]):
            break

    print(steps)

    # RESULT: 298



if __name__ == '__main__':
    main()
