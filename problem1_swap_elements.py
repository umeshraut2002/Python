num = [23, 65, 19, 90]

idx1 = 0
idx2 = 2

for i in range(len(num)):
    print(num[i])

print("Before Swap: ",num)

temp = num[idx1]
num[idx1] = num[idx2]
num[idx2] = temp

print("After Swap: ",num)