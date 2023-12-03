# MAIN

# TASK 1
# calculate the total score if everything goes exactly according to your strategy guide
#
# TASK 2
# calculate the total score following the new rule the elf said

def main():
    with open('2022/02/input.txt') as f:
        inp = f.read().split('\n')

    # PART 1

    replace = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

    # draw difference: 0
    # win  difference: 1, -2 (-2 % 3 == 1)
    # loss difference: 2, -1 (-1 % 3 == 2)

    score = {0: 3, 1: 6, 2: 0}

    print(sum([score[(replace[i[-1]] - replace[i[0]]) % 3] + replace[i[-1]] for i in inp]))

    # RESULT: 12794

    # ----------------------------------------------------------------

    # PART 2

    new = {'X': 0, 'Y': 3, 'Z': 6}
    inverse = {0: 2, 3: 0, 6: 1}
    correct = {0: 3, 1: 1, 2: 2}

    # from the first part we have

    # score[(player_choice - replace[i[0]]) % 3] == new[i[-1]] (result score)
    # player_choice - replace[i[0]] == inverse[new[i[-1]]]
    # player_choice == inverse[new[i[-1]]] + replace[i[0]]
    # but with 3 replaced by 0

    # => correct[player_choice] == actual player choice

    print(sum([correct[(inverse[new[i[-1]]] + replace[i[0]]) % 3] + new[i[-1]] for i in inp]))

    # RESULT: 14979



if __name__ == '__main__':
    main()
