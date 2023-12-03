# MAIN

# TASK 1
# find the the value of the elf carrying the most
#
# TASK 2
# calculate the sum of the three elves carrying the most

def main():
    with open('2022/01/input.txt') as f:
        inp = f.read().split('\n\n')

    # PART 1

    print(max([sum([int(j) for j in i.split('\n')]) for i in inp]))

    # RESULT: 69795

    # ----------------------------------------------------------------

    # PART 2

    print(sum(sorted([sum([int(j) for j in i.split('\n')]) for i in inp])[-3:]))

    # RESULT: 208437



if __name__ == '__main__':
    main()
