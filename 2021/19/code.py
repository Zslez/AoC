# VARIABLES

ORIENTATIONS = [
    (lambda x, y, z:  ( x,  y,  z)),
    (lambda x, y, z:  ( x,  z, -y)),
    (lambda x, y, z:  ( x, -y, -z)),
    (lambda x, y, z:  ( x, -z,  y)),

    (lambda x, y, z:  (-x,  y, -z)),
    (lambda x, y, z:  (-x,  z,  y)),
    (lambda x, y, z:  (-x, -y,  z)),
    (lambda x, y, z:  (-x, -z, -y)),

    (lambda x, y, z:  ( y, -z, -x)),
    (lambda x, y, z:  ( y, -x,  z)),
    (lambda x, y, z:  ( y,  z,  x)),
    (lambda x, y, z:  ( y,  x, -z)),

    (lambda x, y, z:  (-y, -z,  x)),
    (lambda x, y, z:  (-y, -x, -z)),
    (lambda x, y, z:  (-y,  z, -x)),
    (lambda x, y, z:  (-y,  x,  z)),

    (lambda x, y, z:  ( z,  y, -x)),
    (lambda x, y, z:  ( z, -x, -y)),
    (lambda x, y, z:  ( z, -y,  x)),
    (lambda x, y, z:  ( z,  x,  y)),

    (lambda x, y, z:  (-z,  y,  x)),
    (lambda x, y, z:  (-z, -x,  y)),
    (lambda x, y, z:  (-z, -y, -x)),
    (lambda x, y, z:  (-z,  x, -y))
]




# FUNCTIONS AND CLASSES

class Scanner:
    def __init__(self, scan):
        self.scan = scan
        self.orientations = self.get_orientations()

    def get_orientations(self):
        return [tuple([i(*j) for j in self.scan]) for i in ORIENTATIONS]

    def translate(self, coordinates):
        return [tuple([tuple([j[k] + coordinates[k] for k in range(3)]) for j in i]) for i in self.orientations]



def get_common(scan1, scan2):
    orients1, orients2 = scan1.orientations, scan2.orientations

    for x in range(-100, 100):
        for y in range(-100, 100):
            for z in range(-100, 100):
                common = []

                for i in orients1:
                    if any([i in j for j in scan2.translate((x, y, z))]):
                        common.append(i)

                if len(common) >= 1:
                    return common

    return common




# MAIN

# TASK 1
# find the total number of beacons in the map
#
# TASK 2
# ...

def main():
    with open('2021/19/example copy.txt') as f:
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
