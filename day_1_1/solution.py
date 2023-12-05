
def process_line(l: str) -> int:
    front = 0
    back = len(l) - 1
    first, last = None, None
    while back >= front and (first is None or last is None):
        if first is None:
            if l[front].isdigit():
                first = l[front]
            else:
                front += 1
        if last is None:
            if l[back].isdigit():
                last = l[back]
            else:
                back -= 1
    return int((str(first) if first else "0") + (str(last) if last else "0"))


if __name__ == '__main__':
    total = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    for l in lines:
        number = process_line(l)
        total += number
        print(l, number)
    print("TOTAL: ", total)
