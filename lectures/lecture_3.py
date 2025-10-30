is_revelle = "Maybe"

student_college = "Revelle"

def check_college(student_college):
    if student_college == "Revelle":
        is_revelle = "Yes"
        return is_revelle
    else:
        is_revelle = "No"


is_revelle = check_college(student_college)
print(is_revelle)