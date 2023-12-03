# FUNCTIONS

def get_adjacent(width, height, pos_of_number):
    # pos is in the form: [positin of first digit, number, number of digits]

    result = []

    for i in (-1, 0, 1):
        pos = pos_of_number[0] - i * width

        for j in range(-1, pos_of_number[2] + 1):
            newpos = pos + j

            # remove out of bounds

            if (newpos % width == 0 and j == pos_of_number[2] + 1) or (newpos % width == width - 1 and j == -1):
                continue

            if newpos < 0 or newpos >= width * height:
                continue

            result.append(pos + j)

    return result




# MAIN

# TASK 1
# What is the sum of all of the part numbers in the engine schematic?
#
# TASK 2
# What is the sum of all of the gear ratios in your engine schematic?



def main():
    with open('2023/03/input.txt') as f:
        inp = f.read()


    # INPUT FORMATTING
    
    numbers = '0123456789'

    pos_of_numbers = []
    pos, num = 0, ''

    for i in inp.replace('\n', ''):
        if i in numbers:
            num += i
        elif num:
            pos_of_numbers.append([pos - len(num), int(num), len(num)])
            num = ''

        pos += 1

    width, height = len(inp.split('\n')[0]), len(inp.split('\n'))
    inp = list(inp.replace('\n', ''))


    # PART 1

    total = 0

    for i in pos_of_numbers:
        for cell in get_adjacent(width, height, i):
            if inp[cell] not in numbers + '.':
                total += i[1]

    print(total)

    # RESULT: 521601

    # ----------------------------------------------------------------


    # PART 2

    gears = {i: [0, 1] for i in range(width * height)}

    for i in pos_of_numbers:
        for cell in get_adjacent(width, height, i):
            if inp[cell] == '*':
                gears[cell][0] += 1
                gears[cell][1] *= i[1]

    total = 0

    for i in gears:
        if gears[i][0] == 2:
            total += gears[i][1]

    print(total)

    # RESULT: 80694070



if __name__ == '__main__':
    main()
