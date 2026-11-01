try:
    #answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as error:
    print(error)