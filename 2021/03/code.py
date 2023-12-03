with open('2021/03/input.txt') as f:
    # part 1

    inp = [i[::-1].strip() for i in f.readlines()]
    gamma = 0

    for i in range(len(inp[0])):
        gamma += [0, 2 ** i][sum([j[i] == '1' for j in inp]) > len(inp) / 2]

    epsilon = 2 ** 12 - gamma - 1

    print(gamma * epsilon)

    # 775304

    # ----------------------------------------------------------------

    # part 2

    remaining = [i[::-1] for i in inp]
    oxigen, co2 = remaining.copy(), remaining.copy()

    for i in range(len(inp[0])):
        most_common = ['0', '1'][sum([j[i] == '1' for j in oxigen]) >= len(oxigen) / 2]
        oxigen = [j for j in oxigen if j[i] == most_common]

        if len(oxigen) == 1:
            break

    for i in range(len(inp[0])):
        least_common = ['0', '1'][sum([j[i] == '1' for j in co2]) < len(co2) / 2]
        co2 = [j for j in co2 if j[i] == least_common]

        if len(co2) == 1:
            break

    print(int(oxigen[0], 2) * int(co2[0], 2))
    
    # 1370737
