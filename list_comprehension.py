numbers = []
for num in [1,2,3,4,5]:
    numbers.append(num**2)
print(numbers)

# LIST COMPREHENSION
# IDENTICAL TO THE ONE ON TOP
numbers1 = [num**2 for num in [1,2,3,4,5]]
print(numbers1)