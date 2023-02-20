# define the function needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit
print("A. addition \nB. Subtraction \nC. Multiplication \nD. Division")

c = input("Input your choise: ")

def add(a,b):
   answer = a + b
   print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

if c == "a" or c == "A":
    print("Addition")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    add(a,b)
elif c == "b" or c== "B":
    print("Substraction")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sub(a,b)
elif c == "c" or c== "C":
    print("Multiplication")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    mul(a,b)
elif c == "d" or c== "D":
    print("Division")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    div(a,b)