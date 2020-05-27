""""

There are tow types of functions:

    1- built-in functions
    2- user-defined functions

built-in functions are already made for you and ready for use
user-defined functions are left for you to define them according to your need

THE SYNTAX FOR DEFINING USER-DEFINED FUNCTIONS IS:

    def function_name():
        statements

where function_name is the name of the function you wanna name it for example:

    def hello():
        print("Hello World")

"""


# function without parameter
def function_name():
    print("I'm function without parameter")


# function with one parameter  (you can pass many parameters to the function as you want)
def function_name1(param):
    print(f"I'm a function with {param} parameter")


# calling function (without calling functions have no effects)
function_name()
function_name1("one")
