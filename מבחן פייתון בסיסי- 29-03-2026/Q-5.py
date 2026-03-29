from itertools import count


def most_common_word(stor : tuple[str, ...]) -> str:
    new_story = " ".join(stor)
    dict1 = {}

    for word in new_story.split():
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
    most_common = max(dict1, key=dict1.get)
    return most_common
'''
    # לא הצלחתי לסיים את השאלה ולהדפיס את כמות הפעמים שהמילה מופיעה

'''
    # list1 = list[dict1]
    # list1.count(most_common)
    # return most_common
    # list1.append(most_common)
    # count = list1.count(most_common)
    # return most_common

story = ("The little fox saw the little bird and the little cat.",
         "The fox was happy because the little bird sang, anf the little cat jumped." ,
         "The little fox, the little bird, and the little cat become friends.")

result = most_common_word(story)
print(result)














