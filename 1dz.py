k = 1 
my_pi = 0
d = input('введите число d: ')

for i in range(100000):
    if i % 2 == 0:
        my_pi += 4/k
    else:
        my_pi -= 4/k
    k+=2

print(my_pi)
print(f'\nЧисло п с точностью {d}: {str(my_pi)[:len(d)]}\n')