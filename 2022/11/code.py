import math

# FUNCTIONS

def get_operation(string):
    if '+' in string:
        added_num = int(string.split('+ ')[1])
        return lambda x: x + added_num

    if string.split('* ')[1] == 'old':
        return lambda x: x * x

    mult_num = int(string.split('* ')[1])
    return lambda x: x * mult_num



# MAIN

# TASK 1
# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds.
# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
#
# TASK 2
# Worry levels are no longer divided by three after each item is inspected;
# you'll need to find another way to keep your worry levels manageable.
# Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

def main():
    with open('2022/11/input.txt') as f:
        inp = f.read().split('\n\n')

    # INPUT FORMATTING AND VARIABLES

    inp = [[j.split(': ')[1] for j in i.split('\n')[1:]] for i in inp]

    monkeys = []


    for i in inp:
        monkeys.append({
            'items': [int(j) for j in i[0].split(', ')],
            'oper': get_operation(i[1]),
            'test': int(i[2].split()[-1]),
            True: int(i[3].split()[-1]),
            False: int(i[4].split()[-1])
        })

    rounds = 20
    inspects = [0 for _ in monkeys]


    # PART 1

    for i in range(rounds):
        for j in range(len(monkeys)):
            monkey = monkeys[j]

            for k in monkey['items']:
                worry_level = monkey['oper'](k) // 3
                new_monkey = monkey[worry_level % monkey['test'] == 0]
                monkeys[new_monkey]['items'].append(worry_level)

            inspects[j] += len(monkey['items'])
            monkeys[j]['items'] = []

    sorted_inspects = list(sorted(inspects))[::-1]

    print(sorted_inspects[0] * sorted_inspects[1])

    # RESULT: 90294

    # ----------------------------------------------------------------

    # PART 2

    monkeys = []

    for i in inp:
        monkeys.append({
            'items': [int(j) for j in i[0].split(', ')],
            'oper': get_operation(i[1]),
            'test': int(i[2].split()[-1]),
            True: int(i[3].split()[-1]),
            False: int(i[4].split()[-1])
        })

    rounds = 10000
    inspects = [0 for _ in monkeys]

    common_multiple = math.lcm(*[i['test'] for i in monkeys])

    for i in range(rounds):
        for j in range(len(monkeys)):
            monkey = monkeys[j]

            for k in monkey['items']:
                worry_level = monkey['oper'](k)
                new_monkey = monkey[worry_level % monkey['test'] == 0]
                monkeys[new_monkey]['items'].append(worry_level % common_multiple)

            inspects[j] += len(monkey['items'])
            monkeys[j]['items'] = []

    inspects.sort(reverse = True)

    print(inspects[0] * inspects[1])

    # RESULT:



if __name__ == '__main__':
    main()
