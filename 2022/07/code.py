# FUNCTIONS

def format_path(path):
    return '/'.join(path)[1:]


def get_size(dir, structure):
    size = sum(structure[dir])

    for i in structure:
        if i.startswith(dir) and i != dir:
            size += sum(structure[i])

    return size




# MAIN

# TASK 1
# Find the sum of the sizes of the directories with a total size of at most 100000
#
# TASK 2
# Find the size of smallest directory that deleted would free up enough space to run the update

def main():
    with open('2022/07/input.txt') as f:
        inp = f.read().split('\n')

    # PART 1

    path = []
    struct = {}

    for i in inp:
        if i.startswith('$ cd'):
            i = i[5:]

            if i == '..':
                path.pop()
            else:
                path.append(i)
                struct[format_path(path)] = []
        elif not i.startswith('$') and not i.startswith('dir'):
            struct[format_path(path)].append(int(i.split()[0]))

    new_struct = {}

    for i in struct:
        new_struct[i] = get_size(i, struct)

    print(sum(list(filter(lambda x: x < 100000, new_struct.values()))))

    # RESULT: 1453349

    # ----------------------------------------------------------------

    # PART 2

    space_to_free = new_struct[''] - 40000000

    print(list(sorted(filter(lambda x: x >= space_to_free, new_struct.values())))[0])

    # RESULT: 2948823



if __name__ == '__main__':
    main()
