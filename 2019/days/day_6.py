orbits = {}
outer_moons = []
outer_moon_dict = {}


def parse_orbit(orbit):
    input_array = orbit.split(')')
    return input_array[0], input_array[1]


def add_orbit(orbit):
    planet, moon = parse_orbit(orbit)
    if moon in orbits.keys():
        orbits[moon].append(planet)

    else:
        orbits[moon] = [planet]


def find_outer_orbits():
    total_moons = []
    moons_with_moon = []

    for planet in orbits.keys():
        total_moons.append(planet)

    for planet in orbits.keys():
        for inner in orbits[planet]:
            if inner not in moons_with_moon:
                moons_with_moon.append(inner)

    for r in total_moons:
        if r not in moons_with_moon:
            outer_moons.append(r)


def find_all_inner(the_moon, count, outer_moon):
    if the_moon in orbits.keys():
        for moon in orbits[the_moon]:
            if moon not in outer_moons:
                outer_moons.append(moon)

            if outer_moon in outer_moon_dict.keys():
                entry = {moon: count}
                outer_moon_dict[outer_moon].append(entry)
            return find_all_inner(moon, count + 1, outer_moon)
    else:
        return count


def find_total_inputs():
    find_outer_orbits()
    i = 0
    total = 0

    for moon in outer_moons:
        outer_moon_dict[moon] = []

    while i < len(outer_moons):
        moon = outer_moons[i]
        total += find_all_inner(moon, 0, moon)
        i += 1

    print(total)


def find_shortest_connection():
    you_nodes = outer_moon_dict["YOU"]
    santa_nodes = outer_moon_dict["SAN"]

    steps = None

    for ynode in you_nodes:
        for ykey in ynode.keys():
            for snode in santa_nodes:
                for skey in snode.keys():
                    if ykey == skey:
                        distance = ynode[ykey] + snode[skey]
                        if steps is None or distance < steps:
                            steps = distance

    print(steps)


def __main__():
    with open('2019/resources/txt/day6.txt') as text:
        planetary_map = text.read()
        planetary_map = planetary_map.splitlines()
        for x in planetary_map:
            add_orbit(x)

        find_total_inputs()
        find_shortest_connection()


__main__()
