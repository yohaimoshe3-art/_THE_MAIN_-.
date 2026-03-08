words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

#Question 1
print(all(word.isupper() for word in words))

#Question 2
print(any( len(word) > 5 for word in words))

