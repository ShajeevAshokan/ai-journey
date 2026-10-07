def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest= n
    return biggest

print(find_max([12,72,93,67,45]))