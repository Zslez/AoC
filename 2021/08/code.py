# TASK 1
# count how many times in the output values digits 1, 4, 7, or 8 appear
#
# TASK 2
# calculate the sum of all the output values

def main():
    with open('2021/08/input.txt') as f:
        inp = f.read().split('\n')

    # INPUT FORMATTING

    inp, out = [[i.split(' | ')[0] for i in inp], [i.split(' | ')[1] for i in inp]]

    # PART 1

    print(len([j for j in sum([i.split() for i in out], []) if len(j) in (2, 3, 4, 7)]))

    # RESULT: 330

    # ----------------------------------------------------------------

    # PART 2

    # 3 has 4 in common with 5
    # 3 has 4 in common with 2
    # 2 has 3 in common with 5

    # 0 has 5 in common with 6
    # 0 has 5 in common with 9
    # 6 has 4 in common with 9

    # STEPS

    # 3 is the only of 5 that has the 1 in it
    # 2 has a stroke that 9 does not have and 5 not
    # 5 will be the only one left of length 5

    # 9 is the only of 6 that has the 4 in it
    # 0 and 9 are the only of 6 that have the 7 in it
    # 6 will be the only one left of length 6

    result = 0

    for i in range(len(inp)):
        nums = {i: '' for i in range(10)}

        codes = inp[i].split()

        # first recognise the unique numbers

        for j in codes:
            l = len(j)

            if l == 2:
                nums[1] = j
            elif l == 3:
                nums[7] = j
            elif l == 4:
                nums[4] = j
            elif l == 7:
                nums[8] = j

        # then determine all the others
        # NOTE: sort the codes in descending length because having determined 9 is necessary to determine 2

        for j in sorted(codes, key = lambda x: len(x), reverse = True):
            l = len(j)

            # 2, 3, 5

            if l == 5:
                if all([k in j for k in nums[1]]):
                    nums[3] = j
                elif any([i not in nums[9] for i in j]):
                    nums[2] = j
                else:
                    nums[5] = j

            # 0, 6, 9

            elif l == 6:
                if all([k in j for k in nums[4]]):
                    nums[9] = j
                elif all([k in j for k in nums[7]]):
                    nums[0] = j
                else:
                    nums[6] = j

        res = ''

        for j in out[i].split():
            for k in nums:
                if sorted(j) == sorted(nums[k]):
                    res += str(k)

        result += int(res)

    print(result)

    # RESULT: 1010472



if __name__ == '__main__':
    main()
