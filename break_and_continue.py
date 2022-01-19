items = ['One', 'Two', 'Three', 'Four', 'Five']

for item in items:
    if item =="Two":        # THIS WILL SKIP "Two"
        continue
    print(item)

for item in items:
    if item == "Three":     # THIS WILL STOP AT BEFORE "Three"
        break
    print(item)

num = 0

while num < 20:
    num += 1
    if num % 2 == 0:
        continue            # SKIP
    print(num)

num1 = 0

while num1 <= 1_000_000_000:
    num1 += 1
    if num1 == 13:
        break               # STOP BEFORE TURNING 13
    print(num1)

