# FUNCTIONS


def lowest_risk_path(grid, size, pos, endvalue, remaining, result = 150, risk = 0):
    x, y = pos

    risk += grid[x][y]

    # 2 * size is the max length possible a path can be
    # so the risk will be at least 1 more for each step remaining
    # the remaining variable is therefore equal to 2 * size - len(path) - 1 + grid[size][size]
    # grid[size][size] is the value of the last cell, that is counted in the risk for sure

    if risk + remaining < result:
        # find not visited adiacents

        adiacents = []
        l = 0

        if x < size:
            adiacents += [(x + 1, y)]
            l = 1

        if y < size:
            adiacents += [(x, y + 1)]
            l += 1

        if l:
            if l == 2:
                adiacents.sort(key = lambda x: grid[x[0]][x[1]])

                for i in adiacents:
                    res = lowest_risk_path(grid, size, i, endvalue, remaining - 1, result, risk)
                    result = min(res, result)

            elif adiacents[0] == (size, size):
                result = min(risk + endvalue, result)

            else:
                res = lowest_risk_path(grid, size, adiacents[0], endvalue, remaining - 1, result, risk)
                result = min(res, result)

    return result




# MAIN

# TASK 1
# find the lowest total risk of any path from the top left to the bottom right
#
# TASK 2
# ...

def main():
    with open('2021/15/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    # ...

    # PART 1

    from time import time

    '''inp = 11637517427263918236
13813736727263918236
21365113287263918236
36949315697263918236
74634171117263918236
13191281377263918236
13599124217263918236
31254216397263918236
12931385217263918236
23119445817263918236
11637517427263918236
13813736727263918236
21365113287263918236
36949315697263918236
74634171117263918236
13191281377263918236
13599124217263918236
31254216397263918236
12931385217263918236
23119445817263918236.split()'''

    risks = []

    for size in range(20, 30):
        grid = tuple([tuple([int(j) for j in i[:size]]) for i in inp[:size]])

        print(size, end = ' ')

        size -= 1
        s = time()

        risk = lowest_risk_path(
            grid,
            size,
            (0, 0),
            grid[size][size],
            2 * size - 1 + grid[size][size]
        ) - grid[0][0]

        risks.append(risk)
        print(risk, end = ' ')
        print(time() - s)

    risks = [risks[i + 1] - risks[i] for i in range(len(risks) - 1)]
    print(sum(risks) / len(risks) * (100 - size - 2) + risk)

    # 20 80  0.7984521389007568
    # 21 85  3.446216583251953
    # 22 89  5.0729475021362305
    # 23 79  1.168994665145874
    # 24 82  1.1815526485443115
    # 25 92  1.6301448345184326
    # 26 97  17.606369733810425
    # 27 100 56.837716579437256

    # RESULT:

    # ----------------------------------------------------------------

    # PART 2

    inp = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''.split()

    # ...

    # RESULT:



if __name__ == '__main__':
    main()
