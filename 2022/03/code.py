from string import ascii_lowercase, ascii_uppercase


# MAIN

# TASK 1
# What is the sum of the priorities of those item types?
#
# TASK 2
# What is the sum of the priorities of those item types?

def main():
    with open('2022/03/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING AND VARIABLES

    value = {i: ord(i) - 96 for i in ascii_lowercase} | {i: ord(i) - 38 for i in ascii_uppercase}

    # PART 1

    print(sum([value[set(i[:len(i) // 2]).intersection(i[len(i) // 2:]).pop()] for i in inp]))

    # RESULT: 7990

    # ----------------------------------------------------------------

    # PART 2

    print(sum([value[set(inp[i]).intersection(inp[i + 1]).intersection(inp[i + 2]).pop()] for i in range(0, len(inp) - 2, 3)]))

    # RESULT: 2602



if __name__ == '__main__':
    main()
