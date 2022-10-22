lst = list(map(int,input('введите числа:\n ').split()))
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
new_lst.sort()
print(new_lst)