
def simple_search(search_list, thing_to_search):
    for index, element in enumerate(search_list):
        if element == thing_to_search:
            return f"found {element} at index {index}"
    return f"not found"



list = [12, 413, 555, 60, 30, 40, 300]

print(simple_search(list, 30))