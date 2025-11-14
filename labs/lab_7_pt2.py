def weekly_income_by_store(weekly_income):
    result = []
    for store in weekly_income:
        total = 0
        for day_income in store:
            if day_income >= 0:
                total += day_income
        result.append(total)
    return result

def best_day_by_store(weekly_income):
    result = []
    for store in weekly_income:
        max_income = None
        for day_income in store:
            if day_income >= 0:
                if max_income is None or day_income > max_income:
                    max_income = day_income
        result.append(max_income)
    return result