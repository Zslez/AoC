from ast import literal_eval
from itertools import permutations
from copy import deepcopy


# FUNCTIONS AND CLASSES

def check_explode(num, path, depth = 0):
    # if after depth 4 another list is nested then that should be split

    if depth == 4:
        return True

    # recursively check first and second elements of the pair
    # and return the first pair that should explode, if any

    first, second = num

    if type(first) is not int:
        path.append('0')

        if check_explode(first, path, depth + 1):
            return path

        path.pop()

    if type(second) is not int:
        path.append('1')

        if check_explode(second, path, depth + 1):
            return path

        path.pop()

    return None



def check_split(num, path):
    if type(num) is int:
        return True if num > 9 else False

    # recursively check first and second elements of the pair

    path.append(0)

    if check_split(num[0], path):
        return path

    path[-1] = 1

    if check_split(num[1], path):
        return path

    path.pop()

    return None



def get_prev_number(path):
    path = int(''.join(path), 2) - 1

    if path < 0:
        return None

    return [path // 8, path // 4 % 2, path // 2 % 2, path % 2]



def get_next_number(path):
    path = int(''.join(path), 2) + 1

    if path > 15:
        return None

    return [path // 8, path // 4 % 2, path // 2 % 2, path % 2]



def add_to_position(num, path, value, direction):
    # shitty way of checking that but it works, so it's fine

    path0, path1, path2, path3 = path
    num0 = num[path0]

    if type(num0) is int:
        num0 += value
    elif type(num0[path1]) is int:
        num0[path1] += value
    elif type(num0[path1][path2]) is int:
        num0[path1][path2] += value
    elif type(num0[path1][path2][path3]) is int:
        num0[path1][path2][path3] += value
    else:
        num0[path1][path2][path3][direction] += value

    return num



def split(num, path):
    match len(path):
        case 1:
            n = num[path[0]]
            num[path[0]] = [n // 2, n // 2 + n % 2]
        case 2:
            n = num[path[0]][path[1]]
            num[path[0]][path[1]] = [n // 2, n // 2 + n % 2]
        case 3:
            n = num[path[0]][path[1]][path[2]]
            num[path[0]][path[1]][path[2]] = [n // 2, n // 2 + n % 2]
        case 4:
            n = num[path[0]][path[1]][path[2]][path[3]]
            num[path[0]][path[1]][path[2]][path[3]] = [n // 2, n // 2 + n % 2]

    return num



def simplify(num):
    path = check_explode(num, [])
    spl = None

    while path is not None or spl is not None:
        # pair explosion

        if path is not None:
            prev, next = get_prev_number(path), get_next_number(path)
            path = [int(i) for i in path]

            values = num[path[0]][path[1]][path[2]][path[3]]

            if prev is not None:
                num = add_to_position(num, prev, values[0], 1)

            if next is not None:
                num = add_to_position(num, next, values[1], 0)

            num[path[0]][path[1]][path[2]][path[3]] = 0

        # split number

        if spl is not None:
            num = split(num, spl)

            # after split, an explosion should happen first, if any
            # before split is checked again

            path = check_explode(num, [])

            if path is not None:
                spl = None

                continue

        # check again

        path = check_explode(num, [])
        spl = check_split(num, [])

    return num



def magnitude(num):
    if isinstance(num, int):
        return num

    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])




# MAIN

# TASK 1
# calculate the magnitude of the sum of all of the snailfish numbers from the homework assignment in the order they appear
#
# TASK 2
# find the largest magnitude of any sum of two different snailfish numbers from the homework assignment

def main():
    with open('2021/18/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    '''inp = [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.split('\n')

    #numbers = [literal_eval(i) for i in inp]
    inp = [literal_eval(i) for i in inp]

    # PART 1

    numbers = deepcopy(inp)

    num = numbers[0]

    for i in numbers[1:]:
        num = simplify([num, i])

    print(magnitude(num))

    # RESULT: 3654

    # ----------------------------------------------------------------

    # PART 2

    from time import time

    s = time()

    poss = permutations(range(len(inp)), 2)

    results = []

    for i in poss:
        results.append(magnitude(simplify([deepcopy(inp[i[0]]), deepcopy(inp[i[1]])])))

    print(max(results))
    print(time() - s)

    # RESULT: 4578



if __name__ == '__main__':
    main()
