with open('2021/02/input.txt') as f:
    # part 1

    inp = [[i.split()[0], int(i.split()[1])] for i in f.readlines()]
    x = sum([i[1] for i in inp if i[0] == 'forward'])
    y = sum([i[1] * [-1, 1][i[0] == 'down']for i in inp if i[0] != 'forward'])
    print(x * y)

    # 1728414

    # ----------------------------------------------------------------

    # part 2

    aim, dep, x = 0, 0, 0

    for i in inp:
        if i[0] == 'forward':
            x += i[1]
            dep += aim * i[1]
        elif i[0] == 'down':
            aim += i[1]
        else:
            aim -= i[1]

    print(dep * x)
