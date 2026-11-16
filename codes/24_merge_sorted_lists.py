"""Program 24: Merge two sorted lists into one sorted list."""


def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


if __name__ == "__main__":
    a = [int(x) for x in input("First sorted list: ").split()]
    b = [int(x) for x in input("Second sorted list: ").split()]
    print("Merged:", merge_sorted_lists(a, b))
