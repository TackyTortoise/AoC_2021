import utility


def part1():
    nums = utility.get_file_lines_as_int('input/01.txt')
    counter = 0
    for n in range(1, len(nums)):
        if nums[n] > nums[n-1]:
            counter += 1
    print(counter)


def part2():
    nums = utility.get_file_lines_as_int('input/01.txt')
    counter = 0
    chuncks = utility.chunk_list(nums, 3)
    sums = [sum(c) for c in chuncks]
    for n in range(1, len(sums)):
        if sums[n] > sums[n-1]:
            counter += 1
    print(counter)


if __name__ == "__main__":
    part2()
