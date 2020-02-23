# n = int(input("Enter the num of rows : "))
# num = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num = num+1
#     print()
n = input("Enter the name to print:")
m=n.split(",")
for i in range(len(n)):
    for j in range(0,i+1):
        print(n[j],end=' ')
    print()
