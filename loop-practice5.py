# start to end print which is divisible by3 and 4
start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i)
    i += 1
