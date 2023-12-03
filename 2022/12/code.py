# FUNCTIONS

def find_shortest_path_from_S_to_E(start_pos, end_pos, inp, width, height):
    steps = 0
    reached_cells = {start_pos: 0}
    dirs = [-1, -width, 1, width]


    while end_pos not in reached_cells:
        for cell in range(len(inp)):
            if cell not in reached_cells:
                continue

            if reached_cells[cell] == steps:
                for d in dirs:
                    newcell = cell + d

                    if newcell in reached_cells:
                        continue

                    # remove directions that are out of bounds

                    if (d == 1 and newcell % width == 0) or (d == -1 and newcell % width == width - 1):
                        continue 

                    if newcell < 0 or newcell >= width * height:
                        continue

                    # check if new cell is not too high to be reached

                    if inp[newcell] - inp[cell] > 1:
                        continue

                    # add new reached cells

                    reached_cells[newcell] = steps + 1
        
        steps += 1

    return reached_cells



def find_shortest_path_from_E_to_a(end_pos, inp, width, height):
    steps = 0
    reached_cells = {end_pos: 0}
    dirs = [-1, -width, 1, width]


    while True:
        for cell in range(len(inp)):
            if cell not in reached_cells:
                continue

            if reached_cells[cell] == steps:
                for d in dirs:
                    newcell = cell + d

                    if newcell in reached_cells:
                        continue

                    # remove directions that are out of bounds

                    if (d == 1 and newcell % width == 0) or (d == -1 and newcell % width == width - 1):
                        continue 

                    if newcell < 0 or newcell >= width * height:
                        continue

                    # check if new cell is not too high to be reached

                    if inp[cell] - inp[newcell] > 1:
                        continue

                    # add new reached cells

                    reached_cells[newcell] = steps + 1

                    if inp[newcell] == 1:
                        return reached_cells
        
        steps += 1




# MAIN

# TASK 1
# What is the fewest steps required to move from your current position
# to the location that should get the best signal?
#
# TASK 2
# What is the fewest steps required to move starting from any square with elevation a
# to the location that should get the best signal?

def main():
    with open('2022/12/input.txt') as f:
        inp = f.read().split('\n')


    # INPUT FORMATTING

    inp = [[ord(j) - 96 if j not in ['S', 'E'] else [0, 27][j == 'E'] for j in list(i)] for i in inp]
    width, height = len(inp[0]), len(inp)
    inp = sum(inp, [])

    start_pos = 0
    end_pos = 0

    # find start position

    for i in range(len(inp)):
        if inp[i] == 0:
            start_pos = i
            inp[i] = 1 # now S can be a normal a

    # find end position

    for i in range(len(inp)):
        if inp[i] == 27:
            end_pos = i
            inp[i] = 26 # now E can be a normal z


    # PART 1

    reached_cells = find_shortest_path_from_S_to_E(start_pos, end_pos, inp, width, height)

    print(reached_cells[end_pos])

    # RESULT: 394

    # ----------------------------------------------------------------


    # PART 2

    reached_cells = find_shortest_path_from_E_to_a(end_pos, inp, width, height)

    print(max(reached_cells.values()))

    # RESULT: 388



if __name__ == '__main__':
    main()
