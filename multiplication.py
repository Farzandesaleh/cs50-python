def mul(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


# gettung user number
number = int(input("Enter a number: "))

# getting user limit
limit = int(input("How far do you want the multiplication table? "))

# printing mul
mul(number, limit)
