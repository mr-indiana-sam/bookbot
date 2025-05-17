"""
count_words takes in text, splits the text to words, and returns a count
"""
def count_words(text):
    words = text.split()
    return len(words)

"""
count_char takes the text from the book as a string, and returns the number of times each character, 
(including symbols and spaces), appears in the string.
"""
def count_char(text):
    char_counts = {}
    for char in text:
        char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
    return char_counts

def sort_on(dict):
    return dict("num")

"""
sorted_list takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
Sort the list from greatest to least by the count.
The .sort() method will be helpful here (see the hint).
"""
def sorted_list(char_dict):
    import operator
    
    dict_list = []

    for k,v in char_dict.items():
        dict_list.append({"char":k,"num":v})

    dict_list.sort(key=operator.itemgetter('num'), reverse=True)

    return dict_list