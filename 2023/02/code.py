# MAIN

# TASK 1
# What is the sum of the IDs of the games possible with 12 red, 13 green and 14 blue?
#
# TASK 2
# What is the sum of the power of these sets?



def main():
    with open('2023/02/input.txt') as f:
        inp = [i.split(': ')[1] for i in f.read().split('\n')]

    # INPUT FORMATTING

    games = []

    for i in inp:
        games.append({'red': 0, 'green': 0, 'blue': 0})

        for j in i.split(';'):
            for k in j.split(', '):
                if 'red' in k:
                    games[-1]['red'] = max(games[-1]['red'], int(k.replace(' red', '')))
                elif 'green' in k:
                    games[-1]['green'] = max(games[-1]['green'], int(k.replace(' green', '')))
                elif 'blue' in k:
                    games[-1]['blue'] = max(games[-1]['blue'], int(k.replace(' blue', '')))

    # PART 1

    limit = {'red': 12, 'green': 13, 'blue': 14}
    count = 0

    result = int(len(inp) * (len(inp) + 1) / 2) # sum of all IDs

    for i in games:
        count += 1

        if i['red'] > limit['red'] or i['green'] > limit['green'] or i['blue'] > limit['blue']:
            result -= count # subtract ID when the game is not possible

    print(result)

    # RESULT: 2632

    # ----------------------------------------------------------------

    # PART 2

    print(sum([i['red'] * i['green'] * i['blue'] for i in games]))

    # RESULT: 69629



if __name__ == '__main__':
    main()
