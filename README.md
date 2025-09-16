[summ3or5(V.Akim).py](https://github.com/user-attachments/files/22369277/summ3or5.V.Akim.py)def sum_multiples_of_3_or_5(number):
    # Если число отрицательное, возвращаем 0
    if number <= 0:
        return 0

    # Сумма чисел, кратных 3 или 5
    total_sum = 0

    # Проходим по числам от 1 до number - 1
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


# Ввод числа
number = int(input("Введите число: "))

# Вывод результата
print(sum_multiples_of_3_or_5(number))
[task gosti i mesta.py](https://github.com/user-attachments/files/22369278/task.gosti.i.mesta.py)
n = int(input())
numbers = input().split()
b = [0] * (n + 1)
for guest in range(1 , n+1):
 seat = int(numbers[guest + 1])
 b[seat] = guest
 numbers = n
print(numbers)
print(b)[task kalendar.py](https://github.com/user-attachments/files/22369280/task.kalendar.py)

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
    i +=1
[task 1.py](https://github.com/user-attachments/files/22369281/task.1.py)
a = int(input())
print("Distance in metters:",a*100)
[task 2.py](https://github.com/user-attachments/files/22369284/task.2.py)
print("введи расстояние в км:")

a = int(input())
print("введи расстояние в м:")

b = int(input())
c = a*1000
if c < b:
    print(c)
else:
    print(b)[task 3.py](https://github.com/user-attachments/files/22369286/task.3.py)
a = int(input())
for i in range(1, a+1):
     for j in range(i, i*a+1, i):
         print(j, end='\t')[task 4.py](https://github.com/user-attachments/files/22369287/task.4.py)
a = int(input())
b = int(input())
if b%a==0:
    print("является делитилем")
else:
    print("не является делителем")
     print()[task 5.py](https://github.com/user-attachments/files/22369293/task.5.py)
a = int(input())
print(a,"это число вы выбрали")[task 6.py](https://github.com/user-attachments/files/22369294/task.6.py)
m = int(input())
n = int(input())
if m>n:
    print("число m > n")
if n>m:
    print("число m < n")
else:
    print("числа равны")[task 7.py](https://github.com/user-attachments/files/22369295/task.7.py)
a = int(input())
b = 500 - a + 1
summ = b*(a+500)//2
print(summ)[task 8.py](https://github.com/user-attachments/files/22369297/task.8.py)
print("введите свое имя")
a = input()
print("Здравствуйте, ",a)[task 9.py](https://github.com/user-attachments/files/22369298/task.9.py)
a = int(input())
b = int(input())
c = int(input())
m = max(a,b,c)
print(m)[task 10.py](https://github.com/user-attachments/files/22369301/task.10.py)
a = int(input())
b = int(input())
c = a
a = b
b = c
print("a:",a,"b:",b)[task 11.py](https://github.com/user-attachments/files/22369305/task.11.py)
a = input().split()
b = min(a)
print(a.index(min(a)))[task 12.py](https://github.com/user-attachments/files/22369306/task.12.py)
a = int(input())
c = input("Перевести в байты (1) или килобайты (2): ")
def kb(n):
    s = n / 1024
    return s
def b(n):
    s = n * 1024
    return s
if c == "1":
    print("kb = ",a,"b = ",b(a))
if c == "2":
    print("b = ", a, "kb = ", kb(a))[task 13.py](https://github.com/user-attachments/files/22369307/task.13.py)
a = input("Введите свое имя: ")
b = int(input("Введите свой возраст: "))
c = 2025 - b + 100
print(a,"вам исполнится 100 лет  ",c," году")[task 15.py](https://github.com/user-attachments/files/22369310/task.15.py)
def f(month):
    if month == 2:
        return 28
    if month in [4,6,9,11]:
        return 30
    else:
        return 31

a = int(input("Введите номер месяца: "))
b = int(input("Введите год: "))
c = f(a)
print(c)[task 16.py](https://github.com/user-attachments/files/22369312/task.16.py)
a = int(input())
n = input().split()

b = [0]*(n+1)

for g in range(1,n+1):
    seat = int(n[g - 1])
    b[seat] = g
print(n)
print(b[1:])[task_cherepasgki(V.Akim).py](https://github.com/user-attachments/files/22369316/task_cherepasgki.V.Akim.py)
from math import *
v1 = int(input("Скорость первой черепахи "))
v2 = int(input("Скорость второй черепахи "))
g = int(input("фора "))
t = g/(v2-v1)
hours = int(t)
minuts = (t - int(t))*60
minn = int(minuts)
sek = (minuts - minn)*60
sek = floor(sek)
print(hours)
print(min)
print(sek)
