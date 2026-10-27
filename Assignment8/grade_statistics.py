
from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.
    """
    final_grades = []

    try:
        with open(GRADES_FILE, "r") as file:
            lines = file.readlines()

            for line in lines[1:]:
                row = line.strip().split(",")
                grade = process_row(row)
                final_grades.append(grade)

        analyze_grade(final_grades)

    except FileNotFoundError:
        print("Error: grades.csv file not found.")
    except (ValueError, IndexError, ZeroDivisionError) as error:
        print(f"Error processing grades: {error}")


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns).
    """
    tests = row[2:6]
    exams = row[6:8]
    discussions = row[8:10]
    project = float(row[10])

    test_avg = average_subject(tests)
    exam_avg = average_subject(exams)
    discussion_avg = average_subject(discussions)

    return weight_final(test_avg, exam_avg, discussion_avg, project)


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    total = 0

    for score in subject_list:
        total += float(score)

    return total / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above.
    """
    final_grade = (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )

    return final_grade


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60.
    """
    grade_counts = [0, 0, 0, 0, 0]

    for grade in weight_final_list:
        if grade >= 90:
            grade_counts[0] += 1
        elif grade >= 80:
            grade_counts[1] += 1
        elif grade >= 70:
            grade_counts[2] += 1
        elif grade >= 60:
            grade_counts[3] += 1
        else:
            grade_counts[4] += 1

    labels = ["90 or above", "80-89", "70-79", "60-69", "below 60"]

    for i in range(5):
        print(f"Number of students with final grade {labels[i]}: {grade_counts[i]}")


if __name__ == "__main__":
    main()
