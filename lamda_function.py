# lambda functions
def first_function():
    print("Ajmal")

first_function();

def second_function(name = "Ajmal"):
    print(f"Assalam Walaikum {name}");

second_function('Quraishi');
#return statement
def square(num):
    return num*num;

# input1 = int(input("Enter a number: "));
# result = square(input1);
# print(result);
# #recursion function (a function that calls itself) and (repeating a task)
# def factorial(n):
#     if n==0:
#         return 1;
#     return n*factorial(n-1);

# input1 = int(input("Enter a number: "));
# result = factorial(input1);
# print(result);
#lambda function (anonymous function)and (one line of code)
#old def
def square(num):
    return num*num;
square = lambda num: num*num;
input1 = int(input("Enter a number: "));
result = square(input1);
print(result);
def add(a, b):
    return a + b;
x = lambda a, b: a + b;
print(x(5, 6));