def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char,0) + 1
    return char_counts

def get_sorted(in_dict):
    chars_list = []
    for k, v in in_dict.items():
        my_dict = {}
        my_dict["name"] = k
        my_dict["num"] = v
        chars_list.append(my_dict)
        chars_list.sort(reverse=True, key=lambda x: x["num"])
    return chars_list
