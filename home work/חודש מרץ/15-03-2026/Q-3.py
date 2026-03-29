
def group_numbers(nums: list) -> dict:
    '''

    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    dict1 = {'positive': [], 'negative': [], 'zero': []}
    for num in nums:
        if num > 0 and num not in dict1:
            dict1['positive'].append(num)
        elif num < 0 and num not in dict1:
            dict1['negative'].append(num)
        else:
            dict1['zero'].append(num)
    return dict1

list1 = [4, -2, 0, 7, -5, 3]

print(group_numbers(list1))