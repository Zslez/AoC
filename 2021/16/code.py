from math import prod


# FUNCTIONS


def find_subpack(binary):
    version = int(''.join(binary[:3]), 2)
    typeID = int(''.join(binary[3:6]), 2)
    binary = binary[6:]

    value = ''
    sub = None

    if typeID == 4:
        l = 6

        while True:
            value += ''.join(binary[1:5])
            l += 5

            if binary[0] == '0':
                binary = binary[5:]
                break

            binary = binary[5:]

        value = int(value, 2)
    else:
        lentypeID = binary.pop(0)

        sub = []

        if lentypeID == '0':
            total_len = int(''.join(binary[:15]), 2)
            binary = binary[15:]
            l = 0

            while l != total_len:
                l += len(binary)
                res = find_subpack(binary)
                sub.append(res[0])
                binary = res[1]
                l -= len(binary)
        else:
            subs = int(''.join(binary[:11]), 2)
            binary = binary[11:]

            for _ in range(subs):
                res = find_subpack(binary)
                sub.append(res[0])
                binary = res[1]

    subpack = {
        'version': version,
        'typeID': typeID,
        'value': value,
        'subpacks': sub
    }

    return subpack, binary


def get_version_sum(packs):
    v = packs['version']

    if packs['subpacks'] is not None:
        v += sum([get_version_sum(i) for i in packs['subpacks']])

    return v


def evaluate(packs):
    match packs['typeID']:
        case 0:
            return sum([evaluate(i) for i in packs['subpacks']])
        case 1:
            return prod([evaluate(i) for i in packs['subpacks']])
        case 2:
            return min([evaluate(i) for i in packs['subpacks']])
        case 3:
            return max([evaluate(i) for i in packs['subpacks']])
        case 4:
            return int(packs['value'])
        case 5:
            return [0, 1][evaluate(packs['subpacks'][0]) > evaluate(packs['subpacks'][1])]
        case 6:
            return [0, 1][evaluate(packs['subpacks'][0]) < evaluate(packs['subpacks'][1])]
        case 7:
            return [0, 1][evaluate(packs['subpacks'][0]) == evaluate(packs['subpacks'][1])]
        




# MAIN

# TASK 1
# calculate the sum of the version numbers in all packets
#
# TASK 2
# evaluate the expression represented by your hexadecimal-encoded BITS transmission

def main():
    with open('2021/16/input.txt') as f:
        inp = f.read()

    # INPUT FORMATTING

    convert = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    binary  = sum([[j for j in convert[i]] for i in inp], [])

    # PART 1

    packs = find_subpack(binary)[0]

    print(get_version_sum(packs))

    # RESULT: 923

    # ----------------------------------------------------------------

    # PART 2

    print(evaluate(packs))

    # RESULT: 258888628940



if __name__ == '__main__':
    main()
