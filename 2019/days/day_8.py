def split_to_layers(barcode, w, t):
    num_to_split = w * t
    layers = []

    barcode_copy = barcode.copy()
    while(len(barcode_copy) > 0):
        layer = []
        slice = barcode_copy[0: num_to_split]

        for x in range(t):
            layer.append(slice[x * w: w + x * w])

        layers.append(layer)

        barcode_copy = barcode_copy[num_to_split:]

    return layers


def analyse_layers(layers):
    best_layer = {"amount": 9999, "layer": []}

    for x in layers:
        num_zeroes = 0
        for row in x:
            for digit in row:
                if digit == 0:
                    num_zeroes += 1

        if num_zeroes < best_layer["amount"]:
            best_layer["amount"] = num_zeroes
            best_layer["layer"] = x

    return best_layer["layer"]


def part_a(layers):

    best_layer = analyse_layers(layers)

    num_ones, num_twos = 0, 0
    for row in best_layer:
        for digit in row:
            if digit == 1:
                num_ones += 1
            elif digit == 2:
                num_twos += 1

    print(num_ones * num_twos)


def create_transparent_array(w, t):
    transparent_array = []
    for x in range(t):
        row = []
        for y in range(w):
            row.append(" ")
        transparent_array.append(row)

    return transparent_array


def part_b(layers, w, t):

    transparent_array = create_transparent_array(w, t)

    for layer in layers:
        for x in range(t):
            for y in range(w):
                if layer[x][y] != 2:
                    if transparent_array[x][y] == " ":
                        transparent_array[x][y] = layer[x][y]

    for row in transparent_array:
        out = ""
        for x in row:
            if x == 0:
                x = " "
            else:
                x = "*"
            out += " " + x + " "
        print(out)


def __main__():
    with open("2019/resources/txt/day8.txt") as txt:
        barcode = txt.read()
        barcode = list(barcode)
        barcode = [int(x) for x in barcode]

        layers = split_to_layers(barcode, 25, 6)
        # part_a(layers)
        part_b(layers, 25, 6)


__main__()
