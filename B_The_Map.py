file = open("input.txt", "r")
map = [line.strip() for line in file.readlines()]
file.close()

map_width = len(map[0])
map_height = len(map)

vac_count = 0
for i in range(len(map)):
    vac_count += map[i].count("o")

def get_variants(map, start_point):
    width = map_width - start_point[0]
    height = map_height - start_point[1]
    successful_squares = []
    for side in multipliers.keys():
        if side <= width and multipliers[side] <= height:
            vac_count = 0
            current_square = []
            for i in range(multipliers[side]):
                current_square_str = map[i + start_point[1]][start_point[0]:start_point[0] + side]
                vac_count += current_square_str.count("o")
                current_square.append(current_square_str)
            if vac_count == 1:
                successful_squares.append(current_square)
            for square in successful_squares:
                for square_str in square:
                    if "x" in square_str:
                        successful_squares.remove(square)
    return successful_squares

def get_actual_tempmap(tempmap, start_point, square):
    for row in range(len(square)):
        tempmap[row + start_point[1]] = list(tempmap[row + start_point[1]])
        for i in range(len(square[row])):
            tempmap[row + start_point[1]][i + start_point[0]] = "x"
        tempmap[row + start_point[1]] = ''.join(tempmap[row + start_point[1]])
    return tempmap

def get_next_sp(tempmap):
    for row in range(len(tempmap)):
        for i in range(len(tempmap[row])):
            if tempmap[row][i] != 'x':
                start_point = [i, row]
                return start_point

if map_width <= 100 and map_height <= 100 and vac_count >= 1 and map_width * map_height % vac_count == 0:
    square_part = int(map_width * map_height / vac_count)
    multipliers = {}
    for i in range(1, square_part + 1):
        if square_part % i == 0:
            multipliers[int(square_part / i)] = i
    start_point = [0, 0]
    successful_squares = get_variants(map, start_point)
    if successful_squares != []:
        solution = []
        map_inwork = map.copy()
        for i in range(1, vac_count):
            for square in successful_squares:
                successful_squares_backup = successful_squares.copy()
                map_backup = map_inwork.copy()
                map_inwork = get_actual_tempmap(map_inwork, start_point, square)
                backup_sp = start_point.copy()
                start_point = get_next_sp(map_inwork)
                successful_squares = get_variants(map_inwork, start_point)
                if successful_squares == []:
                    map_inwork = map_backup.copy()
                    start_point = backup_sp.copy()
                    successful_squares = successful_squares_backup.copy()
                else:
                    solution.append(square)
                    break
        solution.append(successful_squares[0])

        if len(solution) == vac_count:
            for square in solution:
                for row in square:
                    print(row)
                print()