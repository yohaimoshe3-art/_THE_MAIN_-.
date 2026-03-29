def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    return sum(grades.values())/len(grades)

grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}
print(get_average_grade(grades))