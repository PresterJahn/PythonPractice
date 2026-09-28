# defined weights
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# all scored inputed by user
midterm_exam_grade = float(input("Please enter midterm grade 0 - 100: "))
final_exam_grade = float(input("Please enter final exam grade 0 - 100: "))
assignment_one = float(input("Please enter first assignment grade 0 - 30: "))
assignment_two = float(input("Please enter second assignment grade 0 - 30: "))
quiz_one = float(input("Please enter first quiz grade 0 - 20: "))
quiz_two = float(input("Please enter second quiz grade 0 - 20: "))

# checks the exam grades
if midterm_exam_grade >= 0 and midterm_exam_grade <= 100 and final_exam_grade >= 0 and final_exam_grade <= 100:
    exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT
else:
    exam_grade = 0
    print("Invalid input. Please enter exams within the 0 - 100 range.")

# checks the assignment grades
if assignment_one >= 0 and assignment_one <= 30 and assignment_two >= 0 and assignment_two <= 30:
    assignment_grade = (assignment_one + assignment_two) / 60 * 100 * ASSIGNMENT_WEIGHT
else:
    assignment_grade = 0
    print("Invalid input. Please enter assignments within the 0 - 30 range.")

# checks the quiz grades
if quiz_one >= 0 and quiz_one <= 20 and quiz_two >= 0 and quiz_two <= 20:
    quiz_grade = (quiz_one + quiz_two) / 40 * 100 * QUIZ_WEIGHT
else:
    quiz_grade = 0
    print("Invalid input. Please enter quizzes within the 0 - 20 range.")

# calculates the final grade
final_grade = exam_grade + assignment_grade + quiz_grade

# prints the final grade
print(f"The students final grade is {final_grade:.2f}%")