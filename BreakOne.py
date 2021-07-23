n = int(input("Enter the number: "))

for i in range(1, 11):
    if (n*i)==30:
        break
    print(n*i)

n1 = int(input("Enter the numer: "))

for i1 in range(1,11):
    if (n1*i1)%10==0:
        continue
    print(n1*i1)