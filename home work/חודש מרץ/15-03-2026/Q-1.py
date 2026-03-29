def group_words_by_length(word: list) -> dict:
    dict1 = {}
    for word in word:
        if not(len(word) in dict1):
            dict1[len(word)] = [word]
        else:
            dict1[len(word)].append(word)
    return dict1

list1 = ["apple","banana","kiwi","grape","melon","pear"]

print(group_words_by_length(list1))