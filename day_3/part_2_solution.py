
if __name__ == '__main__':
    total = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    # lines = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    # ]

    for line in lines:
        game_id = (line.split(':')[0]).split()[1]
        iterations = (line.split(':')[1]).split(';')
        power = 1
        color_maxes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for i in iterations:
            colors = i.split(',')
            for color in colors:
                amt, col = color.split()
                if color_maxes[col] < int(amt):
                    color_maxes[col] = int(amt)
        for k in color_maxes.keys():
            power *= color_maxes[k]
        total += power

    print("TOTAL: ", total)

