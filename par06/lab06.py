#1
from math import *
from random import randint
from statistics import *
from datetime import date

radius = int(input("Radius: "))
kat1 = float(input("Katety: "))
kat2 = float(input("Katety: "))
item = int(input("Item: "))
inu = int(input("In upacovka: "))


S = pi * radius

gip =(kat1**2) + (kat2**2)


print(f'Потрібно упаковок:{ceil(item/inu)}')
print(f'Гіпотенуза: {ceil(sqrt(gip))}')
print(f'Площа: {ceil(S)}')


#2
N = int(input("Кількість:"))

grade = []
for i in range(N):
    grade.append(randint(1, 12))

count_above_10 = sum(1 for g in grade if g >= 10)

print(grade)
print(f'Середній бал: {mean(grade)}')
print(f'Медіана: {median(grade)}')
print(f'Мінімальне: {min(grade)}')
print(f'Максимальне: {max(grade)}')
print(f'Кількість оцінок більше 10: {count_above_10}')

#3
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

event_date = date(year, month, day)
today = date.today()
dl = event_date - today

if dl.days > 0:
    print(f"До події залишилось: {dl.days} днів")
elif dl.days == 0:
    print(f"Після події минуло: {-dl.days}")
else:
    print("Сьогодні дата події!")

