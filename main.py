#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
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

"""
# Problem 2
"""
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


"""
# Problem 3
"""
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

"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
