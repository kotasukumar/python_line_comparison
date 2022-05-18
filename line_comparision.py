import math


def check(length1, length2):
    if length1 == length2:
        return "Both are equal"
    else:
        return "Both are not equal"


def line(x1, x2, y1, y2):
    length = math.sqrt(math.pow((x2 - x1), 2)) + math.sqrt(math.pow((y2 - y1), 2))
    return length


if __name__ == "__main__":
    l1 = line(5, 6, 15, 21)
    l2 = line(5, 6, 11, 19)
    result = check(l1, l2)
    print(result)
