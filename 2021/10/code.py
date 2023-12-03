# FUNCTIONS

def corruption(line):
    opened = []

    symbs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for i in line:
        if i in symbs:
            opened.append(symbs[i])
        else:
            if i != opened[-1]:
                return i

            opened.pop()

    return None


def get_missing_score(line):
    opened = []

    symbs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for i in line:
        if i in symbs:
            opened.append(i)
        else:
            opened.pop()

    score = 0

    missing = [symbs[i] for i in opened[::-1]]

    for i in missing:
        score *= 5
        score += ')]}>'.index(i) + 1

    return score




# MAIN

# TASK 1
# calculate the sum of the syntax error scores of the first illegal character in each corrupted line
#
# TASK 2
# calculate the score of each completion string of incomplete lines, and sort the scores and return the middle score

def main():
    with open('2021/10/input.txt') as f:
        inp = f.read().split('\n')

    # VARIABLES

    points = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}

    # PART 1

    print(sum([points[corruption(i)] for i in inp]))

    # RESULT: 344193

    # ----------------------------------------------------------------

    # PART 2

    scores = [get_missing_score(i) for i in inp if corruption(i) is None]

    print(sorted(scores)[len(scores) // 2])

    # RESULT: 3241238967



if __name__ == '__main__':
    main()
