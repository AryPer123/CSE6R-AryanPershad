# --- Lab Task Starting Code: CSE 8A-6R Grading System ---
# Goal: Refactor the repeated, complex logic below into a single function.

# --- Grading Thresholds (from our syllabus) ---
# A: HW >= 15 AND Exam >= 6
# B: HW >= 12 AND Exam >= 4
# C: HW >= 9 AND Exam >= 2
# F: Thresholds for C not met

grade = "None"
name = "Student"
hw_total = 0
exam_total = 0

def calculate_grade(hw_total, exam_total):
    if hw_total >= 15 and exam_total >= 6:
        grade = "A"
    elif hw_total >= 12 and exam_total >= 4:
        grade = "B"
    elif hw_total >= 9 and exam_total >= 2:
        grade = "C"
    else:
        grade = "F"
    return grade

def print_student_grade(name, hw_total, exam_total):
    grade = calculate_grade(hw_total, exam_total)
    print(f"{name}'s final grade is {grade}, based on a homework total of {hw_total} and exam total of {exam_total}")

print_student_grade("Aisha", 18, 6)
print_student_grade("Kenji", 14, 4)
print_student_grade("Priya", 10, 2)

