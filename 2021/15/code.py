import heapq


# FUNCTIONS


def lowest_risk_path(grid):
    visited = set()
    results = dict()

    steps = [(0, 0, 0)]
    heapq.heapify(steps)

    size = len(grid)

    while len(steps) > 0:
        risk, row, col = heapq.heappop(steps)

        if (row, col) in visited:
            continue

        visited.add((row, col))
        results[(row, col)] = risk

        if row == size - 1 and col == size - 1:
            break

        for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            temp_row = row + i[0]
            temp_col = col + i[1]

            if not (0 <= temp_row < size and 0 <= temp_col < size):
                continue

            heapq.heappush(steps, (risk + grid[temp_row][temp_col], temp_row, temp_col))

    return results[(size - 1, size - 1)]




# MAIN

# TASK 1
# find the lowest total risk of any path from the top left to the bottom right
#
# TASK 2
# ...

def main():
    with open('2021/15/input.txt') as f:
        inp = f.read().split('\n')

    # PART 1

    grid = [[int(j) for j in i] for i in inp]

    print(lowest_risk_path(grid))

    # RESULT: 386

    # ----------------------------------------------------------------

    # PART 2

    size = len(grid)

    for i in range(size * 4):
        grid.append([])

    for i in range(size):
        for j in range(8):
            grid[i].extend([(k % 9) + 1 for k in grid[i][-size:]])

            for k in range(min(j + 1, 4)):
                grid[i + size * (k + 1)].extend(grid[i][-size:])

    grid = [i[:size * 5] for i in grid]

    print(lowest_risk_path(grid))

    # RESULT: 2806



if __name__ == '__main__':
    main()
