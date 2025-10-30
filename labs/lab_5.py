def count_candy(candies):
    total_candies = {}
    for candy in candies:
        if candy in total_candies:
            total_candies[candy] += 1
        else:
            total_candies[candy] = 1
    return total_candies

def most_candies(candies):
    total_candies = count_candy(candies)
    max_candy = None
    max_count = 0
    for candy, count in total_candies.items():
        if count > max_count:
            max_candy = candy
            max_count = count
    print(f"Most amount of candies is {max_candy} with a count of {max_count}")
    return max_candy, max_count
    
    # most_candy = max(total_candies, key = total_candies.get)
    # return (most_candy, total_candies[most_candy])

# print(count_candy(["Kit Kat", "M&Ms", "M&Ms", "DOTS", "Almond Joy"]))
print(most_candies(["Kit Kat", "Kit Kat", "M&Ms", "M&Ms", "DOTS", "Almond Joy"]))

# print(count_candy(["M&Ms", "M&Ms", "M&Ms"]))

# print(count_candy([]))
