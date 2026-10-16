def add(a,b):
    return a+b

def subtrack(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b



print("Welcome to Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

choice =input("enter your choice (1-5:)")

if choice =="5":
    print("thank you!")

elif choice in ["1","2","3","4"]:
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))

    if choice =="1":
        print("Result:", add(num1, num2))  

    elif choice=="2":
        print("Result:", subtrack(num1,num2))

    elif choice=="3":
        print("Result:",multiply(num1,num2))

    elif choice =="4":
        if num2 ==0:
            print("cannot divide by zero")
        else:
            print("Result:" ,divide(num1,num2))


else:
    print("Invalid choice")