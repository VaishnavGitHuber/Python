# Lambda Function
# * Lambda Function is a simple anonymous function
# * Lambda functions can have any number of arguments
#   but can only have a single expression
# * syntax: lambda arguments: expression

# Lambda function with 1 argument
x = lambda a: a * 10
# Will return 5 * 10 = 50
print("x(5) = ", x(5))

# Lambda function with 2 arguments
x = lambda a, b: a * b
# a = 4,b = 6: Will return 4 * 6 = 24
print(f"x(4,6): {x(4,6)}")

# Lamda function with 3 arguments
x = lambda a, b, c: a+b+c
# a=3,b=4,c=5: will return 3+4+5 = 12
print(f"x(3,4,5): {x(3,4,5)}")

# What is its importance ?
# * Lamda function is used to call a function inside another function
# * Sample example of its importance is mentioned here,

def myfunction(n):
    return lambda x: x * n

doubler = myfunction(2)
tripler = myfunction(3)
# Doubler of 5 : 5*2 = 10
print(f"doubler(5): {doubler(5)}")
# Tripler of 7: 7 * 3 = 21
print(f"tripler(7): {tripler(7)}")



