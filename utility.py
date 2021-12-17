def get_input_path(file_name, is_test):
    prefix = 'testinput' if is_test else 'input'
    return f'{prefix}/{file_name}.txt'


def get_file_text(path):
    with open(path) as f:
        return f.read()


def get_file_lines(path):
    with open(path) as f:
        return [l.strip() for l in f.readlines()]


def get_file_lines_as_int(path):
    return [int(x) for x in get_file_lines(path)]


def chunk_list(list, chunk_size):
    return [list[pos:pos + chunk_size] for pos in range(0, len(list))]


def split_list(list, chunk_size):
    return [list[pos:pos + chunk_size] for pos in range(0, len(list), chunk_size)]
