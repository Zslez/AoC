# FUNCTIONS

def get_points(line):
    if line[0][0] == line[1][0]:
        direction = [-1, 1][line[0][1] < line[1][1]]

        return [[line[0][0], i] for i in range(line[0][1], line[1][1] + direction, direction)]
    elif line[0][1] == line[1][1]:
        direction = [-1, 1][line[0][0] < line[1][0]]

        return [[i, line[0][1]] for i in range(line[0][0], line[1][0] + direction, direction)]
    else:
        xdir = [-1, 1][line[0][0] < line[1][0]]
        ydir = [-1, 1][line[0][1] < line[1][1]]

        length = abs(line[0][0] - line[1][0])

        return [[line[0][0] + i * xdir, line[0][1] + i * ydir] for i in range(0, length + 1)]


def print_table(table, mx, my):
    for i in range(my):
        print(table[i * mx: (i + 1) * mx])




# MAIN

# TASK 1
# considering only horizontal and vertical lines, count at how many points at least two lines overlap
#
# TASK 2
# considering also 45° diagonal lines, count at how many points at least two lines overlap

def main():
    with open('2021/05/input.txt') as f:
        inp = f.readlines()

    # INPUT FORMATTING

    lines = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in inp]

    # PART 1

    straight = [i for i in lines if i[0][0] == i[1][0] or i[0][1] == i[1][1]]
    max_x = max(sum(sum(straight, []), [])[::2]) + 1
    max_y = max(sum(sum(straight, []), [])[1::2]) + 1

    table = [0] * (max_x * max_y)

    for line in straight:
        for point in get_points(line):
            table[point[0] + max_x * point[1]] += 1

    result = len([i for i in table if i > 1])

    print(result)

    # RESULT: 4421

    # ----------------------------------------------------------------

    # PART 2

    possible = [i for i in lines if i[0][0] == i[1][0] or i[0][1] == i[1][1] or abs(i[0][0] - i[1][0]) == abs(i[0][1] - i[1][1])]
    max_x = max(sum(sum(possible, []), [])[::2]) + 1
    max_y = max(sum(sum(possible, []), [])[1::2]) + 1

    table = [0] * (max_x * max_y)

    for line in possible:
        for point in get_points(line):
            table[point[0] + max_x * point[1]] += 1

    result = len([i for i in table if i > 1])

    print(result)

    # RESULT: 18674



if __name__ == '__main__':
    main()
