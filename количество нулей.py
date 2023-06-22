n=int(input('Введите количество чисел'))
zero=0
for i in range(n):
    a=int(input())
    if a==0:
        zero+=1
print('количество нулей',zero)
               
