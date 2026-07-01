# Sum of all the numbers from 1 to 100 divisible by 2 and 7.
start = int(input("Enter the start num:"))
end = int(input("Enter the end num:"))
i = start
total = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1
print(f"sum are {total}")
