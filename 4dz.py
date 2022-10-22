import random

k= int(input('ВВедите натуральную степень K : '))

def create_str(sp):
    lst = sp[::-1]
    wr = " "
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i+1] !=0:
                    wr+= '+'
            elif i== len(lst) - 2 and lst[i]!= 0:
                wr += f'{lst[i]}x'
                if lst[i+1] !=0:
                    wr+= '+'
            elif i == len(lst) - 1 and lst[i] !=0:
                wr+= f'{lst[i]}=0'
            elif i == len(lst) - 1 and lst[i] ==0:
                wr +='=0'
    return wr

koef = [random.randint(0,101)for i in range (k+1)]
result = create_str(koef)
with open('zadacha.txt','w') as text:
    text.write(result)
print(result, '\n\n')