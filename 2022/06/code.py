# MAIN

# TASK 1
# How many characters need to be processed before the first start-of-packet marker is detected?
#
# TASK 2
# How many characters need to be processed before the first start-of-message marker is detected?

def main():
    with open('2022/06/input.txt') as f:
        inp = f.read()

    # PART 1

    count = 4

    while len(set(inp[count - 4: count])) < 4:
        count += 1

    print(count)

    # RESULT: 1855

    # ----------------------------------------------------------------

    # PART 2

    count = 14

    while len(set(inp[count - 14: count])) < 14:
        count += 1

    print(count)

    # RESULT:



if __name__ == '__main__':
    main()
