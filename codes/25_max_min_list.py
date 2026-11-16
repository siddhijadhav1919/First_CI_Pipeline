"""Program 25: Find maximum and minimum without max() / min()."""


def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    maximum = minimum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return (maximum, minimum)


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Max, Min:", find_max_min(data))
