n=int(input("Enter a number: "))
x=n
total=0
while n > 0:
    total += n%10
    n //= 10
print(f"The sum of the digits in {x} is {total}")
