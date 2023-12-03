from math import prod


# FUNCTIONS

def is_low_point(obj, pos):
    x, y = pos

    lx = len(obj)
    ly = len(obj[0])

    if x > 0 and obj[x][y] >= obj[x - 1][y]:
        return False

    elif y > 0 and obj[x][y] >= obj[x][y - 1]:
        return False

    elif x < lx - 1 and obj[x][y] >= obj[x + 1][y]:
        return False

    elif y < ly - 1 and obj[x][y] >= obj[x][y + 1]:
        return False

    return True


def get_basin(obj, pos, already_in = list()):
    basin = [pos]

    x, y = pos

    if obj[x][y] == 9:
        return None

    lx = len(obj)
    ly = len(obj[0])

    already_in.append(pos)

    if x > 0 and not (x - 1, y) in already_in and obj[x - 1][y] != 9:
        basin.extend(get_basin(obj, (x - 1, y), already_in))

    if y > 0 and not (x, y - 1) in already_in and obj[x][y - 1] != 9:
        basin.extend(get_basin(obj, (x, y - 1), already_in))

    if x < lx - 1 and not (x + 1, y) in already_in and obj[x + 1][y] != 9:
        basin.extend(get_basin(obj, (x + 1, y), already_in))

    if y < ly - 1 and not (x, y + 1) in already_in and obj[x][y + 1] != 9:
        basin.extend(get_basin(obj, (x, y + 1), already_in))

    return basin




# MAIN

# TASK 1
# calculate the sum of the risk levels of all low points on the heightmap
#
# TASK 2
# calculate the product of the sizes of the three largest basins on the heightmap

def main():
    with open('2021/09/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    obj = list(map(list, zip(*[[int(j) for j in list(i)] for i in inp])))

    # PART 1

    low_points = []

    for y in range(len(obj)):
        for x in range(len(obj[0])):
            if is_low_point(obj, (x, y)):
                low_points.append(obj[x][y] + 1)

    print(sum(low_points))

    # RESULT: 566

    # ----------------------------------------------------------------

    # PART 2

    basins = []
    positions = []

    for x in range(len(obj)):
        for y in range(len(obj[0])):
            if (x, y) not in positions:
                basin = get_basin(obj, (x, y))

                if basin is not None:
                    basins.append(len(basin))
                    positions.extend(basin)

    print(prod(sorted(basins, reverse = True)[:3]))

    # RESULT: 891684



if __name__ == '__main__':
    main()
