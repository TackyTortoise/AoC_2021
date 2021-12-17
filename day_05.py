import utility


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

# Check if we passed bounds, based on directoin


def dbs(dir, a, b):
    if dir > 0:
        return a < b
    return b < a


def get_points_between(point_a, point_b):
    # Horizontal line
    if point_a.y == point_b.y:
        smallest = min(point_a.x, point_b.x)
        biggest = max(point_a.x, point_b.x)
        points = [Point(x, point_a.y) for x in range(smallest, biggest + 1)]
        return points
    # Vertical line
    elif point_a.x == point_b.x:
        smallest = min(point_a.y, point_b.y)
        biggest = max(point_a.y, point_b.y)
        points = [Point(point_a.x, y) for y in range(smallest, biggest + 1)]
        return points
    # Diagonal
    else:
        x_dir = 1 if point_b.x > point_a.x else -1
        y_dir = 1 if point_b.y > point_a.y else -1
        filled_points = []
        current_point = Point(point_a.x, point_a.y)
        while dbs(x_dir, current_point.x, point_b.x) and dbs(y_dir, current_point.y, point_b.y):
            filled_points.append(Point(current_point.x, current_point.y))
            current_point.x += x_dir
            current_point.y += y_dir
        filled_points.append(point_b)
        return filled_points


def part1():
    input_file = utility.get_input_path('05', False)
    input_lines = utility.get_file_lines(input_file)
    filled = {}
    for line in input_lines:
        from_to = line.split(' -> ')
        point_a = Point(*from_to[0].split(','))
        point_b = Point(*from_to[1].split(','))
        points = get_points_between(point_a, point_b)
        for point in points:
            tup = (point.x, point.y)
            if not tup in filled:
                filled[tup] = 0
            filled[tup] += 1
    overdraw_points = [(x, y) for (x, y), v in filled.items() if v > 1]
    print(len(overdraw_points))


def part2():
    part1()


if __name__ == '__main__':
    part2()
