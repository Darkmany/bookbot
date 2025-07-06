def word_count(text):
    split = text.split()
    return len(split)

def char_count(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(item):
    return item["num"]

def sort_chars(char_dict):
    sorted = []
    for char, count in char_dict.items():
        sorted.append({"char": char, "num": count})
    sorted.sort(reverse=True, key=sort_on)
    return(sorted)