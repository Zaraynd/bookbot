def get_num_words (text):
    words = text.split()
    return len(words)

def get_num_char (text):
    char_list = list(text)
    char_count = {}
    for char in char_list:
        lower_char = char.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 1
        else:
            char_count[lower_char] += 1
    return char_count

def sort_char_list (char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_dict = {"char" : char, "num" : char_count[char]}
            char_list.append(char_dict)

    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list

