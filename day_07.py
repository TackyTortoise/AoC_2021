import utility
import statistics


def get_fuel_for_pos(pos, try_target):
    return sum([abs(x - try_target) for x in pos])


def part1():
    input_file = utility.get_input_path('07', False)
    input_text = utility.get_file_text(input_file)
    pos = sorted([int(n) for n in input_text.split(',')])
    median_idx = len(pos) / 2
    if median_idx.is_integer():
        fuel = get_fuel_for_pos(pos, pos[int(median_idx)])
    else:
        i1 = int(median_idx - .5)
        i2 = int(median_idx + .5)
        f1 = get_fuel_for_pos(pos, pos[i1])
        f2 = get_fuel_for_pos(pos, pos[i2])
        fuel = min(f1, f2)
    print(fuel)


def get_inc_fuel_for_pos(pos, try_target):
    distances = [abs(x - try_target) for x in pos]
    return sum((sum(range(n + 1)) for n in distances))


def part2():
    input_file = utility.get_input_path('07', False)
    input_text = utility.get_file_text(input_file)
    pos = [int(n) for n in input_text.split(',')]
    avg = round(statistics.mean(pos))
    fs = []
    for i in range(-1, 1):
        fs.append(get_inc_fuel_for_pos(pos, avg + i))
    print(min(fs))


if __name__ == '__main__':
    part2()
