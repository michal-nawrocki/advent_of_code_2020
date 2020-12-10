input_data = [
    70,
    102,
    148,
    9,
    99,
    63,
    40,
    52,
    91,
    39,
    55,
    28,
    54,
    22,
    95,
    61,
    118,
    35,
    14,
    21,
    129,
    82,
    137,
    45,
    7,
    87,
    81,
    25,
    3,
    108,
    41,
    11,
    145,
    18,
    65,
    80,
    115,
    29,
    136,
    42,
    97,
    104,
    117,
    141,
    62,
    121,
    23,
    96,
    24,
    128,
    48,
    1,
    112,
    8,
    34,
    144,
    134,
    116,
    58,
    147,
    51,
    84,
    17,
    126,
    64,
    68,
    135,
    10,
    77,
    105,
    127,
    73,
    111,
    90,
    16,
    103,
    109,
    98,
    146,
    123,
    130,
    69,
    133,
    110,
    30,
    122,
    15,
    74,
    33,
    38,
    83,
    92,
    2,
    53,
    140,
    4,
]

small = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

def handle_input():
    """
        Store the data in a dictionary, so we have O(1) access
        whenever we are looking for the next 3 adapters.
        Sorting the array would limit space complexity but meh.
    """
    handled_data = dict()

    for number in small:
        handled_data[number] = True
    
    return handled_data

def recursive_traverse(start_jolts, all_paths, current_path, data):
    next_jolts = []

    # TODO: Implement this
    # if start_jolts == 0:

    # if data.get(start_jolts - 1, False):
    #     next_jolts.append(start_jolts - 1)
    
    # if data.get(start_jolts - 2, False):
    #     next_jolts.append(start_jolts - 2)

    # if data.get(start_jolts - 3, False):
    #     next_jolts.append(start_jolts - 3)



def part_one():
    data = handle_input()
    current_jolts = 0
    jolt_1_differences = 0
    jolt_3_differences = 1

    while True:
        if data.get(current_jolts+1, False):
            jolt_1_differences += 1
            current_jolts = current_jolts+1
            continue
        elif data.get(current_jolts+2, False):
            current_jolts = current_jolts+2
            continue
        elif data.get(current_jolts+3, False):
            jolt_3_differences += 1
            current_jolts = current_jolts+3
        else:
            break

    print(jolt_1_differences * jolt_3_differences)
    print(max(data))

def part_two():
    all_paths = set()
    data = handle_input()

    recursive_traverse(max(data), all_paths, [max(data)], data)
    print("2 done")
        
if __name__ == "__main__":
    print("Part one:")
    part_one()
    print("")

    print("Part two:")
    part_two()
    print("")

    print("Done")
