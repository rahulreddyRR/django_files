
n = int(input("Enter fact number"))
# result = fact(n)
# print(result)
result = 1

for i in range(n,0,-1):
    result = result*i
    print(result)
