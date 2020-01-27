from collections import defaultdict
import re
from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.pos = {
            "x": x,
            "y": y,
            "z": z
        }

        self.velocity = {
            "x": 0,
            "y": 0,
            "z": 0
        }

        self.initial_pos = {
            "x": x,
            "y": y,
            "z": z
        }

    def update_velocity_by_axis(self, axis, value):
        self.velocity[axis] += value
        self.pos[axis] += self.velocity[axis]

    def update_velocity(self, x, y, z):
        self.update_velocity_by_axis("x", x)
        self.update_velocity_by_axis("y", y)
        self.update_velocity_by_axis("z", z)

    def get_total_energy(self):
        potential_energy = abs(self.pos["x"]) + \
            abs(self.pos["y"]) + abs(self.pos["z"])
        kinetic_energy = abs(self.velocity["x"]) + \
            abs(self.velocity["y"]) + abs(self.velocity["z"])

        return potential_energy * kinetic_energy

    def is_initial(self, axis):
        return self.pos[axis] == self.initial_pos[axis] and self.velocity[axis] == 0


def compare(moon_a, moon_b):
    dvelocity_a, dvelocity_b = {}, {}  # x, y, z

    for axis in moon_a.pos.keys():
        if moon_a.pos[axis] > moon_b.pos[axis]:
            dvelocity_a[axis] = -1
            dvelocity_b[axis] = 1
        elif moon_a.pos[axis] < moon_b.pos[axis]:
            dvelocity_a[axis] = 1
            dvelocity_b[axis] = -1
        elif moon_a.pos[axis] == moon_b.pos[axis]:
            dvelocity_a[axis] = 0
            dvelocity_b[axis] = 0

    return dvelocity_a, dvelocity_b


def compare_by_axis(axis, moon_a, moon_b):
    dvelocity_a, dvelocity_b = 0, 0

    if moon_a.pos[axis] > moon_b.pos[axis]:
        dvelocity_a = -1
        dvelocity_b = 1
    elif moon_a.pos[axis] < moon_b.pos[axis]:
        dvelocity_a = 1
        dvelocity_b = -1

    return dvelocity_a, dvelocity_b


def step(moon_a, moon_b, moon_c, moon_d):
    total_dvelocity_a, total_dvelocity_b, total_dvelocity_c, total_dvelocity_d = defaultdict(
        int), defaultdict(int), defaultdict(int), defaultdict(int)

    dv_a_1, dv_b_1 = compare(moon_a, moon_b)
    dv_a_2, dv_c_1 = compare(moon_a, moon_c)
    dv_a_3, dv_d_1 = compare(moon_a, moon_d)
    dv_b_2, dv_c_2 = compare(moon_b, moon_c)
    dv_b_3, dv_d_2 = compare(moon_b, moon_d)
    dv_c_3, dv_d_3 = compare(moon_c, moon_d)

    list_a = [dv_a_1, dv_a_2, dv_a_3]
    list_b = [dv_b_1, dv_b_2, dv_b_3]
    list_c = [dv_c_1, dv_c_2, dv_c_3]
    list_d = [dv_d_1, dv_d_2, dv_d_3]

    for dv in list_a:
        for axis in dv.keys():
            total_dvelocity_a[axis] += dv[axis]

    for dv in list_b:
        for axis in dv.keys():
            total_dvelocity_b[axis] += dv[axis]

    for dv in list_c:
        for axis in dv.keys():
            total_dvelocity_c[axis] += dv[axis]

    for dv in list_d:
        for axis in dv.keys():
            total_dvelocity_d[axis] += dv[axis]

    moon_a.update_velocity(
        total_dvelocity_a["x"], total_dvelocity_a["y"], total_dvelocity_a["z"])
    moon_b.update_velocity(
        total_dvelocity_b["x"], total_dvelocity_b["y"], total_dvelocity_b["z"])
    moon_c.update_velocity(
        total_dvelocity_c["x"], total_dvelocity_c["y"], total_dvelocity_c["z"])
    moon_d.update_velocity(
        total_dvelocity_d["x"], total_dvelocity_d["y"], total_dvelocity_d["z"])


