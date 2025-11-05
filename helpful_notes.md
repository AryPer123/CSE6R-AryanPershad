From line #13 in lecture_3.py: In order for the value of a variable to actually update and be able to be printed globally, we need to run it like var = func(param) not just func(param)

When making a for loop, we can assign anything as the "loop variable". Then if we want to print / return it, we need to print the loop variable inside the loop, NOT the name of the list itself i.e. print(num) not print (nums)

When writing a function with multiplication involved, remember to start at 1 and not 0.

When defining variables inside a function, make sure not to define variables that are already being passed in as arguments that will get overridden.

In a dictionary, whatever is on the left side of the = in the [] will be the key, and then whatever is on the right side of the = will be the value.

Three ways to access a dictionary: dict.keys, dict.values, dict.items -- first two are self-explanatory, and dict.items accesses both