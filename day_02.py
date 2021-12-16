import utility


def part1():
    input_file = utility.get_input_path('02', False)
    instructions = utility.get_file_lines(input_file)
    horizontal, depth = 0, 0
    for i in instructions:
        command = i[0]
        value = int(i[-1])
        if command == 'f':
            horizontal += value
        elif command == 'd':
            depth += value
        elif command == 'u':
            depth -= value
    print(f'Horizontal: {horizontal}, Depth: {depth}')
    print(f'Result {horizontal * depth}')


def part2():
    input_file = utility.get_input_path('02', False)
    instructions = utility.get_file_lines(input_file)
    horizontal, depth, aim = 0, 0, 0
    for i in instructions:
        command = i[0]
        value = int(i[-1])
        if command == 'f':
            horizontal += value
            depth += aim * value
        elif command == 'd':
            aim += value
        elif command == 'u':
            aim -= value
    print(f'Horizontal: {horizontal}, Depth: {depth}, Aim: {aim}')
    print(f'Result {horizontal * depth}')


if __name__ == "__main__":
    part2()
