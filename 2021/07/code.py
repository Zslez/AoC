# TASK 1
# calculate how much fuel crabs must spend to align to the position that costs the least fuel possible
# knowing that each step costs 1
#
# TASK 2
# calculate how much fuel crabs must spend to align to the position that costs the least fuel possible
# knowing that the first step costs 1 and each further step costs 1 more than the previous

def main():
    with open('2021/07/input.txt') as f:
        inp = f.read()

    # INPUT FORMATTING

    pos = [int(i) for i in inp.split(',')]

    # PART 1

    fuel = min([sum([abs(j - i) for j in pos]) for i in range(min(pos), max(pos))])

    print(fuel)

    # RESULT: 347011

    # ----------------------------------------------------------------

    # PART 2

    # NOTE: sum from 1 to n = n * (n + 1) / 2

    fuel = min([sum([int(abs(j - i) * (abs(j - i) + 1) * 0.5) for j in pos]) for i in range(min(pos), max(pos))])

    print(fuel)

    # RESULT: 98363777



if __name__ == '__main__':
    main()
