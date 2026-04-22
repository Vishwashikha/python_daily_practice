numbers = [4, 9, 2, 15, 7]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number:", largest)