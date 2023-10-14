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

input1 = int(input("Enter a number: "));
result = square(input1);
print(result);