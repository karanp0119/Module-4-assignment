import math


def main():
    a = 1
    b = -5.86
    c = 8.5408
    pos_root = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    neg_root = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print("Positive root is", str(pos_root), "and the negative root is", str(neg_root))

    for i in range(2,11):
        print(1/i)


if __name__ == "__main__":
    main()
