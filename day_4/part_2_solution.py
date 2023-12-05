
if __name__ == '__main__':
    total = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    # lines = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    # ]
    cards = [i+1 for i in range(len(lines))]
    all_cards = cards
    card_count = {}

    card_num_to_power = {}
    for line in lines:
        card, l = line.split(':')
        card_num = int(card.split('Card')[1].split()[0])
        card_count[card_num] = 1
        target_nums = l.split("|")[0].split()
        power = 0
        for x in l.split("|")[1].split():
            if x in target_nums:
                power += 1

        card_num_to_power[card_num] = power

    for k in card_num_to_power.keys():
        for y in range(card_count[k]):
            for x in range(k+1, k+1+card_num_to_power[k]):
                if x in card_num_to_power:
                    card_count[x] += 1

    for k in card_count.keys():
        total += card_count[k]

    print("TOTAL: ", total)


