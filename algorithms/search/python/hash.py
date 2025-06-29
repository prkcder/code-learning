

def hash_search(hash_list, item):
    if item in hash_list:
        return f"item {item} with the value: {hash_list[item]}"
    else:
        return None


data = {
    "apple": 5,
    "banana": 10,
    "cherry": 15,
    "grape": 0,  # Edge case: falsy value
    "melon": None  # Edge case: explicit None
}

print(data)
user_input = input("what do you want to find? enter: ").strip()

result = hash_search(data, user_input)
print(result)