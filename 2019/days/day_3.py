import re
import collections

lines = []
wires = []


def parse_input(str):
    direction = str[0]
    distance = int(str[1:])
    return direction, distance


def plot_line(direction, distance, starting_point):
    x, y = starting_point[0], starting_point[1]
    line = []
    steps = 0

    while steps < distance:
        if (direction == 'R'):
            x += 1
        elif (direction == 'L'):
            x -= 1
        elif (direction == 'U'):
            y += 1
        elif (direction == 'D'):
            y -= 1

        line.append(tuple([x, y]))
        steps += 1

    final_point = [x, y]
    return line, final_point


def parse_inputs():
    with open("resources/day3.txt") as fp:
        inputs = fp.read()
        unparsed_lines = re.split(r'\n', inputs)

        for line in unparsed_lines:
            parsed_line = re.split(r',', line)
            lines.append(parsed_line)


def translate():
    parse_inputs()

    for line in lines:
        origin = [0, 0]
        wire_points = []
        for point in line:
            direction, distance = parse_input(point)
            new_line, new_point = plot_line(direction, distance, origin)
            wire_points.extend(new_line)
            origin = new_point
        wires.append(tuple(wire_points))

    intersections = set(wires[0]).intersection(*wires)

    calc_shortest_intersection(intersections)
    calc_shortest_distance(intersections)


def calc_shortest_intersection(intersections):
    print(intersections)
    shortest_distance = None

    for intersection in intersections:
        manhattan_distance = get_manhattan_distance(intersection)
        if (shortest_distance == None or manhattan_distance < shortest_distance):
            shortest_distance = manhattan_distance

    print(shortest_distance)


def get_manhattan_distance(point):
    x, y = point[0], point[1]
    if (x < 0):
        x = x * -1
    if (y < 0):
        y = y * -1

    return x + y


def calc_shortest_distance(intersections):
    shortest_distance = None

    for intersection in intersections:
        distances = []
        for wire in wires:
            if intersection in wire:
                distances.append(wire.index(intersection) + 1)
        distances.sort()
        if distances != None:
            distance = distances[0] + distances[1]
            if (shortest_distance == None or distance < shortest_distance):
                shortest_distance = distance

    print(shortest_distance)


translate()
