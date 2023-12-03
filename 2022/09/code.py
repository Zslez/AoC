from math import dist
from numpy import array
from itertools import product


# FUNCTIONS

def print_map(rope, visited):
    map = {i: '.' for i in product(range(-16, 6), range(-11, 15))}
    map[(0, 0)] = 's'

    for i in range(len(rope) - 1, -1, -1):
        coords = (-rope[i][1], rope[i][0])
        map[coords] = i

    for i in visited[:-1]:
        coords = (-i[1], i[0])
        map[coords] = '#'

    c = 0
    print(rope)

    for i in map:
        print(map[i], end = ' ')
        c += 1

        if c == 26:
            print()
            c = 0

    input()




# MAIN

# TASK 1
# How many positions does the tail of the rope visit at least once?
#
# TASK 2
# Simulate the series of motions on a rope with ten knots. How many positions does the tail of the rope visit at least once?

def main():
    with open('2022/09/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING AND VARIABLES

    dirs = {'R': [1, 0], 'U': [0, 1], 'L': [-1, 0], 'D': [0, -1]}

    # PART 1

    visited = []
    head, tail = array([0, 0]), array([0, 0])

    for i in inp:
        dir, steps = i.split()
        dir = array(dirs[dir])
        is_horizontal = int(dir[0] != 0)

        for _ in range(int(steps)):
            head += dir

            distance = dist(head, tail)

            if distance == 2:
                tail += dir
            elif distance > 1.5:
                tail += dir
                tail[is_horizontal] = head[is_horizontal]

            if tuple(tail) not in visited:
                visited.append(tuple(tail))

    print(len(visited))

    # RESULT: 6271

    # ----------------------------------------------------------------

    # PART 2

    visited = []
    rope = [array([0, 0]) for _ in range(10)]

    for i in inp:
        dir, steps = i.split()
        dir = array(dirs[dir])
        is_horizontal = int(dir[0] != 0)

        for _ in range(int(steps)):
            old_rope = [i.copy() for i in rope]
            rope[0] += dir

            chain = False
            for j in range(1, 10):
                distance = dist(rope[j], rope[j - 1])

                if distance == 2:
                    rope[j] = (rope[j] + rope[j - 1]) / 2

                    # break the chain

                    chain = False
                elif distance > 1.5:
                    if not chain:
                        # make the know move diagonally towards the previous one and start a chain

                        r0, r1 = rope[j]
                        rp0, rp1 = rope[j - 1]

                        if rp0 - r0 in (2, -2):
                            rope[j][0] += (rp0 - r0) / 2
                            rope[j][1] = rp1
                        else:
                            rope[j][1] += (rp1 - r1) / 2
                            rope[j][0] = rp0

                        chain = True
                    else:
                        # CHAIN
                        # if the previous knot did a diagonal move the next will necessarily make the same exact move
                        # unless the distance is again 2

                        rope[j] += (rope[j - 1] - old_rope[j - 1]).astype(int)

                if tuple(rope[-1]) not in visited:
                    visited.append(tuple(rope[-1]))

    print(len(visited))

    # RESULT: 2458



if __name__ == '__main__':
    main()
