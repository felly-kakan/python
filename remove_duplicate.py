numbers=[2,3,1,2,4,2,3,1,6,7,8,7,10]
unique=[]
for num in numbers:
    if num not in unique:
      unique.append(num)
      unique.sort()
print(unique)     

    