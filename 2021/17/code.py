from itertools import product


# FUNCTIONS

def steps(num, v):
    x, y = 0, 0

    for i in range(num):
        x += max(v[0] - i, 0)
        y += v[1] - i

    return (x, y)


def ymax(y0):
    return y0 * (y0 + 1) // 2


def y_in_target_after(y0, target_y):
    y = 0
    steps = 2 * y0 + 1 if y0 > 0 else 0
    result = []

    while 1:
        y += y0 - steps
        steps += 1

        if y in target_y:
            result.append(steps)
        elif y < target_y[-1] + 1:
            return result




# MAIN

# TASK 1
# find the initial velocity for the probe to reach the highest y position and still be within the target area after any step
#
# TASK 2
# find how many distinct initial velocity values cause the probe to be within the target area after any step

def main():
    with open('2021/17/input.txt') as f:
        inp = f.read().replace('target area: ', '')

    # INPUT FORMATTING

    area = inp.split(', ')

    ax = [int(i) for i in area[0].replace('x=', '').split('..')]
    ay = [int(i) for i in area[1].replace('y=', '').split('..')]

    target = (range(ax[0], ax[1] + 1), range(ay[0], ay[1] + 1))

    area = list(product(target[0], target[1]))

    # PART 1

    # NOTE:

    # with the given instructions is trivial to notice that
    # the probe will be at y = 0 after 2 * y0 + 1 steps

    # so to check if the probe will eventually be within the target area
    # it's enough to check the first few steps after 2 * y0 + 1

    # in addition to this,
    # the max y0 value that could be within the target area after any steps will be -target_y[0]
    # because with y0 greater than that,
    # the y after 2 * y0 steps will be always below the target area

    # follows that looping starting from the max_y downwards,
    # the first x that happens to be within the target area too
    # forms with the y the velocity with the max possible y reached

    max_x = target[0][-1] + 1
    max_y = -target[1][0]

    range_x = range(max_x)
    range_y = range(max_y - 1, -max_y - 1, -1)

    for y in range_y:
        for s in y_in_target_after(y,target[1]):
            for x in range_x:
                if steps(s, (x, y)) in area:
                    print(ymax(y))
                    break
            else:
                continue

            break
        else:
            continue

        break

    # RESULT: 5778

    # ----------------------------------------------------------------

    # PART 2

    result = 0
    res = []

    for y in range_y:
        for s in y_in_target_after(y, target[1]):
            for x in range_x:
                if steps(s, (x, y)) in area:
                    if (x, y) not in res:
                        res.append((x, y))
                        result += 1


    print(result)

    # RESULT: 2576



if __name__ == '__main__':
    main()
