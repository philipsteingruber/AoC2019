from itertools import combinations

def part1():
    with open('input.txt') as file:
        positions = list(map(int, file.read().split(',')))
    current_position = 0
    positions[1] = 12
    positions[2] = 2
    while current_position < len(positions):
        operation = positions[current_position]
        if operation == 99:
            print('Part 1:', positions[0])
            break
        elif operation == 1:
            operands = [positions[positions[current_position+1]], positions[positions[current_position+2]]]
            output_slot = positions[current_position+3]
            positions[output_slot] = sum(operands)
        elif operation == 2:
            operands = [positions[positions[current_position+1]], positions[positions[current_position+2]]]
            output_slot = positions[current_position+3]
            positions[output_slot] = operands[0] * operands[1]
        current_position += 4


def part2():
    current_position = 0
    wanted_result = 19690720
    combs = iter(combinations(range(100), 2))
    current_result = 0
    current_comb = None
    while current_result != wanted_result:
        positions = reset_memory()
        current_comb = next(combs)
        print(current_comb)
        positions[1], positions[2] = current_comb
        print(positions[1], positions[2])
        while current_position < len(positions):
            operation = positions[current_position]
            if operation == 99:
                current_result = positions[0]
                break
            elif operation == 1:
                operands = [positions[positions[current_position + 1]], positions[positions[current_position + 2]]]
                output_slot = positions[current_position + 3]
                positions[output_slot] = sum(operands)
            elif operation == 2:
                operands = [positions[positions[current_position + 1]], positions[positions[current_position + 2]]]
                output_slot = positions[current_position + 3]
                positions[output_slot] = operands[0] * operands[1]
            current_position += 4
    print('Part 2:', 100 * current_comb[0] + current_comb[1])

def reset_memory():
    with open('input.txt') as file:
        positions = list(map(int, file.read().split(',')))
        return positions

def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
