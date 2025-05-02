def sum(number_1, number_2):
    return number_1 + number_2

def sub(number_1, number_2):
    return number_1 - number_2

def mul(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    if number_2 != 0:
        return number_1 / number_2
    else:
        return "Error: Division by zero is not allowed."


# getting first number from user
number_1 = float(input("First number :"))

# getting second number from user
number_2 = float(input("second number:"))

# ask the user what he/she want to do
doing = input("what do you want to do?(sum, subtract, multiply, divide): ")


# check what the user want to do and call the function
if doing == "sum":
    print("The sum is: ", sum(number_1, number_2))
elif doing == "subtract":
    print("The subtract is: ", sub(number_1, number_2))
elif doing == "multiply":
    print("The multiply is: ", mul(number_1, number_2))
elif doing == "divide":
    print("The divide is: ", div(number_1, number_2))

else:
    print("Error: Invalid operation. Please choose from sum, subtract, multiply, or divide.")