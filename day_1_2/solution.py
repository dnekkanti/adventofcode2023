from typing import Optional, Tuple

numbers_as_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def check_and_replace_front(l: str) -> Optional[str]:
    for k in numbers_as_words.keys():
        if l[0: len(k)] == k:
            return numbers_as_words[k]


def check_and_replace_back(l: str) -> Optional[str]:
    for k in numbers_as_words.keys():
        if l[-len(k):] == k:
            return numbers_as_words[k]


def convert_line_to_number_str(l: str) -> Tuple[str, str]:
    front_to_back_counter = 0
    back_to_front_counter = len(l) - 1
    last = len(l)
    front_to_back = l
    back_to_front = l

    first_number_in_word = None
    last_number_in_word = None

    # Start front to back, figure out the first numerical digit or word that represents a digit
    while front_to_back_counter < last and first_number_in_word is None:
        if front_to_back[front_to_back_counter].isdigit():
            first_number_in_word = front_to_back[front_to_back_counter]
            front_to_back_counter = last
        else:
            first_number_in_word = check_and_replace_front(front_to_back[front_to_back_counter:])
            front_to_back_counter += 1

    while back_to_front_counter > -1 and last_number_in_word is None:
        if back_to_front[back_to_front_counter].isdigit():
            last_number_in_word = back_to_front[back_to_front_counter]
            back_to_front_counter = -1
        else:
            last_number_in_word = check_and_replace_back(back_to_front[0:back_to_front_counter+1])
            back_to_front_counter -= 1

    return first_number_in_word if first_number_in_word else "0", last_number_in_word if last_number_in_word else "0"


if __name__ == '__main__':
    total = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        front, back = convert_line_to_number_str(line)
        number = int(str(front) + str(back))
        total += number
        print(line, front, back, number)
    print("TOTAL: ", total)

