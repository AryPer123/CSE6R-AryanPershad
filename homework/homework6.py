# Final Letter Grade Calculator for CSE 8A/6R Fall 2025

def calculate_base_grade(homework_points, exam_points):
    """
    Determine base letter grade based on homework and exam points.
    
    Args:
        homework_points: Total homework points (max 18)
        exam_points: Total exam points (max 6)
    
    Returns:
        str: Base letter grade ('A', 'B', 'C', or 'F')
    
    Grading criteria:
    - A: At least 15 homework points AND 6 exam points
    - B: At least 12 homework points AND 4 exam points
    - C: At least 9 homework points AND 2 exam points
    - F: Does not meet requirements for C
    """
    base_grade = None
    if homework_points >= 15 and exam_points >= 6:
        base_grade = 'A'
    elif homework_points >= 12 and exam_points >= 4:
        base_grade = 'B'
    elif homework_points >= 9 and exam_points >= 2:
        base_grade = 'C'
    else:
        base_grade = 'F'
    return base_grade
    
def calculate_social_modifier(social_points):
    """
    Determine social learning modifier based on total social points.

    Args:
        social_points: Total social learning points (max 30)

    Returns:
        str: Modifier ('+', '', '-', or 'lower')

    Modifier criteria:
    - '+': At least 24 total social points
    - '': 18 to 23 total social points
    - '-': 12 to 17 total social points
    - 'lower': Fewer than 12 total social points
    """
    if social_points >= 24:
        return '+'
    elif 18 <= social_points <= 23:
        return ''
    elif 12 <= social_points <= 17:
        return '-'
    else:
        return 'lower'

def calculate_final_grade(homework_points, exam_points, social_points):
    """
    Calculate the final letter grade including social learning modifier.
    Args:
        homework_points: Total homework points (max 18)
        exam_points: Total exam points (max 6)
        social_points: Total social learning points (max 30)
    Returns:
        str: Final letter grade with modifier
    """
    base_grade = calculate_base_grade(homework_points, exam_points)
    social_modifier = calculate_social_modifier(social_points)

    if base_grade == 'F':
        final_grade = 'F'
    elif social_modifier == 'lower':
        if base_grade == 'A':
            final_grade = 'B'
        elif base_grade == 'B':
            final_grade = 'C'
        elif base_grade == 'C':
            final_grade = 'F'
    else:
        final_grade = base_grade + social_modifier

    return final_grade

# First three test cases for regression testing
print("Testing bug fix - original functionality:")

test_grade = calculate_final_grade(15, 6, 25)
print(f"Test 1 - A with 25 social points: {test_grade}")

test_grade = calculate_final_grade(12, 4, 20)
print(f"Test 2 - B with 20 social points: {test_grade}")

test_grade = calculate_final_grade(9, 2, 15)
print(f"Test 3 - C with 15 social points: {test_grade}")

test_grade = calculate_final_grade(15, 6, 10)
print(f"Test 4 - A with 10 social points: {test_grade}")

test_grade = calculate_final_grade(12, 4, 5)
print(f"Test 5 - B with 5 social points: {test_grade}")

test_grade = calculate_final_grade(9, 2, 8)
print(f"Test 6 - C with 8 social points: {test_grade}")

test_grade = calculate_final_grade(0, 0, 30)
print(f"Test 7 - F with 30 social points: {test_grade}")

# Prompt user for input for their total homework, exam, and social learning points
homework_points = int(input("\nEnter total homework points (max 18): "))
exam_points = int(input("Enter total exam points (max 6): "))
social_points = int(input("Enter total social learning points (max 30): "))

# Calculate and display the final letter grade
final_grade = calculate_final_grade(homework_points, exam_points, social_points)
print(f"Your final letter grade is: {final_grade}")