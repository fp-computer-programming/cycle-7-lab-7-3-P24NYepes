"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
def greeting():
    """
    This function prints 'Hello World!' and returns its docstring.
    """
    print("Hello World!")
    return greeting.__doc__

# calls the function
result = greeting()
print("Test Case 1 Result:", result)

#Call the function again and check if the returned docstring is not empty
result = greeting()
print("Test Case 2 Result:", bool(result))

# Override the docstring
greeting.__doc__ = "Modified docstring"
result = greeting()
print("Test Case 3 Result:", result)

#testing with a empty docstring
greeting.__doc__ = ""
result = greeting()
print("Test Case 4 Result:", bool(result))