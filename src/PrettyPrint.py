class PrettyPrint:

    def print_students(students):
        print("Сведения об успеваемости студентов:")
        print()
        for student, subjects in students.items():
            print(student)
            for subj, score in subjects:
                print(subj, ':', score)
            print()

    def print_rating(rating):
        print("Рейтинг студентов:")
        print()
        for student, rating_value in rating.items():
            print(student, ':', "%.2f" % rating_value)
        print()
