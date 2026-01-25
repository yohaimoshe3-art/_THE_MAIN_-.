# START
'''
קלוט מהמשתמש ציון (מספר שלם)

כללים:

אם הציון גדול מ־199 או קטן מ־0 – הדפס invalid
אחרת, אם הציון בין 80 ל־100 (כולל) – הדפס VERY GOOD
אחרת, אם הציון בין 60 ל־80 (כולל 60, לא כולל 80) – הדפס NOT BAD
אחרת, אם הציון בין 40 ל־60 (כולל 40, לא כולל 60) – הדפס BAD
אחרת, אם הציון בין 0 ל־40 (כולל) – הדפס REALLY BAD
'''

grade: int = int(input("Enter a grade"))
if grade > 199 and grade < 0:
    print("invalid")
elif grade >= 80 and grade <= 100:
    print("VERY GOOD")
elif grade >= 60 and grade <80:
    print("NOT BAD")
elif grade >=40 and grade <60:
    print("BAD")
elif grade >=0 and grade <= 40:
    print("REALLY BAD")
else:
    print("invalid grade")


