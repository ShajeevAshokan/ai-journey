for n in range(1, 31):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:    
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)