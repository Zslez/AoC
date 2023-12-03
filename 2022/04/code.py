# MAIN

# TASK 1
# In how many assignment pairs does one range fully contain the other?
#
# TASK 2
# In how many assignment pairs do the ranges overlap?

def main():
    with open('2022/04/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    inp = [[set(range(int(j.split('-')[0]), int(j.split('-')[1]) + 1)) for j in i.split(',')] for i in inp]

    # PART 1

    print(sum([1 if i[0].union(i[1]) in i else 0 for i in inp]))

    # RESULT: 538

    # ----------------------------------------------------------------

    # PART 2

    print(sum([1 if len(i[0].intersection(i[1])) else 0 for i in inp]))

    # RESULT: 792



if __name__ == '__main__':
    main()
