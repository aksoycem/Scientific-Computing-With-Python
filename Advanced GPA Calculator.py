def get_user_grades(num_courses):
    grades = []
    for i in range(num_courses):
        while True:
            try:
                grade = float(input(f"Enter the grade for Course {i+1}: "))
                if 0 <= grade <= 4:
                    grades.append(grade)
                    break
                else:
                    print("Invalid input! Grade must be between 0 and 4.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    return grades

def calculate_weighted_gpa(grades, credit_hours):
    total_credit_hours = sum(credit_hours)
    weighted_gpa = sum(grade * credit for grade, credit in zip(grades, credit_hours))
    return weighted_gpa / total_credit_hours

if __name__ == "__main__":
    num_courses = int(input("Enter the number of courses: "))
    grades = get_user_grades(num_courses)

    credit_hours = []
    for i in range(num_courses):
        while True:
            try:
                credit_hour = int(input(f"Enter the credit hours for Course {i+1}: "))
                if credit_hour > 0:
                    credit_hours.append(credit_hour)
                    break
                else:
                    print("Invalid input! Credit hours must be greater than 0.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    semester_gpa = calculate_weighted_gpa(grades, credit_hours)
    print("Semester GPA:", semester_gpa)
