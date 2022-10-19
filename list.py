# wapp to read list from the user and print on the screen

num = []

n = int(input("Enter elements to add"))

for i in range(n):
    ele=int(input("enter element"))
    num.append(ele)

print(num)

for d in num:
    print(d, end = ' ')
print()


