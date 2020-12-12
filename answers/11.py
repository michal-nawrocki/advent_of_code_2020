# Note the added border using '@' so that the conditions checking for adjecten tiles is simplified
data = [
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
    "@LLLLLL.LLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL..L.LLLLLL@",
    "@LLLLLLLLLL..LLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLL.LL.LLLLLLLL.LLLLLLLL.L.LLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLL.LLLLLLL.L.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.L.LLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL.LLLLLLLL@",
    "@.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.L.LLLLLLLL.LLLL.LLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.L.LL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL..LLLLLLLLLLLLL.LLL.LLLL@",
    "@..LL....L.LL........L...L......LL..L.L........L....L..........L..L.........LLLL..L.L.L..LL...LL....@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LL.LL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL..LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLL.LL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LL.LLLLL.LLLLLLLL@",
    "@L.L.........L..L..L.L....LLLL...LL..L....L.L..L..L.L.L.L........LL.L...........L........L..LLL...LL@",
    "@LLLLLLLLLL.LLLLLLLLLLL.LL.LLLLLLLLL.LLLLLL.LLLL..LLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.L@",
    "@LLLLLLLLLL.LLL..LLLLLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.L.LLLLL..L.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLL.LL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLL.L.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL..LLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL..LLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLL.L.@",
    "@LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LL.LLL.LLLLLL.LLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.L..LLLL.LLL.LLLLLL..LLLLLLLL.LLLLL..LLLLLL.@",
    "@LLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLLL.LLLLLLLLLLLLL..LLLLLLL.L.LLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL..LLLLLLLL.LLLLLLLLLLLLLLLL.L.LL.LLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLL..LLLLLL.L.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@LL...L.LL....L.LL.L.....L.LL......L.......L...........L.L..L.LL....LL..LLL.L.LL...........L...LLLL.@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.L..LLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLL.L@",
    "@LLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LL..LLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@...LL.LL.L....L....LLL..LL..L.....................L....LL..L...LL..L........LL.....L...........L..L@",
    "@LLLLLLLLLL.LLLL..LLL.LLLL.LLLLLLLLL.LLLLLL..LLLLL.LLLLLLLL.LLLLLLLLLLLLLLL...LLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLLLLL.L.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLL.LLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLL.LL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLL.LLL..LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LL.LLL.LLL.LLLLLLLLLLL.LLLLLLLL.L.LLLLL.LLLLLLLL..LLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@.......LL.L.LL.....LL.L...L.L..LL..L...L..L.......LLLL....LL..LL.L...L...L...L..L.L.LL..L...L....L.@",
    "@L.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LL..LLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLL.LLLL..LLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL..LLLLLLLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLL.L.LLLLLLLLLLLL.L.LLLLLLLL@",
    "@L..LLL..L........L.LL......L........LL.....L.L..LL...L......L...LL......L.L.....LL..L......L...L.LL@",
    "@LL.LLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL..LLL..LLLLLLLL@",
    "@LLLLLLLLLLLLLL..LLLL.LLLLLLLLLL.LLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL@",
    "@.L...L...L..LLLLLLL.L.L..............L.LL..L.L..LLL...L......LL.L...LL.L.L.L..L....L..LLL..LL.L....@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLL.LLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.L.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLL.LLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL..LLLLLLLLLLL..LL.LLLLLLL..LLLLLLL.LLLLLL.L.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LL.L.LLLLLLLLLLL.LLLLLLL.LLLLLL.LL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL..LLLLLLL.LLLLLLL.LLLLLLLLLLLL.L.L.LLLLLL@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL..LLLLLLLLLLLL.LL.LLLLLL.LLLLLLLL.LLLLLLLL.LL..LLL.LLLLLLLL.LLLLLLLLLLLLL.@",
    "@....L.L..L......L.LL..L.L.LLL.L...L....LL.L..LL....LL.LL...LLL........L.LL..L...L..LL.LL..L...L...L@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLL.L@",
    "@L.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLL.LL.LLL.L.LLLLLLL.LLLLLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.L.LLLLLLLLL.LLLLLLLLLL.LLLLLL.L@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLL.LLL.LLLLLL.LLLLLLLLLLLL.LL.LL.LLLLL.LLLLLLL..LLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLL.L.L.L..L...L...LL.L........LL..L..L.....L..L.LLL..L.L.L.L.LL..LLLL.L............L..........L...@",
    "@LLLLLL.LLL.LLLL.L.LLLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.L..LLLL.L.LLLLLL@",
    "@LLLLLLLLLL.L.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.L..LLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLL.L@",
    "@LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.@",
    "@LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.L@",
    "@L.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLL.LLLLLLL@",
    "@LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLL.LLL.LLL.LLLL.LLLLLL..LLLLLLLLLLLLLL.LLLLLLLL@",
    "@.....L..LLLL..LL....LLLL.LL..L..L...L.L...LL.L...L.........L.L..........L...L....L.L.LL.LL..LL.LL.L@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLL.LLL@",
    "@LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL@",
    "@LLLLLLLLLL.LLLL.LLL.LL.LLLLLLLLLLLLLLL.LLL..LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL@",
    "@.L.LL........L...LL.LLL...............LL....L...L....LL.LLL...............L....L...L...L....L...L..@",
    "@LLLLLLLLLLLLLLL.LLL.LLLLL.L.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLL.LL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLL.LLLLLLLLLLLLL..LLLLLLLL@",
    "@LLLLLLL.L..LLLL.LLLLLLLLL..LLLLL.LL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLL.L.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL..LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLL..LL.L.L..LL.LL....LL..LL.LLL...L..LL...L..L....L......L.L..LLL.L....LLLL.LL....LL.LL.....L.L@",
    "@LLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL@",
    "@LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLL.LLLLLL..LLLLLLLL.LLLLL.LLLLLLLL@",
    "@LLLLLLLLLL.LLLL.LLL.LLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LL.LLLLL.LLLLLLLLLL.LLLLLLLLL.L.LLLLLLLL@",
    "@.LLLLL.LLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL@",
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
]

