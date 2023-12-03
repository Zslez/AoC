# FUNCTIONS

def get_string(string, steps, rules):
    for _ in range(steps):
        new_string = string[0]

        for i in range(len(string) - 1):
            new_string += rules[string[i] + string[i + 1]]

        string = new_string

    letters = sorted(list(set(string)))
    freq = {i: string[:-1].count(i) for i in letters}

    return string, freq




# MAIN

# TASK 1
# calculate the difference between the quantity of the most common element and the quantity of the least common after 10 steps
#
# TASK 2
# calculate the difference between the quantity of the most common element and the quantity of the least common after 40 steps

def main():
    with open('2021/14/input.txt') as f:
        inp = f.read()

    # INPUT FORMATTING

    polymer, rules = inp.split('\n\n')
    rules = [i.split(' -> ') for i in rules.split('\n')]
    rules = {i[0]: i[1] + i[0][1] for i in rules}

    # PART 1

    steps = 10

    for _ in range(steps):
        new_polymer = polymer[0]

        for i in range(len(polymer) - 1):
            new_polymer += rules[polymer[i] + polymer[i + 1]]

        polymer = new_polymer

    freq = sorted([polymer.count(i) for i in set(polymer)], reverse = True)

    print(freq[0] - freq[-1])

    # RESULT: 5656

    # ----------------------------------------------------------------

    # PART 2

    # APPROACH: 30 steps are missing; compute first the string of each rule pair after 15 steps, and their frequences,
    # then, compute the 25 steps polymer and add the frequencies of each pair (the 15 steps ones) in it to the total

    from time import time

    s = time()

    rules15 = {i: None for i in rules}
    freqs15 = {i: None for i in rules}

    for i in rules:
        rules15[i], freqs15[i] = get_string(i, 15, rules)

    letters = sorted(list(set(''.join(list(rules15)))))

    # almost found a way to compute it much faster (≈1.2s)

    '''freqs30 = {i: {j: 0 for j in letters} for i in rules}

    for i in freqs30:
        for j in rules15:
            c = rules15[i].count(j)

            for k in letters:
                freqs30[i][k] += freqs15[j].get(k, 0) * c
            
            freqs30[i][rules15[i][-1]] -= 1

        for j in letters:
            c = rules15[i].count(j * 3)

            if c > 0:
                for k in letters:
                    freqs30[i][k] += freqs15[j * 2].get(k, 0) * c

    #print(freqs30)

    freq = {i: 0 for i in letters}

    for i in freqs30:
        c = polymer.count(i)

        for j in letters:
            freq[j] += freqs30[i].get(j, 0) * c

    for i in letters:
        c = polymer.count(i * 3)

        if c > 0:
            for j in letters:
                freq[j] += freqs30[i * 2].get(j, 0) * c

    print(freq)

    freq[polymer[-1]] += 1
    freq = sorted(list(freq.values()))
    print(3 * (2 ** 40) + 1 - sum(freq)) # the lenght of the polymer after n steps is 3 * (2 ** n) + 1

    print(freq[-1] - freq[0])
    print(time() - s)

    input()'''

    polymer = ''.join([rules15[polymer[i: i + 2]][:-1] for i in range(len(polymer) - 1)]) + polymer[-1]

    # calculate the frequency of each letter after 40 steps

    freq = {i: 0 for i in letters}

    for i in rules15:
        c = polymer.count(i)

        for j in letters:
            freq[j] += freqs15[i].get(j, 0) * c

    # match also overlapping occurrences of 3

    for i in letters:
        c = polymer.count(i * 3)

        if c > 0:
            for j in letters:
                freq[j] += freqs15[i * 2].get(j, 0) * c

    # add the last that was removed before

    freq[polymer[-1]] += 1
    freq = sorted(list(freq.values()))

    print(freq[-1] - freq[0])
    print(time() - s)

    # RESULT: 12271437788530
    # SADLY COMPUTED IN: 34.3s



if __name__ == '__main__':
    main()
