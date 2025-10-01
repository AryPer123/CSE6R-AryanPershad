name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to CSE 6R!")

user_college=input("Enter your UCSD college: ")

user_grad_yr = input("Enter your expected graduation year: ")
user_grad_yr = int(user_grad_yr)

years_till_grad = user_grad_yr - 2025
days_till_grad = years_till_grad * 365

print(f"Your college is {user_college} and you have {years_till_grad} until you graduate -- that's about {days_till_grad} days!")