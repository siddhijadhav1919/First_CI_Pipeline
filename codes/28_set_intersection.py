"""Program 28: Intersection of two sets."""


def set_intersection(first, second):
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result


if __name__ == "__main__":
    a = set(input("First set (space separated): ").split())
    b = set(input("Second set (space separated): ").split())
    print("Intersection:", set_intersection(a, b))
