n = int(input("Enter how many num u want!"))
first = 0
sec = 1
for i in range(n):
    print(first)
    tem = first
    first = sec
    sec = tem+first
