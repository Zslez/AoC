from numpy import array


# MAIN

# TASK 1
# Find the sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
#
# TASK 2
# Render the image given by your program. What eight capital letters appear on your CRT?

def main():
    with open('2022/10/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    inp = [i.split() for i in inp]

    interesting = [20, 60, 100, 140, 180, 220]

    # PART 1

    cycle = 0
    x = 1

    results = []

    for i in inp:
        if len(i) == 1:
            cycle += 1

            if cycle in interesting:
                results.append(x)
        else:
            for _ in range(2):
                cycle += 1

                if cycle in interesting:
                    results.append(x)

            x += int(i[1])

    print(sum(results * array(interesting)))

    # RESULT: 16880

    # ----------------------------------------------------------------

    # PART 2

    cycle = 0
    x = 1

    results = [[]]

    for i in inp:
        if len(i) == 1:
            if cycle in range(x - 1, x + 2):
                results[-1].append('#')
            else:
                results[-1].append(' ')

            cycle += 1

            if cycle == 40:
                results.append([])
                cycle = 0
        else:
            for _ in range(2):
                if cycle in range(x - 1, x + 2):
                    results[-1].append('#')
                else:
                    results[-1].append(' ')

                cycle += 1

                if cycle == 40:
                    results.append([])
                    cycle = 0

            x += int(i[1])

    print('\n'.join([''.join(i) for i in results]))

    # RESULT: RKAZAJBR



if __name__ == '__main__':
    main()
