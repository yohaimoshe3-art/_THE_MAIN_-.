grades = []
count = 0
while True:
    try:
        user_grade = int(input('enter your grade: '))
        if user_grade == -999:
            if count < 10:
                print("you must enter at least 10 valid grades before finishing")
                continue
            break
        if 0 <= user_grade <= 100:
            grades.append(user_grade)
            count += 1
        else:
            print("invalid grade, try again please")

    except ValueError :
        print('Invalid input, skip')

print(f'Class average: {sum(grades)/len(grades):.2f}')
print(f'Highest grade: {max(grades)}')
print(f"Number of valid grades: {len(grades)}")



