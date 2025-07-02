
def binary_search(search_list, thing_to_search):
    low = 0
    high = len(search_list) - 1

    search_list.sort()

    while low < high:
        mid = int((low + high) / 2)

        guess = search_list[mid]
        print(guess)
        if guess == thing_to_search:
            return f"found the mid on index {mid}"
        if guess > thing_to_search:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9, 12, 413, 555, 60, 30, 40, 300]

print(binary_search(my_list, 30))