def count_occupied_seats(seat_map):
    occupied_seats = 0

    for row in seat_map:
        for char in row:
            if char == "#":
                occupied_seats += 1
    
    return occupied_seats

def count_occupied_adjacent_seats(seat_map, row_index, char_index):
    adjacent_seats = 0

    top_row = row_index - 1
    bot_row = row_index + 1
    col_index = char_index - 1

    # Check top and bot row relative to seat
    for offset in range(0, 3):
        if seat_map[top_row][col_index + offset] == "#":
            adjacent_seats += 1

        if seat_map[bot_row][col_index + offset] == "#":
            adjacent_seats += 1
    
    # Check seat to left
    if seat_map[row_index][char_index - 1] == "#":
        adjacent_seats += 1

    # Check seat to right
    if seat_map[row_index][char_index + 1] == "#":
        adjacent_seats += 1

    return adjacent_seats

def count_occupied_adjacent_seats_extended(seat_map, row_index, char_index):
    adjacent_seats = 0
    
    # Check seats above
    for index in range(row_index - 1, 0, -1):
        char = seat_map[index][char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break

    
    # Check seats below
    for index in range(row_index + 1, len(seat_map)):
        char = seat_map[index][char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break

    # Check seats to left
    for index in range(char_index - 1, 0, -1):
        char = seat_map[row_index][index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break

    # Check seats to right
    for index in range(char_index + 1, len(seat_map[0])):
        char = seat_map[row_index][index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break
    
    # Check Upper-Left diagonal
    UL_row_index = row_index - 1
    UL_char_index = char_index - 1

    while UL_row_index > 0 and UL_char_index > 0:
        char = seat_map[UL_row_index][UL_char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break
        else:
            UL_row_index -= 1
            UL_char_index -= 1
    
    # Check Upper-Right diagonal
    UR_row_index = row_index - 1
    UR_char_index = char_index + 1

    while UR_row_index > 0 and UR_char_index < len(seat_map[0]):
        char = seat_map[UR_row_index][UR_char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break
        else:
            UR_row_index -= 1
            UR_char_index += 1
    
    # Check Lower-Left diagonal
    LL_row_index = row_index + 1
    LL_char_index = char_index - 1
    
    while LL_row_index < len(seat_map) and LL_char_index > 0:
        char = seat_map[LL_row_index][LL_char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break
        else:
            LL_row_index += 1
            LL_char_index -= 1

    # Check Lower-Right diagonal
    LR_row_index = row_index + 1
    LR_char_index = char_index + 1
    
    while LR_row_index < len(seat_map) and LR_char_index < len(seat_map[0]):
        char = seat_map[LR_row_index][LR_char_index]
        if char == "#":
            adjacent_seats += 1
            break
        elif char == "L":
            break
        else:
            LR_row_index += 1
            LR_char_index += 1

    return adjacent_seats

def progress_seat_map(seat_map):
    """Return a copy of seat_map with updated seat positions"""
    copied_map = []
    copied_map.append(seat_map[0])

    for row_index in range(1, len(seat_map)):
        copied_row = []

        # Each line has the same length
        for char_index in range(0, len(seat_map[0])):
            character = seat_map[row_index][char_index]

            if character == "L":
                if count_occupied_adjacent_seats(seat_map, row_index, char_index) == 0:
                    copied_row.append("#")
                else:
                    copied_row.append(character)
            elif character == "#":
                if count_occupied_adjacent_seats(seat_map, row_index, char_index) >= 4:
                    copied_row.append("L")
                else:
                    copied_row.append(character)
            else:
                copied_row.append(character)

        copied_map.append("".join(copied_row))

    return copied_map

def progress_seat_map_extended(seat_map):
    """Return a copy of seat_map with updated seat positions"""
    copied_map = []
    copied_map.append(seat_map[0])

    for row_index in range(1, len(seat_map)):
        copied_row = []

        # Each line has the same length
        for char_index in range(0, len(seat_map[0])):
            character = seat_map[row_index][char_index]

            if character == "L":
                if count_occupied_adjacent_seats_extended(seat_map, row_index, char_index) == 0:
                    copied_row.append("#")
                else:
                    copied_row.append(character)
            elif character == "#":
                if count_occupied_adjacent_seats_extended(seat_map, row_index, char_index) >= 5:
                    copied_row.append("L")
                else:
                    copied_row.append(character)
            else:
                copied_row.append(character)

        copied_map.append("".join(copied_row))

    return copied_map

def part_one():
    seat_map = data
    next_map = progress_seat_map(seat_map)

    while seat_map != next_map:
        seat_map = next_map
        next_map = progress_seat_map(seat_map)

    occupied_seats = count_occupied_seats(seat_map)
    print(occupied_seats)

def part_two():
    seat_map = data
    next_map = progress_seat_map_extended(seat_map)

    while seat_map != next_map:
        seat_map = next_map
        next_map = progress_seat_map_extended(seat_map)

    occupied_seats = count_occupied_seats(next_map)
    print(occupied_seats)
        
if __name__ == "__main__":
    print("Part one:")
    part_one()
    print("")

    print("Part two:")
    part_two()
    print("")

    print("Done")
