import utility


class Board:
    def __init__(self, board_rows):
        self.board_size = len(board_rows)
        #board_rows = utility.split_list(board_rows, self.board_size)
        self.board = board_rows
        self.sorted_rows = [sorted(row) for row in board_rows]
        self.sorted_colums = [[] for i in range(self.board_size)]
        for row in board_rows:
            for x, value in enumerate(row):
                self.sorted_colums[x].append(value)
        self.sorted_colums = [sorted(column) for column in self.sorted_colums]

    def check_bingo(self, nums):
        sorted_nums = sorted(nums)
        for row in self.sorted_rows:
            if all(item in sorted_nums for item in row):
                return True
        for column in self.sorted_colums:
            if all(item in sorted_nums for item in column):
                return True
        return False

    def get_sum(self, winning_nums):
        sum = 0
        for row in self.sorted_rows:
            for num in row:
                if num not in winning_nums:
                    sum += num
        return sum


def create_boards(boards_input):
    current_board_rows = []
    boards = []
    for row in boards_input:
        if len(row) == 0:
            boards.append(Board(current_board_rows))
            current_board_rows = []
            continue
        current_board_rows.append([int(c) for c in row.split()])
    # Add last board
    boards.append(Board(current_board_rows))
    return boards


def check_bingo(boards, winning_numbers):
    winning_boards = []
    for board in boards:
        if board.check_bingo(winning_numbers):
            winning_boards.append(board)
    return winning_boards


def part1():
    input_file = utility.get_input_path('04', False)
    puzzle_input = utility.get_file_lines(input_file)
    winning_numbers = [int(c) for c in puzzle_input[0].split(',')]
    puzzle_input = puzzle_input[2:]
    boards = create_boards(puzzle_input)
    board_size = boards[0].board_size
    current_numbers = winning_numbers[0:board_size]
    current_pull_index = board_size
    winning_boards = []
    while len(winning_boards) == 0:
        current_numbers.append(winning_numbers[current_pull_index])
        winning_boards = check_bingo(boards, current_numbers)
        current_pull_index += 1

    if len(winning_boards) == 1:
        print(
            f'{winning_boards[0].get_sum(current_numbers) * current_numbers[-1]}')


def part2():
    input_file = utility.get_input_path('04', False)
    puzzle_input = utility.get_file_lines(input_file)
    winning_numbers = [int(c) for c in puzzle_input[0].split(',')]
    puzzle_input = puzzle_input[2:]
    boards = create_boards(puzzle_input)
    winning_boards = list(boards)
    last_num = -1
    while len(winning_boards) == len(boards):
        prev_last_num = last_num
        last_num = winning_numbers[-1]
        winning_boards = check_bingo(boards, winning_numbers)
        winning_numbers = winning_numbers[:-1]

    losing_board = [
        board for board in boards if board not in winning_boards][0]
    winning_numbers.append(last_num)
    winning_numbers.append(prev_last_num)
    print(
        f'{losing_board.get_sum(winning_numbers) * prev_last_num}')


if __name__ == '__main__':
    part2()
