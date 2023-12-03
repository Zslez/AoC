# FUNCTIONS

def get_diagram(inp):
    # new list containing as many empty lists as the number of columns in the input_diag

    diagram = [[] for _ in range(int(inp[-1].strip().split()[-1]))]

    for i in range(len(inp) - 1):
        row = inp[i]

        for j in range(len(row) // 4 + 1):
            if row[j * 4 + 1] != ' ':
                diagram[j].append(row[j * 4 + 1])

    return diagram




# MAIN

# TASK 1
# After the rearrangement procedure completes, what crate ends up on top of each stack?
#
# TASK 2
# ...

def main():
    with open('2022/05/input.txt') as f:
        inp = f.read().split('\n\n')

    # INPUT FORMATTING

    input_diag, moves = inp

    input_diag = input_diag.split('\n')
    diagram = get_diagram(input_diag)

    moves = moves.replace('move ', '').replace('from ', '').replace('to ', '').split('\n')
    moves = [[int(j) - 1 for j in i.split()] for i in moves]

    # PART 1

    for i in moves:
        for _ in range(i[0] + 1):
            diagram[i[2]] = [diagram[i[1]][0]] + diagram[i[2]]
            diagram[i[1]] = diagram[i[1]][1:]

    print(''.join([i[0] for i in diagram]))

    # RESULT: TGWSMRBPN

    # ----------------------------------------------------------------

    # PART 2

    diagram = get_diagram(input_diag)

    for i in moves:
        diagram[i[2]] = diagram[i[1]][:i[0] + 1] + diagram[i[2]]
        diagram[i[1]] = diagram[i[1]][i[0] + 1:]

    print(''.join([i[0] for i in diagram]))

    # RESULT: TZLTLWRNF



if __name__ == '__main__':
    main()
