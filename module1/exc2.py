# try:
#     a = int(input("Enter the number"))
#     b = int(input("Enter the number"))
#     total = a/ b
# except ValueError:
#     print("That wasn't a number")
# except ZeroDivisionError:
#     print("None")
# else:
#     print(total)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "None"

print(safe_divide(10, 2))
print(safe_divide(10, 0))



