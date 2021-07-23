data = "Testing world"
print(data)

d1='www.the"testingworld".com'
print("\n", d1)

d2="""
This is testing world website
wesite is: testing world.com
paragraph
"""
print(d2 + "Thank you" *3)

name = input("Enter ur first and lat name: ")
address=input("please enter your address: ")
profile = input("Enter ur job profile: ")

print("Person "+ name + " live in "+ address + " working as"+ profile)

#fetching substring by giving index
emil = "testingworld@gmail.com"
#for i in emil:
print(emil[0:])
print(emil[:22])
print(len(emil))

z=0
for i in emil:
    if i=='l':
        z=z+1
print(z, "Two times")

x=len(emil)
y=len(emil.replace("l",""))
print(x-y)

a="mail"
print(emil.find(a))