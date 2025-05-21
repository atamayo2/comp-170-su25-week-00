# Welcome: Week 0  

Welcome to week 0 of comp150 Fall 2024 at Loyola University Chicago (LUC)!

Normally, you'd find a bunch of information here about the new material covered in the week, but since this is the first week, I'm taking the space at the start to review course expectations and general flow of each day of class.

The design of the course is 50% flipped. In a traditional course, most of synchronous class time is spent on lectures, and students are meant to solve homework problems on their own. In a 100% flipped classroom, students read the text chapters and watch prepared lectures or YouTube videos before class, and then during the class time when lectures normally take place, problems are solved by the instructor. Personally, I find that a mix of the two strategies is best. 

## Workload expectation
In general, each credit hour in a 100-200 level course will require an average of 3 hours per week spent on work for that course, outside of the synchronous meeting time. This course is 3 credits, so the general expectation is that you're spending roughly 9 hours a week outside of class: studying new material, working on homework and working on the project/paper for that semester. What follows is both my expectations from each student in the class, and my best guide for success.

## Self Study before each class
Therefore, students in this class should be prepared to study some of the lecture notes/textbook chapters/youtube videos in advanced of each class, and then take an online quiz.

## Pre-class quiz to test your comprehension
The quiz isn't timed in the traditional sense. The quiz will be available for a limited amount of time, generally for 24-48 hours before the class. Since you're doing the quiz online, its technically open book/open notes. Open internet really, because it exists primarily to make students have a sense of confidence in their preparedness to come to class and participate in discussion. If you take the quiz and you feel like you didn't do well, or you have questions, be sure to right them down! I will ask the class if they have questions at the start of every class after reviewing the solutions to the pre-class quiz.  

## In-class lectures
After the quiz everyday, there's going to be time for lecture and answering student questions on the new topic. 

## In class quiz:
During the first week, we'll be doing a logic and maths test, but in each week thereafter, there will be a short 30 minute comprehensive exam covering up to and including all of the material on the homework due the previous week. 

## Short break
Our class is scheduled for 150 minutes. That's a long time to stay seated, so after the in class exam, everyone gets a 10 minute long break to stretch their legs, grab a drink, use the restroom, etc. I actively discourage students to stay in the classroom during this time. If you finish the exam early, hand it in and start your break early!

## Lecture part #2
After the exam, I'll review the solutions (you'll receive your individually graded exams the following week), and then we'll cover the rest of the material for the week. Interspersed with this part of the lecture will be time for pairing (or group work) on the lab assignment. In general, the lab assignment will be 1 or 2 problems of medium difficulty, to prepare students for the more challenging homework problems. The lab problems are technically submitted as part of the homework, even though students will likely begin them in class.

## Homework
Students are encouraged to start working on the homework as soon as they feel comfortable. During office hours, I will be more than happy to help students with any issues they encounter while solving the homework, but if students haven't started it yet, then they will not benefit to the same degree. 

Because I feel like this can't be stressed enough, learning to program takes _time_. Sometimes you read a problem, write some code, and try to figure out why the code doesn't work. You struggle with it, and go to the next problem, you sleep on it, you wrestle with it again, you go to tutoring or office hours, and you finally figure it out. To some, the process of debugging code comes naturally, for other you will need to build up a new set of skills. 

Historically, on any given homework assignment students either do very well (80-100%) or they do poorly (0-20%). This is because unlike in other fields, you can determine immediately if the solution is correct, because the software is executed and you obtain your result in microseconds. Not so in other disciplines where it takes someone else to critique you when you are just beginning to know where you're making mistakes. 

## Pre-class quiz for the next week...
Once you've submitted your homework for the current week (or even earlier if you're curious) you can begin to digest the material for the next week's class. Because so much of what we will study in the first 8 weeks in cumulative and intertwined, its possible that material in future weeks will inspire you on a homework problem for the current week. 

Hopefully, this gives you all good idea of what's expected of you. Now onto the rest of the administrative material for this week.

The syllabus contains links to all of the resources for this class. Let's review those resources together:
### Sakai
If this is your first course at LUC, you may be unfamiliar with the course website. The link in the syllabus will take you to the sakai site for your section. To enter, you will need to enter your UVID and your password. Your UVID is generally all of the characters that make up your university email before the @ character. In my case, my email is amiller17@luc.edu, so my UVID is amiller17. On the sakai site, on the left hand side of the site by default, you will see numerous tabs. For our class, we won't be using most of them. The only tabs I anticipate you'll use regularly are the syllabus tab, which contains a link to the syllabus, and the gradebook tab, which contains the scores you've earned on all of the assignments you've submitted so far. To make it easy for students to know their expected letter grade in the course, I've conveniently made the points associated with all of the graded work sum to 1000. You can check the minimum %'s associated with each letter grade in the syllabus. Your mid-term grades will be posted to LOCUS at the mid point of the semester, and it will calculated as total points earned divided by total points available so far. 

