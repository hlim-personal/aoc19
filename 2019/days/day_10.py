import math


def initialise_grid():
    with open("2019/resources/txt/day10.txt") as txt:
        grid = txt.read()
        grid = grid.split('\n')
        for i in range(len(grid)):
            grid[i] = list(grid[i])

        return grid


def get_asteroid_coordinates(grid):
    asteroids = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                asteroids.append([col, row])

    return asteroids


def get_best_asteroid(coordinates):
    best_asteroid = None
    best_angle_list = []
    for asteroid in coordinates:
        angle_list = []
        for other_asteroid in coordinates:
            if asteroid is not other_asteroid:
                angle = get_angle(asteroid, other_asteroid)
                if angle not in angle_list:
                    angle_list.append(angle)

        if len(angle_list) > len(best_angle_list):
            best_asteroid = asteroid
            best_angle_list = angle_list

    return best_asteroid, len(best_angle_list)


def organise_asteroids(best_asteroid, asteroids):
    ast_dict = {}
    for asteroid in asteroids:
        if asteroid is not best_asteroid:
            rel_angle = get_angle(best_asteroid, asteroid)
            rel_distance = get_distance(best_asteroid, asteroid)

            if not rel_angle in ast_dict.keys():
                ast_dict[rel_angle] = [
                    {"distance": rel_distance, "coordinate": asteroid}]
            else:
                ast_dict[rel_angle].append(
                    {"distance": rel_distance, "coordinate": asteroid})

    sorted_ast_dict = {}
    sorted_keys = sorted(ast_dict.keys())
    for key in sorted_keys:
        sorted_ast_dict[key] = sorted(
            ast_dict[key], key=lambda k: k['distance'])

    return sorted_ast_dict


def shoot_asteroids(ast_dict, n):
    sorted_asteroids = []
    keys = list(ast_dict.keys())
    angle_range = len(keys)

    i = 0
    while i < angle_range:
        key = keys[i]
        if key in ast_dict.keys():
            sorted_asteroids.append(ast_dict[key][0])
            del ast_dict[key][0]

            if len(ast_dict[key]) == 0:
                ast_dict.pop(key, None)

        if (i == angle_range - 1):
            i = 0
        else:
            i += 1

        if len(sorted_asteroids) == n:
            break

    print(sorted_asteroids[n - 1])


def get_angle(a, b):

    if b[0] == a[0]:
        return 0 if b[1] < a[1] else 180
    if b[1] == a[1]:
        return 90 if b[0] > a[0] else 270

    rel_x = b[0] - a[0]
    rel_y = b[1] - a[1]

    is_y_neg = rel_y < 0
    is_x_neg = rel_x < 0
    opposite = rel_y if not is_y_neg else rel_y * -1
    adjacent = rel_x if not is_x_neg else rel_x * -1

    angle = math.degrees(math.atan(opposite/adjacent))

    if not is_x_neg and is_y_neg:
        angle = 90 - angle
    elif not is_x_neg and not is_y_neg:
        angle += 90
    elif is_x_neg and not is_y_neg:
        angle = 90 - angle + 180
    elif is_x_neg and is_y_neg:
        angle += 270

    return angle


def get_distance(a, b):
    rel_x = b[0] - a[0]
    rel_y = b[1] - a[1]
    return math.sqrt(rel_x ** 2 + rel_y ** 2)


def __main__():
    grid = initialise_grid()
    coordinates = get_asteroid_coordinates(grid)

    best_asteroid, best_length = get_best_asteroid(coordinates)

    # part A
    print("************** PART A **************")
    print(best_asteroid, best_length)

    # part B
    ast_dict = organise_asteroids(best_asteroid, coordinates)
    print("************** PART B **************")
    shoot_asteroids(ast_dict, 200)


__main__()
