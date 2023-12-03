# MAIN

# TASK 1
# What is the sum of all of the calibration values?
#
# TASK 2
# What is the sum of all of the calibration values? (with also digits spelled as words)



def main():
    with open('2023/01/input.txt') as f:
        inp = f.read().split()

    numberdigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letterdigits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # PART 1

    numbers = []

    for i in inp:
        numbers.append([])

        for j in i:
            if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                numbers[-1].append(j)

    print(sum([int(i[0] + i[-1]) for i in numbers]))

    # RESULT: 54927

    # ----------------------------------------------------------------

    # PART 2

    for i in range(len(inp)):
        for j in range(len(letterdigits)):
            inp[i] = inp[i].replace(letterdigits[j], letterdigits[j] + numberdigits[j] + letterdigits[j])

    numbers = []

    for i in inp:
        numbers.append([])

        for j in i:
            if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                numbers[-1].append(j)

    print(sum([int(i[0] + i[-1]) for i in numbers]))

    # RESULT: 54581



if __name__ == '__main__':
    main()
