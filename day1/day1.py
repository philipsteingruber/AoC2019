def part1():
    with open('input.txt') as file:
        weights = list(map(int, file.readlines()))

    sum_of_fuel = 0
    for weight in weights:
        fuel_weight = int(weight/3) - 2
        # print('Module with weight {} requires {} fuel.'.format(weight, fuel_weight))
        sum_of_fuel += fuel_weight
    print('Part 1:', sum_of_fuel)


def part2():
    with open('input.txt') as file:
        weights = list(map(int, file.readlines()))

    sum_of_fuel = 0
    for weight in weights:
        fuel_weight = part2_recursive(0, weight)
        # print('Module with weight {} requires {} fuel.'.format(weight, fuel_weight))
        sum_of_fuel += fuel_weight
    print('Part 2:', sum_of_fuel)


def part2_recursive(rolling_sum, weight):
    new_weight = int(weight/3) - 2
    if new_weight <= 0:
        return rolling_sum
    else:
        return part2_recursive(rolling_sum+new_weight, new_weight)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
