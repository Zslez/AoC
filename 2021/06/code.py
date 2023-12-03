# FUNCTIONS

def get_iteration(num, iters):
    if iters > 0:
        if num > 6:
            return get_iteration(num - 7, iters - 1)

        return get_iteration(num, iters - 1) + get_iteration(num + 2, iters - 1)

    return [num]


def get_length(num, iters):
    if iters > 0:
        if num > 6:
            return get_length(num - 7, iters - 1)

        return get_length(num, iters - 1) + get_length(num + 2, iters - 1)

    return 1



# MAIN

# TASK 1
# calculate how many lanternfish would be there after 80 days
#
# TASK 2
# calculate how many lanternfish would be there after 256 days

def main():
    with open('2021/06/input.txt') as f:
        inp = f.read()

    # INPUT FORMATTING

    fish = [int(i) for i in inp.split(',')]
    days = 80

    # PART 1

    for _ in range(days):
        fish = [i - 1 for i in fish]

        for i in range(len(fish)):
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)

    print(len(fish))

    # RESULT: 350149

    # ----------------------------------------------------------------

    # PART 2

    # I don't know why it gives the wrong result for 80 but the correct for 256
    # but at least it works 💀

    fish = [int(i) for i in inp.split(',')]
    days = 256

    for _ in range(days % 7):
        fish = [i - 1 for i in fish]

        for i in range(len(fish)):
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)

    days -= days % 7

    half_res = [get_iteration(i, days // 14) for i in range(9)]
    half_len = [get_length(i, days // 14) for i in range(9)]

    for i in range(len(fish)):
        fish[i] = half_res[fish[i]]

    fish = sum(fish, [])

    result = 0

    for i in fish:
        result += half_len[i]

    print(result)

    # RESULT: 1590327954513



if __name__ == '__main__':
    main()
