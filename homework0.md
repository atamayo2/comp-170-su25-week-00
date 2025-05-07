# Homework 0
In the file main.py please complete the following homework questions:

### 1. Function: `is_even`

**Description**: Write a function that takes an integer and returns `True` if it's even and `False` if it's odd.

**Unit Tests**:

```python
def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)
```

### 2. Function: `split_dict_to_lists`

**Description**: Write a function that takes a dictionary and returns two lists: one containing the keys and the other containing the values.

**Unit Tests**:

```python
def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
```

### 3. Function: `evaluate_expression`

**Description**: Write a function that takes two boolean values and a string operator ('and', 'or', 'not') and returns the result of evaluating the expression. If the operator is 'not', only consider the first boolean value.

**Unit Tests**:

```python
def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)
```

### 4. Function: `find_odd_numbers`

**Description**: Write a function that takes a list of integers and returns a new list containing only the odd numbers from the original list.

**Unit Tests**:

```python
def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])
```


### 5. Function: `calculate_average`

**Description**: Write a function that takes a list of numbers and returns the average of those numbers.

**Unit Tests**:

```python
def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)
```

### Test Suite:

```python
def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
```
# Homework Grading
The homework assignments in this course are graded in the following ways. First, if the test_suite for the homework does not pass, then marks are taken off. Second, as the semester progresses certain inefficient strategies taken when developing code will be identified as bad practice, and if those practices are used, then additional points will be lost. Finally, points are awarded for clever solutions and for explanations to why questions. Students are encouraged to use inline comments and create descriptive variable names. 
