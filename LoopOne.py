#for loop

#For loop with final range - end

for i in range(10):
    print(i, end='\t') #0123456789

n = int(input("\nEnter the number: "))
for i in range(n):
    print(i, end='\t')
    print()
#starting and final - start and end

for i1 in range(1,10):
    print(i1, end='\t') #123456789
print("\n")

n1 = int(input("\nEnter the number: "))
for i in range(1,11):
    print(str(n1) + "*" +str(i)+"="+str(n1*i))

#increment - automatically 1 is increment

print("\n increased by 2")
for i2 in range(1,11,2):
    print(i2, end="\t")

#decrement

print("\n decrement")
for i3 in range(10,1,-2):
    print(i3, end="\t")

n3= int(input("\nPlease enter ur number: "))
for i in range(10,0,-1):
    print(i*n3, end="\t")

#list - #for with list (for each loop)
# we need to create alist with some data
print("\n list")
l1 = [1,3,5,7,10,20,'Testing','www.testingworld.com']
for i in l1:
    print(i, end="\t")

print("\n")
for i in 'Testing':
    print(i, end="\t")

print("\nmultiple numeric values")
l2 = [43,44,56,34,77]
z=0
for i in l2:
    z =z+i
print("Sum is: " + str(z))

