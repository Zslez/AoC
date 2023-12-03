with open('2021/01/input.txt') as f:
    # part 1

    txt = [int(i) for i in f.readlines()]
    print(sum([txt[i] > txt[i - 1] for i in range(1, len(txt))]))

    # 1616

    # ----------------------------------------------------------------

    # part 2

    print(sum([sum(txt[i: i + 3]) > sum(txt[i - 1: i + 2]) for i in range(1, len(txt))]))

    # 1645
