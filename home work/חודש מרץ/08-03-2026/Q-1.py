import random
from sys import exception


def get_lucky_numbers(amount: int) -> tuple[int]:
    '''
    returns tuple of random ints between 0-100 and amount
    :param amount:how many numbers you want
    :return:tuple of random ints
    '''
    return tuple(random.sample(range(1, 101), amount))

result = get_lucky_numbers(3)
print(result)

def input_until_lucky(lucky_numbers: tuple) -> int:
    '''
    input number from user until guessed the lucky number

    :param lucky_numbers: number to guess
    :return: how many attempts were made
    '''
    attempts = 0
    while True:
        try:
            user_answer = int(input("enter a number :"))
            attempts += 1

        except Exception as e:
            print("Invalid input, try again", e)
            continue

        if user_answer in lucky_numbers:
            break
    print("*" * 20)
    print("You guessed correctly!")
    print(f"Number of attempts: {attempts}")
    print(f"The correct number you guessed: {user_answer}")
    print(f"The lucky numbers were: {lucky_numbers}")

    return attempts

input_until_lucky(result)








