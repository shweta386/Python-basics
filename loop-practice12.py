# prime number using loop

# num = int(input("Enter the number: "))

# i = 2
# is_prime = True

# while i < num:
#     if num % i == 0:
#         is_prime = False
#         break
#     i += 1

# if is_prime and num > 1:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


num = int(input("Enter the number="))
i = 2

prime = True

if num <= 1:
    prime = False

while i < num:
    if num % i == 0:
        prime = False
        break
    i += 1
    if prime:
        print(i)
