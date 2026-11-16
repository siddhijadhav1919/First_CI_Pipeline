"""Program 27: Rotate a list to the right by k positions."""


def rotate_list(items, k):
    if len(items) == 0:
        return []
    k = k % len(items)  # handles k > length and negative k (left rotation)
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]


if __name__ == "__main__":
    data = [int(x) for x in input("Enter list: ").split()]
    k = int(input("Rotate by k: "))
    print("Rotated:", rotate_list(data, k))
