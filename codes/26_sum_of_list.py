"""Program 26: Sum of list elements without sum()."""


def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Sum:", sum_of_list(data))