## Tentative Course Calendar
If you're curious about what we're going to cover on any given day, and you just want a high-level overview of the day, you can check out the course calendar (link in the syllabus).

# week 0: Beginning to Program in Python
Ok, so these are lecture notes for if I was going to lecture for the full 150 minutes. The content will be written informally, and there will be links to resources placed throughout. 
The cannonical program basically every new coder learns first, no matter the language is the "Hello World!" program. In python it looks something like this:

```
def hello_world():
  print("hello world!")
    
hello_world()
```
This piece of code(also known as a program), will display the text "hello world!" to the screen. The coder jargon for displaying text, is called printing. REPL will let us render this text to highlight different words in different colors. This will match what you see if you write the code yourself. For all future example, the text of the code will be colored, and I'll also add line numbers to make it easier to talk about the code. See the code block below:
```python
1 def hello_world():
2   print("hello world!")
3     
4 hello_world()
```
On line #1, the word _def_ is highlighted in blue. Words highlighted in blue are so called _reserved strings_. 
>A string is a group of characters. A character is a single symbol, letter, or number. 'A', 'g','5', and '%' are all characters. A string is group of characters, like the word "stage" or the phrase "eat this cake! its really tasty. --Darius". In python, we can use single quotes('') or  double quotes (""), to let the computer know that we want it to consider whatever is inside the quotes to be a string. Otherwise, the group of characters must have some other meaning. For now, that other meaning is probably a number or a reserved word. But later, we may find other meanings.

Reserved strings are special words that convey to the computer that we intend a specific syntactic purpose. In this case, we are defining a function. 
>Different programming languages have different names for algorithms, functions or methods. All of these words refer to a series of steps used to solve a particular problem. In python the word is function, and we define functions using the def keyword.

