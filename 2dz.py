x = int(input('введите число: '))
i = 2
lst= []
temp = x
while i <= temp:
    if temp % i == 0:
        lst.append(i)
        temp //= i
    else:
        i+=1
print(lst)