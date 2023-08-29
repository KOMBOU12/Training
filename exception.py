x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z = int(x) / int(y)
except Exception as e:
    print('exception occured: ',e)
    z = None
except ZeroDivisionError as e:
    Print('Division by zero exception: ', e)
    z = None
print("Division is: ", z)
