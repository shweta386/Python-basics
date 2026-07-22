def can_vote(age):
    if age>=18:
        return True
    else:
        return False
a=int(input("Enter the age:"))
ans=can_vote(a)
print(ans)