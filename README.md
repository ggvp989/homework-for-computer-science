[task 1.py](https://github.com/user-attachments/files/22364732/task.1.py)a = int(input())
print("Distance in metters:",a*100)

[task 2.py](https://github.com/user-attachments/files/22364734/task.2.py)
print("введи расстояние в км:")

a = int(input())
print("введи расстояние в м:")

b = int(input())
c = a*1000
if c < b:
    print(c)
else:
    print(b)[task 3.py](https://github.com/user-attachments/files/22364736/task.3.py)
a = int(input())
for i in range(1, a+1):
     for j in range(i, i*a+1, i):
         print(j, end='\t')
     print()[task 4.py](https://github.com/user-attachments/files/22364740/task.4.py)
a = int(input())
b = int(input())
if b%a==0:
    print("является делитилем")
else:
    print("не является делителем")[task 5.py](https://github.com/user-attachments/files/22364744/task.5.py)
a = int(input())
print(a,"это число вы выбрали")[task 6.py](https://github.com/user-attachments/files/22364752/task.6.py)
m = int(input())
n = int(input())
if m>n:
    print("число m > n")
if n>m:
    print("число m < n")
else:[task 7.py](https://github.com/user-attachments/files/22364755/task.7.py)
a = int(input())
b = 500 - a + 1
summ = b*(a+500)//2
print(summ)
    print("числа равны")[task 8.py](https://github.com/user-attachments/files/22364756/task.8.py)
print("введите свое имя")
a = input()[task 9.py](https://github.com/user-attachments/files/22364761/task.9.py)
a = int(input())
b = int(input())
c = int(input())
m = max(a,b,c)
print(m)
print("Здравствуйте, ",a)[task gosti i mesta.py](https://github.com/user-attachments/files/22364762/task.gosti.i.mesta.py)
[task kalendar.py](https://github.com/user-attachments/files/22364764/task.kalendar.py)

a = int(input("день - "))
k = int(input("количесство дней - "))
day = 1
for i in range (1,a) :
    print("   ", end = "")
i = a
while day<=k:
    if day<=10:
        print (f" {day}", end = "")
    else:
        print (f"{day}", end = "")
    if i%7==0 or day==k:
        print ()
    else:
        print ("  ", end = "")
    day +=1
    i +=1[task_cherepasgki(V.Akim).py](https://github.com/user-attachments/files/22364766/task_cherepasgki.V.Akim.py)
v1 = int(input())
v2 = int(input())
g = int(input())
if v1 >= v2 :
    print("null")
else:
    t= g/(v2 - v1)
    ts= t * 3600
    tm= ts *60
    th= ts* 3600
    ts= ts
print(")
