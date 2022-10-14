def f(x):
    max_i=0
    for i in x:
        if i > max_i:
            max_i=i
    return max_i
    
print('Введите кол-во элементов в массиве')
cnt=int(input()) 
a=[0]*cnt
print('Вводите элементы массива')
for i in range (cnt):
    a[i]=float(input())
    
index_max_i=a.index(f(a))
print("Максимальный элемент массива а =",a[index_max_i])
for j in range (index_max_i+1,cnt):
    a[j]=0
print(a)

