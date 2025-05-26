# Lab 0: Python Naming Conventions and Boolean Expressions

## Instructions

Complete the following assignments in the provided `main.py` file. For each problem, write your answers within the triple quotes ("""...""") provided under each problem's comment.
For full credit make sure to include the phrase you are examining in your solution.

## Problem 1: Variable Names

Evaluate the following variable names. For each, explain why it is valid or invalid as a Python variable name:

1. `first_name` this is valid because it is a function name
2. `2nd_name` not valid because it uses a numeric number at begining, function must start with letter or underscore
3. `age` valid follows a string 
4. `total_amount`valid, same as one, seperates words with underscore
5. `while` invalid it is a reserved python word
6. `Student`valid, just because it has a capital it is still a function name
7. `my-variable`not valid you cant use "-"
8. `for`invalid, reserved python word
9. `_temp` valid, can start with underscore
10. `value#` not valid cant use a # , not a character

## Problem 2: Function Names

Evaluate the following function names. For each, explain why it is valid or invalid as a Python function name:

1. `calculate_total` valid, function name also uses underscore to seperate words
2. `3rd_function`invalid, cant start with digits
3. `print_values`valid, correct format for function name
4. `find-item` invalid, cant use "-"
5. `def` invalid, python keyword
6. `updateProfile` valid? can use capital for next word
7. `my_function`valid, function name format is correct
8. `try` invalid, python keyword
9. `init_data` valid, uses underscore correctly
10. `value@function`invalid, cant use @ character

## Problem 3: Boolean Expressions

Evaluate the following boolean expressions. For each:
- If it's a valid expression, show what it evaluates to and explain why.
- If it's not valid, explain why it's not valid.

1. `True and False`, valid , it uses "and" so it evalutes false
2. `5 > 3 or "apple" < "banana"`, valid, it is true because points to 5 greater than 3 
3. `not 10 <= 20`, valid because it is true and 'not true' is false
4. `True or 5 = 4` invalid, should be == because it is operator 
5. `"apple" != "orange" and 5`, valid apple and orange evaluate to true 'true and 5' also evaluates to true 
6. `3 < 5 not True`, invalid because it is missing operator  between not and 5 '(3>5) and not true'
7. `False == (3 > 4)` valid, boolean format is correct 3>4 is false so it is ==
8. `10 <= "10"`, invalid, cant compare integer and string ""
9. `True or not False`, valid, 'not false' is true, true is true (not false)
10. `5 and or 4`, invalid, cant use "and" or "or" without proper operates 

## Submission

Write your answers directly in the `main.py` file under each problem's comment, within the provided triple quotes. Ensure your explanations are clear and concise.
