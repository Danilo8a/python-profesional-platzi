# Eliminando repetidos de una lista

def remove_duplicate(some_list: list) -> list:
    return list(set(some_list))


if __name__ == "__main__":
    my_list = [1, 1, 3, 4, 4, 5, 7, 9]
    print(remove_duplicate(my_list))
