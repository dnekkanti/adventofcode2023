import re

if __name__ == '__main__':
    total = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    # lines = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:+=-]')
    matrix = []
    for line in lines:
        l = list(line)
        matrix.append(l)
    # row = index within list
    # col = lst number
    row_max = len(matrix)
    gear_coordinate_to_adjacent_nums = {}
    for row in range(row_max):
        col = 0
        col_max = len(matrix[row])
        while col < col_max:
            # check all 4 directions if this is a digit, and all 4 diagonal directions
            hit = False
            coordinate = None
            if matrix[row][col].isdigit():
                if not hit and row - 1 >= 0:
                    if regex.search(matrix[row-1][col]):
                        hit = True
                        coordinate = ((row-1), col)
                if not hit and row + 1 < row_max:
                    if regex.search(matrix[row+1][col]):
                        hit = True
                        coordinate = ((row + 1), col)
                if not hit and col - 1 >= 0:
                    if regex.search(matrix[row][col-1]):
                        hit = True
                        coordinate = (row, col-1)
                if not hit and col + 1 < col_max:
                    if regex.search(matrix[row][col+1]):
                        hit = True
                        coordinate = (row, col+1)
                if not hit and row + 1 < row_max and col + 1 < col_max:
                    if regex.search(matrix[row + 1][col+1]):
                        hit = True
                        coordinate = ((row + 1), (col + 1))
                if not hit and row - 1 >= 0 and col - 1 >= 0:
                    if regex.search(matrix[row-1][col-1]):
                        hit = True
                        coordinate = ((row - 1), (col - 1))
                if not hit and row + 1 < row_max and col - 1 >=0:
                    if regex.search(matrix[row + 1][col-1]):
                        hit = True
                        coordinate = ((row + 1), (col - 1))
                if not hit and row - 1 >= 0 and col + 1 < col_max:
                    if regex.search(matrix[row-1][col+1]):
                        hit = True
                        coordinate = ((row - 1), (col + 1))
                if hit:
                    # get the entire length number
                    hit_index = col
                    start = hit_index
                    end = hit_index

                    asc_index = hit_index + 1
                    while asc_index < col_max:
                        if matrix[row][asc_index].isdigit():
                            end = asc_index
                            asc_index += 1
                        else:
                            break
                    desc_index = hit_index - 1
                    while desc_index >= 0:
                        if matrix[row][desc_index].isdigit():
                            start = desc_index
                            desc_index -= 1
                        else:
                            break
                    full_num = int(''.join(matrix[row][start:end + 1]))
                    if str(coordinate) in gear_coordinate_to_adjacent_nums:
                        nums = gear_coordinate_to_adjacent_nums[str(coordinate)]
                        nums.append(full_num)
                        gear_coordinate_to_adjacent_nums[str(coordinate)] = nums
                    else:
                        gear_coordinate_to_adjacent_nums[str(coordinate)] = [full_num]
                    col = end + 1
                else:
                    col += 1
            else:
                col += 1

    print(gear_coordinate_to_adjacent_nums)
    for k in gear_coordinate_to_adjacent_nums.keys():
        if len(gear_coordinate_to_adjacent_nums[k]) == 2:
            subtotal = gear_coordinate_to_adjacent_nums[k][0] * gear_coordinate_to_adjacent_nums[k][1]
            total += subtotal
    print("TOTAL: ", total)

