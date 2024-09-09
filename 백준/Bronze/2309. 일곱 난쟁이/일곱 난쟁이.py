arr = []
for _ in range(9):
    a = int(input())
    arr.append(a)
arr.sort()
    
sumA = sum(arr)
fake = []
for i in range(9):
    for j in range(i+1, 9):
        if(len(fake)==2):
            continue
        if(sumA - arr[i] - arr[j] == 100):
            fake.append(arr[i])
            fake.append(arr[j])
            
for i in arr:
    if i in fake:
        continue
    print(i)