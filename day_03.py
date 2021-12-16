import utility


def count_bits(records, count_size, count_start=0):
    ones = {}
    zeros = {}
    for i in range(count_start, count_size):
        ones[i] = 0
        zeros[i] = 0
    for row in records:
        for i, bit in enumerate(row):
            if i < count_start:
                continue
            if i > count_size:
                break
            if bit == '0':
                zeros[i] += 1
            elif bit == '1':
                ones[i] += 1
    return (ones, zeros)


def part1():
    input_file = utility.get_input_path('03', False)
    report = utility.get_file_lines(input_file)
    row_length = len(report[0])
    ones, zeros = count_bits(report, row_length)
    result = ''
    for i in range(0, row_length):
        zeroscount = zeros[i]
        onescount = ones[i]
        result += '0' if zeroscount > onescount else '1'
    print(f'Binary result: {result}')
    gamma = int(result, 2)
    print(f'Gamma: {gamma}')
    epsilon = ''.join(['1' if c == '0' else '0' for c in result])
    epsilon = int(epsilon, 2)
    print(f'Epsilon: {epsilon}')
    print(f'Result: {gamma * epsilon}')


def part2():
    input_file = utility.get_input_path('03', False)
    rows = utility.get_file_lines(input_file)
    row_length = len(rows[0])
    oxygen_to_find = ''
    for i in range(0, row_length):
        ones, zeros = count_bits(rows, row_length, i)
        oxygen_to_find += '1' if ones[i] >= zeros[i] else '0'
        rows = [row for row in rows if row.startswith(oxygen_to_find)]
        if len(rows) == 1:
            print(f'Oxygen row: {rows[0]}')
            oxygen_to_find = rows[0]
            break

    rows = utility.get_file_lines(input_file)
    co_to_find = ''
    for i in range(0, row_length):
        ones, zeros = count_bits(rows, row_length, i)
        co_to_find += '1' if ones[i] < zeros[i] else '0'
        rows = [row for row in rows if row.startswith(co_to_find)]
        ones, zeros = count_bits(rows, row_length, i)
        if len(rows) == 1:
            print(f'CO2 row: {rows[0]}')
            co_to_find = rows[0]
            break

    print(f'Result: {int(oxygen_to_find, 2) * int(co_to_find, 2)} ')


if __name__ == '__main__':
    part2()
