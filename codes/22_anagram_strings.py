"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    s1 = input("First string: ")
    s2 = input("Second string: ")
    print("Anagram:", is_anagram(s1, s2))
