# FUNCTIONS

def get_boards(board):
    res = [[]]

    for i in board.split('\n'):
        if i == '':
            res.append([])
        else:
            res[-1].append(i.split())
    
    return res


def board_sum(board, calls):
    '''returns the sum of the unmarked numbers in the board'''

    return sum([sum([int(j) for j in i if j not in calls]) for i in board])


def is_complete(board, calls):
    '''returns the sum of the unmarked numbers in the board if it won, 0 otherwise'''

    for i in range(len(board)):
        if all([j in calls for j in board[i]]): # if any row is complete
            return board_sum(board, calls)

        if all([j[i] in calls for j in board]): # if any column is complete
            return board_sum(board, calls)

    return False



# MAIN

# TASK 1
# find the board that wins first
#
# TASK 2
# find the board that wins last

def main():
    with open('2021/04/input.txt') as f:
        inp = f.read()

    # PART 1

    calls, boards_input = inp.split('\n\n', 1)
    called = []
    boards = get_boards(boards_input)

    for i in calls.split(','):
        called.append(i)

        for j in boards:
            # multiply the sum returned by is_complete() by the last called number

            result = is_complete(j, called) * int(i)

            if result:
                print(result)
                break
        else:
            continue

        break

    # RESULT: 49860

    # ----------------------------------------------------------------

    # PART 2

    called = []

    for i in calls.split(','):
        called.append(i)

        for j in boards:
            # multiply the sum returned by is_complete() by the last called number

            result = is_complete(j, called)

            if result is not False:
                if len(boards) == 1:
                    print(result * int(i))
                    break

                boards.remove(j)
        else:
            continue

        break

    # RESULT: 24628



if __name__ == '__main__':
    main()
