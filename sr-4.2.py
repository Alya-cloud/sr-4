print('Ввести размерность массива А')
cnt_a=int(input())
A=[0]*cnt_a
print('Вводить элементы массива А')
for i in range (cnt_a):
    A[i]=float(input())
    
print('Ввести размерность массива B')
cnt_b=int(input())
B=[0]*cnt_b
print('Вводить элементы массива B')
for j in range (cnt_b):
    B[j]=float(input())


    
ravn=[]
for k in A:
    for n in B:
        if k==n:
            ravn.append(k)
ravn=set(ravn)
print(ravn)
    
    
