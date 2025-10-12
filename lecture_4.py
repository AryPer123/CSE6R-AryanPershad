def find_generation_v1(birth_year):
    generation = None
    if birth_year < 1946:
        generation = "Silent Generation"
    elif birth_year < 1965:
        generation = "Baby Boomer"
    elif birth_year < 1981:
        generation = "Generation X"
    elif birth_year < 1997:
        generation = "Millennial"
    elif birth_year < 2013:
        generation = "Generation Z"
    elif birth_year < 2030:
        generation = "Generation Alpha"
    else:
        generation = "Future Generation"
    return generation


print(find_generation_v1(2010))

def find_generation_v2(birth_year):
    generation = None
    if birth_year < 1946:
        generation = "Silent Generation"
    if birth_year < 1965:
        generation = "Baby Boomer"
    if birth_year < 1981:
        generation = "Generation X"
    if birth_year < 1997:
        generation = "Millennial"
    if birth_year < 2013:
        generation = "Generation Z"
    if birth_year < 2030:
        generation = "Generation Alpha"
    else:
        generation = "Future Generation"
    return generation


print(find_generation_v2(1955))