def step_by_axis(axis, moon_a, moon_b, moon_c, moon_d):
    dv_a_1, dv_b_1 = compare_by_axis(axis, moon_a, moon_b)
    dv_a_2, dv_c_1 = compare_by_axis(axis, moon_a, moon_c)
    dv_a_3, dv_d_1 = compare_by_axis(axis, moon_a, moon_d)
    dv_b_2, dv_c_2 = compare_by_axis(axis, moon_b, moon_c)
    dv_b_3, dv_d_2 = compare_by_axis(axis, moon_b, moon_d)
    dv_c_3, dv_d_3 = compare_by_axis(axis, moon_c, moon_d)

    total_dvelocity_a = dv_a_1 + dv_a_2 + dv_a_3
    total_dvelocity_b = dv_b_1 + dv_b_2 + dv_b_3
    total_dvelocity_c = dv_c_1 + dv_c_2 + dv_c_3
    total_dvelocity_d = dv_d_1 + dv_d_2 + dv_d_3

    moon_a.update_velocity_by_axis(axis, total_dvelocity_a)
    moon_b.update_velocity_by_axis(axis, total_dvelocity_b)
    moon_c.update_velocity_by_axis(axis, total_dvelocity_c)
    moon_d.update_velocity_by_axis(axis, total_dvelocity_d)


def part_a(moon_a, moon_b, moon_c, moon_d):
    for _ in range(1000):
        step(moon_a, moon_b, moon_c, moon_d)

    print(moon_a.pos, moon_a.get_total_energy())
    print(moon_b.pos, moon_b.get_total_energy())
    print(moon_c.pos, moon_c.get_total_energy())
    print(moon_d.pos, moon_d.get_total_energy())

    total_energy = moon_a.get_total_energy() + moon_b.get_total_energy() + \
        moon_c.get_total_energy() + moon_d.get_total_energy()

    print(total_energy)


def is_equal_by_axis(axis, moon_a, moon_b, moon_c, moon_d):
    i = 1
    while True:
        step_by_axis(axis, moon_a, moon_b, moon_c, moon_d)
        if moon_a.is_initial(axis) and moon_b.is_initial(axis) and moon_c.is_initial(axis) and moon_d.is_initial(axis):
            return i
        i += 1


def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def part_b(moon_a, moon_b, moon_c, moon_d):
    x = is_equal_by_axis("x", moon_a, moon_b, moon_c, moon_d)
    y = is_equal_by_axis("y", moon_a, moon_b, moon_c, moon_d)
    z = is_equal_by_axis("z", moon_a, moon_b, moon_c, moon_d)

    # x, y, z = 15, 25, 41

    steps = [x, y, z]

    # print(steps)

    lcm = steps[0]
    for i in steps[1:]:
        lcm = lcm * i//gcd(lcm, i)
    print(lcm)


def main():
    with open("2019/resources/txt/day12.txt") as txt:
        moons = txt.readlines()
        moons = [m.strip() for m in moons]

        for x in range(len(moons)):
            moons[x] = re.sub(r"[<>xyz=]", "", moons[x])
            moons[x] = moons[x].split(",")
            moons[x] = [int(m) for m in moons[x]]

        moon_a = Moon(moons[0][0], moons[0][1], moons[0][2])
        moon_b = Moon(moons[1][0], moons[1][1], moons[1][2])
        moon_c = Moon(moons[2][0], moons[2][1], moons[2][2])
        moon_d = Moon(moons[3][0], moons[3][1], moons[3][2])

        # part_a(moon_a, moon_b, moon_c, moon_d)
        part_b(moon_a, moon_b, moon_c, moon_d)


main()
