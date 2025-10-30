def social_learning_grade(readings, lectures, labs, study_groups):
    social_points = 0
    social_grade = 0
    
    social_points = readings + lectures + labs + study_groups

    if social_points >= 4 and labs == 1 and readings == 1:
        social_grade = 3
    
    elif social_points > 3 and labs == 1 or (social_points >= 3 and readings == 1):
        social_grade = 2

    elif social_points >= 2:
        social_grade = 1
    
    else:
        social_grade = 0

    return social_grade


#Expected: Exemplary
print(social_learning_grade(1, 2, 1, 1))
print(social_learning_grade(1, 1, 1, 1))

#Expected: Satisfactory
print(social_learning_grade(1, 2, 0, 1))
print(social_learning_grade(0, 2, 1, 1))

#Expected: Needs Improvement
print(social_learning_grade(0, 2, 0, 0))
print(social_learning_grade(1, 0, 0, 1))

#Expected: Incomplete
print(social_learning_grade(0, 0, 0, 0))
print(social_learning_grade(1, 0, 0, 0))