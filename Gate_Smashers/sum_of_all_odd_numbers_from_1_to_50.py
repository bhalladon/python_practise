# using for loop
total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i

print(total)

# using while loop
a = 1
total = 0

while a <= 50:
    if a%2 != 0:
        total += a
    a+=1

print(f"Value of {total}")

# using another login using while

a = 1
total = 0
while a <= 50:
    total += a
    a += 2