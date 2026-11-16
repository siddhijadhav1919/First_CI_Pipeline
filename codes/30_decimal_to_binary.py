"""Program 30: Convert decimal to binary without bin()."""


def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not supported")
    if number == 0:
        return "0"
    bits = ""
    while number > 0:
        bits = str(number % 2) + bits
        number //= 2
    return bits


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Binary:", decimal_to_binary(n))
