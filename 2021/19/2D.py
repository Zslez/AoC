from math import dist
from itertools import combinations


# VARIABLES

ORIENTATIONS = [
    (lambda x, y:  ( x,  y)),
    (lambda x, y:  ( y, -x)),
    (lambda x, y:  (-x, -y)),
    (lambda x, y:  (-y,  x))
]




# FUNCTIONS AND CLASSES

class Scanner:
    def __init__(self, scan):
        self.scan = scan
        self.orientations = self.get_orientations()

    def get_orientations(self):
        return [tuple([i(*j) for j in self.scan]) for i in ORIENTATIONS]

    def translate(self, coordinates):
        return [tuple([tuple([j[k] + coordinates[k] for k in range(2)]) for j in i]) for i in self.orientations]



def get_common(scan1, scan2):
    orients1, orients2 = scan1.orientations, scan2.orientations

    #for i in range(4):
    #    print(f'{str(orients1[i]):30}', orients2[i], sep = '   ')

    dists1 = [dist(*k) for k in combinations(scan1.scan, 2)]
    dists2 = [dist(*k) for k in combinations(scan2.scan, 2)]

    for i in orients1:
        print(dists1)
        print(dists2)

        for j in combinations(i, 2):
            print(j)

    return




# MAIN

# TASK 1
# find the total number of beacons in the map
#
# TASK 2
# ...

def main():
    with open('2021/19/2D.txt') as f:
        inp = f.read().split('\n\n')

    # INPUT FORMATTING

    inp = [tuple([tuple([int(k) for k in j.split(',')]) for j in i.split('\n')[1:]]) for i in inp]
    inp = [Scanner(i) for i in inp]

    # PART 1

    print(get_common(inp[0], inp[1]))

    # RESULT:

    # ----------------------------------------------------------------

    # PART 2

    # ...

    # RESULT:



if __name__ == '__main__':
    main()