Functions names like variable names (which we'll see in the next example), follow certain rules and conventions. Here's a breakdown of the main rules and guidelines:

### Rules:

1. **Start with a Letter or Underscore**: A function name must start with a letter (uppercase or lowercase) or an underscore (`_`). It cannot start with a number or special character.
2. **Alphanumeric and Underscore**: After the first character, a function name can contain letters, numbers, and underscores. No spaces or special characters are allowed.
3. **Case-Sensitive**: Function names in Python are case-sensitive, so `myfunction`, `myFunction`, and `MYFUNCTION` are all different functions.
4. **No Reserved Words**: You cannot use Python's reserved words as function names. These include words like `if`, `else`, `while`, `for`, `return`, etc.

### Conventions:

1. **Snake Case**: By convention, function names in Python are usually written in snake_case, where all letters are lowercase, and words are separated by underscores. For example, `my_function_name`.
2. **Avoid Leading Underscores Unless Necessary**: A leading underscore in a function name (e.g., `_my_function`) typically indicates that the function is intended for internal use within a module or class and should not be accessed from outside. It's a convention, not a strict rule, so it won't prevent access, but it signals to other developers that the function is considered "private" or "protected."
3. **Descriptive Names**: It's good practice to choose function names that clearly describe what the function does. This makes the code more readable and maintainable.

Here are some valid examples of function names:

```python
def my_function():
    pass

def _internal_use_only():
    pass

def calculate_sum(x, y):
    return x + y
```

And here are some invalid examples:

```python
def 123_function(): # Starts with a number
    pass

def my-function(): # Contains a special character
    pass

def for(): # Uses a reserved word
    pass
```

Following these rules and conventions helps ensure that your code is valid, readable, and consistent with common Python programming practices.
Back to our example:
```python
1 def hello_world():
2   print("hello world!")
3     
4 hello_world()
```
Let's break down the rest of the code snippet, explaining each part in detail.
### Line-by-Line Explanation:

1. **Line 1**: `def hello_world():`
   - `def`: This keyword is used to define a new function in Python.
   - `hello_world`: This is the name of the function. It follows the naming convention of using lowercase letters and underscores.
   - `()`: These parentheses are used to define the parameters (inputs) of the function. Since there are no parameters inside the parentheses, this function takes no arguments.
   - `:`: The colon marks the beginning of the function's body. All the code indented under this line will be part of the function.

2. **Line 2**: `print("hello world!")`
   - This line is indented, so it's part of the function's body.
   - `print`: This is a built-in Python function that outputs text to the console.
   - `("hello world!")`: This is the text that will be printed to the console when the `print` function is called. The text is enclosed in quotation marks, which is how strings are defined in Python.

3. **Line 3**: 
   - This line is blank and does not contain any code. Blank lines can be used to improve readability.

4. **Line 4**: `hello_world()`
   - This line calls the `hello_world` function that was defined earlier.
   - `hello_world()`: The function's name followed by parentheses is how you call a function in Python. Since this function doesn't take any parameters, the parentheses are empty.
   - When this line is executed, it will run the code inside the `hello_world` function, which means the text "hello world!" will be printed to the console.

### Summary:
The code defines a simple function named `hello_world` that prints the text "hello world!" to the console. Then, the function is called, causing the message to be displayed.

This example illustrates fundamental concepts in Python such as function definition, function calling, indentation, and the use of the `print` statement. It's a great starting point for understanding how functions work in Python.

### Inline Comprehension Questions
> Since there's no "Back of the book" in this text, questions will the reading. After the questions will be a break in the text so you don't accidentally see the answers. Take a moment to pause and think about the questions. When you think you have a good guess, feel free to jot down your answers, and then read the answers and see what you missed.

1. **Basic Understanding**:
   - What does the `def` keyword do in Python?
   - What is the purpose of the `print` statement in the code?
   - How would you describe the function's name and its naming convention?

2. **Function Concepts**:
   - What does the `hello_world` function do when it is called?
   - How many parameters does the `hello_world` function take? Can you explain what a parameter is?

3. **Code Execution**:
   - What will be the output of the code when it is run?
   - In what order are the lines of code executed?

4. **Indentation and Structure**:
   - Why is indentation important in defining the body of a function?
   - What is the significance of the colon `:` at the end of the function definition?

5. **Application and Extension**:
   - Can you write a similar function that prints a different message?
   - How would you modify the `hello_world` function to take a name as a parameter and print "Hello, [name]!"?

6. **Understanding Errors** (Advanced):
   - What would happen if you removed the indentation from line 2? Why?
   - What would happen if you tried to call the `hello_world` function before defining it?
---

### Solutions:
> Did you take a chance to think about the questions in advanced? If you didn't you're only cheating yourself. Learning takes time. Give yourself the time to succeed.

1. **What does the `def` keyword do in Python?**
   - Answer: The `def` keyword is used to define a new function in Python. It marks the beginning of a function declaration.

2. **What is the purpose of the `print` statement in the code?**
   - Answer: The `print` statement outputs the text within the parentheses to the console. In this case, it prints the string "hello world!".

3. **How would you describe the function's name and its naming convention?**
   - Answer: The function's name is `hello_world`, and it follows the snake_case naming convention where all letters are lowercase, and words are separated by underscores.

4. **What does the `hello_world` function do when it is called?**
   - Answer: When called, the `hello_world` function prints the text "hello world!" to the console.

5. **How many parameters does the `hello_world` function take? Can you explain what a parameter is?**
   - Answer: The `hello_world` function takes no parameters. A parameter is an input that a function can accept when called. It allows the function to receive data from outside and use it within the function.

6. **What will be the output of the code when it is run?**
   - Answer: The output of the code will be the text "hello world!" printed to the console.

7. **In what order are the lines of code executed?**
   - Answer: The lines are executed in the order they appear: the function is defined first (lines 1-2), and then it is called (line 4).

8. **Why is indentation important in defining the body of a function?**
   - Answer: Indentation in Python is used to define the scope of code blocks, such as the body of a function. It shows what lines of code are part of the function and distinguishes them from the rest of the code.

9. **What is the significance of the colon `:` at the end of the function definition?**
   - Answer: The colon `:` marks the beginning of the function's body. It signifies that the following indented lines are part of the function.

10. **Can you write a similar function that prints a different message?**
   - Answer: Yes, here's an example:
     ```python
     def say_hi():
         print("Hi there!")
     ```

11. **How would you modify the `hello_world` function to take a name as a parameter and print "Hello, [name]!"?**
   - Answer: You can add a parameter and use it in the print statement:
     ```python
     def hello_name(name):
         print(f"Hello, {name}!")
     ```

12. **What would happen if you removed the indentation from line 2? Why?**
   - Answer: Removing the indentation would cause a syntax error because Python uses indentation to determine the scope of code blocks, such as the body of a function.

13. **What would happen if you tried to call the `hello_world` function before defining it?**
   - Answer: Calling the function before defining it would result in a `NameError`, as Python would not recognize the name `hello_world` at the point where the function is called.

In the solution to question 11, we introduced the concept of fstrings. f-strings are a powerful feature in Python for string formatting, introduced in version 3.6. They allow you to embed expressions directly within string literals, making it easier to concatenate and format strings.

An f-string is created by placing an `f` before the opening quotation mark of a string and including expressions inside curly braces `{}` within the string.

### Example:

```python
1 name = "John"
2 age = 25
3 greeting = f"Hello, {name}! You are {age} years old."
```

Here, the variables `name` and `age` are directly embedded within the string, resulting in the greeting: "Hello, John! You are 25 years old."

### Key Points:

- **Conciseness**: f-strings provide a concise way to include variables or expressions inside strings.
- **Readability**: By embedding values directly in the string, the code remains clean and easy to read.
- **Dynamic Evaluation**: The expressions inside the curly braces are evaluated at runtime, allowing for dynamic string creation.

f-strings are an essential tool in Python programming, and you'll often find them used to create clear and efficient string representations.

### Variables and Boolean logic
This next example will introduce variables, boolean values, boolean logic, and function parameters.

```python
1  def check_age(age):
2      is_adult = age >= 18
3      is_teenager = 13 <= age < 18
4      print(f"Age provided: {age}")
5      if is_adult:
6          print("You are an adult.")
7      elif is_teenager:
8          print("You are a teenager.")
9      else:
10         print("You are a child.")
11     print(f"Is adult? {is_adult}")
12     print(f"Is teenager? {is_teenager}")
13 
14 check_age(20)
```
The function takes an input parameter, "age", and then produces text output that changes depending on the value used. Let's go through this example line by line.

### Line-by-Line Explanation:

1. **Line 1**: `def check_age(age):` - Defines a function named `check_age` that takes one parameter, `age`.
2. **Line 2**: `is_adult = age >= 18` - Declares a boolean variable `is_adult`, which is `True` if `age` is 18 or older.
3. **Line 3**: `is_teenager = 13 <= age < 18` - Declares a boolean variable `is_teenager`, which is `True` if `age` is between 13 and 17 (inclusive).
4. **Line 4**: `print(f"Age provided: {age}")` - Prints the provided age using an f-string.
5. **Line 5**: `if is_adult:` - Begins an `if` statement that checks if `is_adult` is `True`.
6. **Line 6**: `print("You are an adult.")` - Prints a message if `is_adult` is `True`.
7. **Line 7**: `elif is_teenager:` - Begins an `elif` statement that checks if `is_teenager` is `True`.
8. **Line 8**: `print("You are a teenager.")` - Prints a message if `is_teenager` is `True`.
9. **Line 9-10**: `else:` / `print("You are a child.")` - If neither `is_adult` nor `is_teenager` is `True`, this message is printed.
11. **Line 11-12**: `print(f"Is adult? {is_adult}")` / `print(f"Is teenager? {is_teenager}")` - Prints the values of the boolean variables.
12. **Line 14**: `check_age(20)` - Calls the `check_age` function with an argument of 20.

### Questions:
1. What is the output of the code when `check_age(20)` is called?
2. How would the output change if the age provided was 15?
3. What are the boolean variables `is_adult` and `is_teenager`, and how are they used in the code?
4. Can you write a similar function that checks and prints whether a number is positive, negative, or zero?
---

### Questions and Answers:
1. **What is the output of the code when `check_age(20)` is called?**
   - Answer: The output will be:
     ```
     Age provided: 20
     You are an adult.
     Is adult? True
     Is teenager? False
     ```

2. **How would the output change if the age provided was 15?**
   - Answer: The output would indicate that the person is a teenager, with `is_adult` being `False` and `is_teenager` being `True`.

3. **What are the boolean variables `is_adult` and `is_teenager`, and how are they used in the code?**
   - Answer: They store the result of boolean expressions and are used in the `if` statement to determine the message to print.

4. **Can you write a similar function that checks and prints whether a number is positive, negative, or zero?**
   - Answer: __This is a homework question for this week__

### Working with numbers
In this next example, we'll be looking at a piece of code that shows some of the kinds of operations we can perform with numbers. We'll also include type annotations, a docstring, and inline comments and introduce those concepts as well.

### Code Example:

```python
1  def calculate_statistics(number1: int, number2: float) -> str:
2      """Calculates and returns a summary of statistics.
3      
4      Args:
5          number1 (int): An integer input.
6          number2 (float): A decimal input.
7      
8      Returns:
9          str: A string summary of the statistics.
10     """
11     sum_result = number1 + number2  # Addition
12     product = number1 * number2     # Multiplication
13     is_odd = number1 % 2 == 1       # Modulo operation to check odd
14
15     summary = (f"Sum of {number1} and {number2}: {sum_result}\n"
16                f"Product of {number1} and {number2}: {product}\n"
17                f"{number1} is {'odd' if is_odd else 'even'}")
18
19     return summary
20 
21 print(calculate_statistics(3, 4.5))
```

### Line-by-Line Explanation:

1. **Line 1**: `def calculate_statistics(number1: int, number2: float) -> str:` - Defines a function with type annotations for the parameters and return type. This improves code readability and helps tools provide better analysis.
2. **Line 2-10**: These lines form the docstring, which provides a detailed explanation of the function, its parameters, and its return value. This is essential for understanding the function's purpose and usage.
3. **Line 11**: `sum_result = number1 + number2  # Addition` - Calculates the sum of `number1` and `number2` and stores it in `sum_result`. The inline comment explains the operation.
4. **Line 12**: `product = number1 * number2     # Multiplication` - Calculates the product of the numbers.
5. **Line 13**: `is_odd = number1 % 2 == 1       # Modulo operation to check odd` - Uses the modulo operator `%` to check if `number1` is odd. If `number1` divided by 2 has a remainder of 1, it's odd.
6. **Line 15-17**: Constructs a summary string that includes the results of the previous calculations and whether `number1` is odd or even.
7. **Line 19**: `return summary` - Returns the summary string.
8. **Line 21**: `print(calculate_statistics(3, 4.5))` - Calls the function with an integer and a float, and prints the result.

### Questions for Students:
1. What is the purpose of the type annotations in the function definition, and how are they used?
2. What is a docstring, and why is it included in the code?
3. How does the code determine if `number1` is odd or even?
4. What will be the output of the code when `calculate_statistics(3, 4.5)` is called?

### Questions and Answers:
1. **What is the purpose of the type annotations in the function definition, and how are they used?**
   - Answer: Type annotations indicate the expected data types for the function's parameters (`number1` as `int`, `number2` as `float`) and its return value (`str`). They enhance code readability and allow tools to provide better analysis and error checking.

2. **What is a docstring, and why is it included in the code?**
   - Answer: A docstring is a multiline comment used to explain the purpose, parameters, and return value of a function. It serves as documentation and helps others understand the function's usage.

3. **How does the code determine if `number1` is odd or even?**
   - Answer: The code uses the modulo operator `%` to divide `number1` by 2 and check the remainder. If the remainder is 1, `number1` is odd; otherwise, it's even.

4. **What will be the output of the code when `calculate_statistics(3, 4.5)` is called?**
   - Answer:
     ```
     Sum of 3 and 4.5: 7.5
     Product of 3 and 4.5: 13.5
     3 is odd
     ```

### Booleans and truth tables

Booleans are a fundamental data type in programming that represents one of two values: `True` or `False`. They are named after George Boole, who first defined an algebraic system of logic in the mid-1800s.

In Python, booleans are often used to represent the results of logical comparisons, such as equality or inequality tests.

### Example:

```python
x = 10
y = 5
is_greater = x > y  # Evaluates to True
is_equal = x == y   # Evaluates to False
```

### Truth Tables

A truth table is a mathematical table used to represent the values of logical expressions based on their possible inputs. It's a systematic way to list every possible combination of truth values for a given logical operation, such as AND, OR, and NOT.

Here are the truth tables for the three basic logical operations:

1. **AND** (Both must be true)

   | A     | B     | A AND B |
   |-------|-------|---------|
   | True  | True  | True    |
   | True  | False | False   |
   | False | True  | False   |
   | False | False | False   |

2. **OR** (At least one must be true)

   | A     | B     | A OR B  |
   |-------|-------|---------|
   | True  | True  | True    |
   | True  | False | True    |
   | False | True  | True    |
   | False | False | False   |

3. **NOT** (Reverses the truth value)

   | A     | NOT A |
   |-------|-------|
   | True  | False |
   | False | True  |

Booleans and truth tables are fundamental to understanding logic in programming. They form the basis of conditional statements and control flow, allowing programs to make decisions and perform different actions depending on certain conditions. Understanding these concepts will enable you to write more complex and dynamic code.
### What does it mean for something to be evaluated in a boolean context: Truthiness and Falsiness

In programming, the concepts of truthiness and falsiness refer to how non-boolean values are treated when evaluated in a boolean context. Essentially, truthiness and falsiness determine how values are interpreted as `True` or `False` when used in conditions, such as in an `if` statement.

### Truthiness and Falsiness in General:

- **Truthiness**: A value is considered "truthy" if it evaluates to `True` in a boolean context, even if it is not explicitly the boolean value `True`.
- **Falsiness**: Conversely, a value is considered "falsy" if it evaluates to `False` in a boolean context, even if it is not explicitly the boolean value `False`.

Different programming languages have different rules for what values are considered truthy or falsy.

### Truthiness and Falsiness in Python:

In Python, the following values are considered falsy:

- `None`
- `False`
- Zero of any numeric type, such as `0`, `0.0`, `0j`
- Any empty sequence, such as `''`, `[]`, `()`
- Any empty mapping, such as `{}`
- Custom objects that implement a `__bool__()` or `__len__()` method that returns `False` or `0`

All other values are considered truthy.

### Examples in Python:

```python
if 'hello':           # Truthy, because the string is not empty
    print('True')

if []:                # Falsy, because the list is empty
    print('True')
else:
    print('False')

if 42:                # Truthy, because the number is not zero
    print('True')

if 0.0:               # Falsy, because the number is zero
    print('True')
else:
    print('False')
```

Understanding truthiness and falsiness is vital for writing conditional statements and working with logical operations. It allows you to leverage non-boolean values in conditions and can lead to more concise and expressive code. However, it's essential to be aware of these rules, as unexpected truthiness or falsiness can lead to subtle bugs in a program.

### Variable Naming Rules in Python

Variables are used to store data in a program, and their names should be chosen to convey meaning. In Python, the rules for naming variables are:

1. **Start with a Letter or Underscore**: Variable names must start with a letter (either uppercase or lowercase) or an underscore.
2. **Contain Only Alphanumeric Characters and Underscores**: The rest of the name can consist of letters, numbers, and underscores.
3. **Cannot Be a Reserved Word**: Python's reserved words, such as `if`, `for`, `while`, cannot be used as variable names.
4. **Case-Sensitive**: Variable names are case-sensitive, so `myVariable` and `myvariable` are different.
5. **Conventions**: By convention, variable names are written in snake_case (e.g., `my_variable`), and constants are written in UPPERCASE.

### Common Data Types in Python

Python has several built-in data types that can be grouped into the following categories:

1. **Numeric Types**: Integers (`int`), Floating-Point Numbers (`float`), Complex Numbers (`complex`).
2. **Sequence Types**: Lists (`list`), Tuples (`tuple`), Ranges (`range`).
3. **Text Type**: Strings (`str`).
4. **Mapping Type**: Dictionaries (`dict`).
5. **Set Types**: Sets (`set`), Frozen Sets (`frozenset`).
6. **Boolean Type**: Boolean (`bool`), with values `True` or `False`.
7. **Binary Types**: Bytes (`bytes`), Byte Arrays (`bytearray`).

### Type Annotations in Python

Type annotations are used to indicate the expected type of a variable, parameter, or return value. They enhance code readability and can help with error checking.

Here's how you can use type annotations for different types:

- **Integers**: `x: int = 10`
- **Floats**: `y: float = 5.5`
- **Strings**: `name: str = "Alice"`
- **Lists**: `numbers: list[int] = [1, 2, 3]`
- **Dictionaries**: `mapping: dict[str, int] = {'a': 1}`
- **Booleans**: `is_active: bool = True`
- **Function Parameters and Return Types**:
  ```python
  def add(x: int, y: int) -> int:
      return x + y
  ```

Understanding the rules for naming variables, the common types in Python, and how to use type annotations will enable you to write clear, expressive, and maintainable code. It's an essential foundation for programming in Python.

### Introduction to Data Structures

Data structures are a way of organizing and storing data in a computer. They provide a means to manage large amounts of data efficiently for uses such as large databases and internet indexing services. In Python, two fundamental data structures are lists and dictionaries.

#### Lists

Lists are ordered collections of items and are one of the most versatile data structures in Python. They can contain items of different types, but usually, all the items in a list are of the same type.

#### Dictionaries

Dictionaries are unordered collections where data is stored in key-value pairs. Keys must be unique and immutable, while values can be of any type.

### Code Example:

```python
def add_to_list(lst: list, item: int) -> None:
    """Add an item to the list."""
    lst.append(item)

def read_from_list(lst: list, index: int) -> int:
    """Read an item from the list by index."""
    return lst[index]

def update_list(lst: list, index: int, item: int) -> None:
    """Update an item in the list by index."""
    lst[index] = item

def delete_from_list(lst: list, index: int) -> None:
    """Delete an item from the list by index."""
    lst.pop(index)

def create_dict() -> dict:
    """Create a new dictionary."""
    return {}

def add_to_dict(dct: dict, key: str, value: int) -> None:
    """Add a key-value pair to the dictionary."""
    dct[key] = value

def read_from_dict(dct: dict, key: str) -> int:
    """Read a value from the dictionary by key."""
    return dct[key]

def update_dict(dct: dict, key: str, value: int) -> None:
    """Update a value in the dictionary by key."""
    dct[key] = value

def delete_from_dict(dct: dict, key: str) -> None:
    """Delete a key-value pair from the dictionary by key."""
    del dct[key]
```

### Questions for Students:

1. What are lists and dictionaries, and how are they used in Python?
2. Explain the CRUD operations performed on lists and dictionaries in the code.
3. How can you handle situations where you attempt to read from or delete a non-existing index or key?
4. What are some use cases for using lists and dictionaries in programming?

### Questions and Answers:

1. **What are lists and dictionaries, and how are they used in Python?**
   - Answer: Lists are ordered collections of items, and dictionaries are unordered collections of key-value pairs. Lists are used for storing elements sequentially, while dictionaries provide a way to associate keys with values.

2. **Explain the CRUD operations performed on lists and dictionaries in the code.**
   - Answer: CRUD operations include Create, Read, Update, and Delete. For lists, items can be added (created) with `append`, read by index, updated by index, and deleted with `pop`. For dictionaries, key-value pairs can be created, read, updated, or deleted using key indexing.

3. **How can you handle situations where you attempt to read from or delete a non-existing index or key?**
   - Answer: You can use exception handling, such as try-except blocks, to catch `IndexError` for lists or `KeyError` for dictionaries. This allows graceful handling of errors when accessing non-existing indices or keys.

4. **What are some use cases for using lists and dictionaries in programming?**
   - Answer: Lists are commonly used to store and iterate through ordered data, such as elements in a sequence. Dictionaries are used for mapping keys to values, such as storing configuration settings or representing a sparse matrix.

### Lists and Dictionary: Example Usage

Here's a code example for a function that takes two lists as input and creates a dictionary where the keys are from the first list and the values are from the second list. The function ensures that the lists are of the same length.

### Code Example:
```python
1   def create_dict_from_lists(keys: list[str], values: list[int]) -> dict[str, int]:
2       """Create a dictionary from two lists of equal length.
3       
4       Args:
5           keys (list[str]): A list of keys.
6           values (list[int]): A list of values.
7       
8       Returns:
9           dict[str, int]: A dictionary with keys from the first list and values from the second list.
10      """
11      if len(keys) != len(values): # Check if lists are of the same length
12          raise ValueError("Keys and values must be of the same length.")
13      
14      result_dict = {}
15      for i in range(len(keys)): # Iterate through indices of both lists
16          key = keys[i]
17          value = values[i]
18          result_dict[key] = value
19      
20      return result_dict

```
### Line-by-Line Explanation:

1. **Line 1**: Function definition with type annotations for parameters and return type.
2 **Lines 2-10**: Docstring explaining the purpose, parameters, and return value of the function.
3. **Line 11**: An inline comment mentioning the purpose of the upcoming condition.
4. **Line 12**: Checks if the lengths of the keys and values lists are the same; if not, raises a `ValueError`.
5. **Line 14**: Initializes an empty dictionary to store the result.
6. **Line 15**: Uses a for loop to iterate through the indices of the keys list (and implicitly, the values list since they have the same length).

7. **Line 16**: Retrieves the key from the keys list using the current index.
8. **Line 17**: Retrieves the value from the values list using the current index.
9. **Line 18**: Assigns the value to the corresponding key in the result dictionary.
10. **Line 20**: Returns the created dictionary.


### Questions for Students:

1. What is the purpose of the `create_dict_from_lists` function, and how does it ensure that the input lists are of the same length?
2. How does the `for` loop work in this code, and how are the keys and values retrieved using the index?
3. What error will be raised if the input lists have different lengths, and how can it be handled?
4. How would you write a test case to verify that the function works correctly with valid input lists?

---

### Questions and Answers:

1. **What is the purpose of the `create_dict_from_lists` function, and how does it ensure that the input lists are of the same length?**
   - Answer: The function's purpose is to create a dictionary using two lists, where the first list provides the keys and the second list provides the values. It ensures that the lists are of the same length by checking their lengths using `len(keys) != len(values)` and raising a `ValueError` if they differ.

2. **How does the `for` loop work in this code, and how are the keys and values retrieved using the index?**
   - Answer: The `for` loop iterates through the indices of the keys list using `range(len(keys))`. Inside the loop, the keys and values are retrieved using the current index `i`, with `key = keys[i]` and `value = values[i]`. The key-value pairs are then added to the result dictionary.

3. **What error will be raised if the input lists have different lengths, and how can it be handled?**
   - Answer: If the input lists have different lengths, a `ValueError` with the message "Keys and values must be of the same length" will be raised. This error can be handled by enclosing the function call in a try-except block that catches this specific error, allowing for graceful error handling.

4. **How would you write a test case to verify that the function works correctly with valid input lists?**
   - Answer: A test case could involve calling the function with two lists of the same length, such as `keys = ['a', 'b']` and `values = [1, 2]`, and verifying that the returned dictionary is `{'a': 1, 'b': 2}`. Another test case could include providing lists of different lengths to ensure that the appropriate `ValueError` is raised.

### Unit tests and loops
In this final section we'll introduce loops (although you got a sneak peak last section to the _for_ loop) and unit tests. We'll also showcase the test() function you'll use in future homework and lab assignments.

### Code Example:

```python
1   import sys
2   
3   def test(did_pass):
4       """ Print the result of a test. """
5       linenum = sys._getframe(1).f_lineno
6       msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
7       print(msg)
8   
9   def factorial(n: int) -> int:
10      """Calculate the factorial of a non-negative integer.
11      
12      Args:
13          n (int): A non-negative integer.
14      
15      Returns:
16          int: The factorial of n.
17      """
18      result = 1
19      for i in range(1, n + 1): # For loop to iterate through the range
20          result *= i
21      return result
22  
23  def count_odds(numbers: list[int]) -> int:
24      """Count the number of odd numbers in a list.
25      
26      Args:
27          numbers (list[int]): A list of integers.
28      
29      Returns:
30          int: The count of odd numbers in the list.
31      """
32      count = 0
33      i = 0
34      while i < len(numbers): # While loop to iterate through the list
35          if numbers[i] % 2 == 1:
36              count += 1
37          i += 1
38      return count
39  
40  def test_suite():
41      """ Run the suite of tests for code in this module (this file).
42      """
43      test(factorial(5) == 120)
44      test(factorial(0) == 1)
45      test(count_odds([1, 2, 3, 4, 5]) == 3)
46      test(count_odds([2, 4, 6]) == 0)
47  
48  test_suite() # Here is the call to run the tests
```

### Line-by-Line Explanation:

1. **Line 1**: Imports the `sys` module, needed to obtain the line number of the calling code in the test function.
2. **Lines 3-7**: Defines the `test` function, which takes a boolean and prints a success or failure message, including the line number of the test.
3. **Lines 9-21**: Defines the `factorial` function, which calculates the factorial of a non-negative integer using a `for` loop. The docstring and type annotations provide details about the function.
4. **Lines 23-38**: Defines the `count_odds` function, which counts the number of odd numbers in a list using a `while` loop.
5. **Lines 40-46**: Defines the `test_suite` function, which runs a series of tests to verify the functionality of the `factorial` and `count_odds` functions.
6. **Line 48**: Calls the `test_suite` function to run the tests.

### Questions for Students:

1. What is the purpose of the `test` function, and how does it obtain the line number of the calling code?
2. Explain the use of the `for` loop in the `factorial` function.
3. Describe how the `count_odds` function uses a `while` loop to achieve its goal.
4. What are the benefits of including docstrings and type annotations in the functions?
5. How can you write a test to verify that the `factorial` function returns an error for negative input?

### Questions and Answers:

1. **What is the purpose of the `test` function, and how does it obtain the line number of the calling code?**
   - Answer: The `test` function prints the result of a test (either "ok" or "FAILED"), including the line number where the test was called. It obtains the line number using `sys._getframe(1).f_lineno`.

2. **Explain the use of the `for` loop in the `factorial` function.**
   - Answer: The `for` loop in the `factorial` function iterates from 1 to `n`, multiplying the `result` variable by each number in the range. This calculates the factorial of `n`.

3. **Describe how the `count_odds` function uses a `while` loop to achieve its goal.**
   - Answer: The `count_odds` function uses a `while` loop to iterate through the list of numbers. It checks if each number is odd (using the modulo operator `%`) and increments the count if it is.

4. **What are the benefits of including docstrings and type annotations in the functions?**
   - Answer: Docstrings provide a detailed description of the function's purpose, parameters, and return value, enhancing code readability. Type annotations indicate the expected types for parameters and return values, aiding in code understanding and
error checking.

5. **How can you write a test to verify that the `factorial` function returns an error for negative input?**
   - Answer: A test for negative input could involve using a try-except block to call the `factorial` function with a negative argument and verifying that an expected error is raised.

