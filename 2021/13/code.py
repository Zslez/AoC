# MAIN

# TASK 1
# calculate how many dots are visible after completing just the first fold instruction on your transparent paper
#
# TASK 2
# find the code to use to activate the infrared thermal imaging camera system, following every remaining fold instruction

def main():
    with open('2021/13/input.txt') as f:
        inp = f.read()

    # INPUT FORMATTING

    dots, instructions = inp.split('\n\n')
    dots = [[int(j) for j in i.split(',')] for i in dots.split('\n')]
    instructions = [i.replace('fold along ', '').split('=') for i in instructions.split('\n')]

    # PART 1

    first_fold = instructions[0]

    for i in range(len(dots)):
        x_or_y = first_fold[0] == 'y'

        if dots[i][x_or_y] > int(first_fold[1]):
            dots[i][x_or_y] = 2 * int(first_fold[1]) - dots[i][x_or_y]

    dots = [tuple(i) for i in dots]

    print(len(list(set(dots))))

    # RESULT: 638

    # ----------------------------------------------------------------

    # PART 2

    dots, instructions = inp.split('\n\n')
    dots = [[int(j) for j in i.split(',')] for i in dots.split('\n')]
    instructions = [i.replace('fold along ', '').split('=') for i in instructions.split('\n')]

    for instr in instructions:
        for i in range(len(dots)):
            x_or_y = instr[0] == 'y'

            if dots[i][x_or_y] > int(instr[1]):
                dots[i][x_or_y] = 2 * int(instr[1]) - dots[i][x_or_y]

        dots = [list(i) for i in set([tuple(i) for i in dots])]

    lx, ly = max([i[0] for i in dots]), max([i[1] for i in dots])

    for i in range(ly + 1):
        for j in range(lx + 1):
            if [j, i] in dots:
                print('#', end = '')
            else:
                print(' ', end = '')
        print()

    # RESULT: CJCKBAPB



if __name__ == '__main__':
    main()
