import utility


def part1():
    # Brute force yolo
    input_file = utility.get_input_path('06', False)
    input_text = utility.get_file_text(input_file)
    fish = [int(n) for n in input_text.split(',')]
    days = 80
    for i in range(0, days):
        fish_to_add = 0
        for idx, _ in enumerate(fish):
            fish[idx] -= 1
            if fish[idx] == -1:
                fish_to_add += 1
                fish[idx] = 6
        if fish_to_add > 0:
            fish += [8] * fish_to_add
    print(len(fish))


def part2():
    input_file = utility.get_input_path('06', False)
    input_text = utility.get_file_text(input_file)
    fish = [int(n) for n in input_text.split(',')]

    life_count = [0] * 9
    days = 256
    for f in fish:
        life_count[f] += 1
    for _ in range(0, days):
        zero_count = life_count[0]
        for day in range(0, len(life_count) - 1):
            life_count[day] = life_count[day + 1]
        life_count[-1] = zero_count
        life_count[6] += zero_count

    print(sum(life_count))


if __name__ == '__main__':
    part2()
