# FUNCTIONS

def paths_to_end(graph, cave, exclude = list(), path = None):
    paths = []

    if path == None:
        path = ['start', cave]

    # I make copies of the arguments to modify their value only in the following recursions and not in the current

    newpath = path.copy()

    # for every cave that can be visited from the current

    for i in sorted(graph[cave]):
        # when a small cave is visited it gets marked as excluded in the subsequent recursion
        # and if a cave connected to the current is in excluded it should be ignored

        if i in exclude:
            continue

        # if end is reached skip the iteration part, save the path and go to the next iteration

        if i == 'end':
            paths.append(path)
            continue

        newpath.append(i)

        # same reason here

        new_exclude = exclude.copy()

        # if the cave is small, exclude it

        if cave.lower() == cave:
            new_exclude.append(cave)

        # calculate the paths starting from the new selected cave (recursion)

        paths += paths_to_end(graph, i, new_exclude, newpath)

        newpath.pop()

    return paths



def paths_to_end_part2(graph, cave, exclude = list(), path = None, reuse_cave = None):
    paths = []
    small_cave = reuse_cave

    if path == None:
        path = ('start', cave)

    # I convert path to list every time to use methods as .append and .pop
    # but reconvert it back to tuple every time to be able to use list(set()) at the end
    # as list is not an hashable type and list(set()) is the most efficient way to remove duplicates

    newpath = list(path)

    # for every cave that can be visited from the current

    for i in sorted(graph[cave]):
        # when a small cave is visited it gets marked as excluded in the subsequent recursion
        # and if a cave connected to the current is in excluded it should be ignored

        if i in exclude:
            continue

        # if end is reached skip the iteration part, save the path and go to the next iteration

        if i == 'end':
            paths.append(path + ('end',))
            continue

        newpath.append(i)

        new_exclude = exclude.copy()

        # try both the path excluding the encountered small cave and the path with that cave selected as reused
        # this however leads to saving some duplicates (I don't want to think of a way to avoid this)

        if cave.lower() == cave:
            if reuse_cave == None:
                small_cave = cave
            else:
                new_exclude.append(cave)

        # calculate the paths starting from the new selected cave (recursion)

        paths += paths_to_end_part2(graph, i, new_exclude, tuple(newpath), small_cave)

        # if a small cave was encountered and so far no small cave was already used twice (aka reuse_cave == None)
        # then calculate also the paths with this cave not selected as reused and so including it in the excluded list

        # this allows the code to reuse also small caves not encountered as first like
        # start,A,c,A,b,A,b,end - where b is used twice even though c was encountered first

        if reuse_cave == None and small_cave != None:
            paths += paths_to_end_part2(graph, i, new_exclude + [cave], tuple(newpath), None)

        newpath.pop()

    # remove duplicates and return the paths

    return list(set(paths))




# MAIN

# TASK 1
# find how many paths through this cave system there are that visit small caves at most once
#
# TASK 2
# find how many paths through this cave system there are that visit
# one small cave at most twice and all the remaining small caves at most once 💀

def main():
    with open('2021/12/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    links = [i.split('-') for i in inp]
    positions = set(sum(links, []))
    graph = {i: [] for i in positions}

    for i in links:
        if i[1] != 'start':
            graph[i[0]].append(i[1])

        if i[0] != 'start':
            graph[i[1]].append(i[0])

    # PART 1

    print(len(sum([paths_to_end(graph, cave) for cave in graph['start']], [])))

    # RESULT: 3576

    # ----------------------------------------------------------------

    # PART 2

    print(len(sum([paths_to_end_part2(graph, cave) for cave in graph['start']], [])))

    # RESULT: 84271



if __name__ == '__main__':
    main()
