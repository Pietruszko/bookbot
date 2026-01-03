def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    chars_dict = {}
    for char in text.lower():
        if chars_dict.get(char) is not None:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def sort_dict(dict_to_sort: dict) -> list:
    sorted_list = []
    for key, value in dict_to_sort.items():
        if key.isalpha():
            sorted_list.append({"char": key, "num": value})
    sorted_list.sort(key=helper_func, reverse=True)
    return sorted_list


def helper_func(dict_num: dict) -> int:
    return dict_num["num"]
