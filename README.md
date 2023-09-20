# Лабораторна робота групи 11КН Куку Вадимa Ярославовичa (За списком №7)

* Завдання №1, файл Lab1.py: Скласти програму, яка б додавала, віднімала, множила та ділила два числа. Передбачити вивід результату на екран.

  Я написав калькулятор з умовами if else 

  Детальніше як працює калькулятор:
  Розподіляю код по частинам

```python
num_a = int(input("Enter first num: ")) 
num_b = int(input("Enter second num: "))

operator = input("enter operator: + - *(to multiply) /(divide) ")
```

Я стаорив три оператора, перші вда оператора він простить у користувача аби він написав числа. Друга змінна просить увести математичні оператори (+, -, *, /)

+ ' * ' помножити
+ ' / ' поділити

Далі частина з умовами if else

```python
if operator == '+':
    print(num_a + num_b)
if operator == '-':
    print(num_a - num_b)
if operator == '*':
    print(num_a * num_b)
if operator == '/':
    print(num_a / num_b)
```

Коли користувач увів якийсь математичний оператор наприклад +, то програма додає перше число(num_a) додається з другим числом(num_b), і так з іншими операторами

![](images/Screenshot%20from%202023-09-20%2010-36-47.png)

---

* Завдання №2, файл Lab_2.py: математична задача

$$
у = arctg(a/d) + (b + d)2 a=75; b=4.5; c=6.2; d=5;
$$

Як прцює програма, зновуже розбираємо код по частинам, на цей раз щось новеньке

```python
import math
```

Програма працює за допомогою бібліотеки math (це стандартна бібліотека python'а)

```python
a = 75
b = 4.5
c = 6.2
d = 5
```

Далі додали чотири змінни де а = 75, b = 4.5, c = 6.2, d = 5

```python
result = math.atan(a / d) + (b + d) ** 2
```

далі додали змінну result де ми розв'язує за допомогою функції бібліотеки math, atan(арктангенс) щоб обчислити арктангенс виразу a/d, Арктангенс (також відомий як обернена тангенс) обчислює обернену функцію тангенсу. Після цього програма обчислює b + d, додаючи значення b і d. Знаходить квадрат отриманої суми, (b + d)^2 (у квадраті).

Нарешті, вона додає результати обчислень арктангенсу та квадрату досягнутого раніше і виводить фінальний результат.

## Як вирішити цю задачу математичним способом: 

$$
a = 75

b = 4.5

c = 6.2

d = 5
$$

Потрібно обчислити вираз:

$$
у = arctan(a/d) + (b + d)^2
$$

Обчислімо arctan(a / d):

$$
arctan(a/d) = arctan(75/5) = arctan(15)
$$

Обчислімо (b + d)^2:

$$
(b + d)^2 = (4.5 + 5)^2 = (9.5)^2 = 90.25
$$

Додамо обидва обчислені значення:

$$
у = arctan(15) + 90.25
$$

Тепер обчислімо суму:

$$
у ≈ 1.32581766 + 90.25 ≈ 91.57581766
$$

Отже, значення виразу у близько дорівнює 91.5758 (з округленням до чотирьох знаків після коми)

---
* Завдання №3 файл Lab_3.py: 
  Два автомобілі виїхали одночасно в різних напрямках з пункту А. Перший - зі швидкістю V1 км/год., а другий - V2 км/год. Складіть програму для визначення відстані між ними через дві години, якщо перший зробив дві зупинки по 20 хв., а другий - одну десятихвилинну зупинку.

В цій програму трохи більше змін но не суть важна,

```python
V1 = float(input("Введіть швидкість першого автомобіля (км/год): "))
V2 = float(input("Введіть швидкість другого автомобіля (км/год): "))

stop1_count = int(input("Введіть кількість зупинок першого автомобіля: "))

stop2_count = int(input("Введіть кількість зупинок другого автомобіля: "))

stop1_duration = 20
stop2_duration = 10

distance1 = (V1 * 2)
distance2 = (V2 * 2)

stop1_total_duration = stop1_count * stop1_duration
stop2_total_duration = stop2_count * stop2_duration

distance1 += (stop1_total_duration / 60) * V1
distance2 += (stop2_total_duration / 60) * V2

distance_between = abs(distance1 - distance2)
```

Я розумію дуже багато змін і може можна було зробити програму май помкншою но що є то є, розбираємо по частинам

```python
V1 = float(input("Введіть швидкість першого автомобіля (км/год): "))

V2 = float(input("Введіть швидкість другого автомобіля (км/год): "))
```
Дві змінні просять ввести швидкість двох автівок в кіломтри на годину, (Якщо не зрозуміло V - Vehicle, V1, V2 - це типу Vehicle1 та Vehicle2) 

```python
stop1_count = int(input("Введіть кількість зупинок першого автомобіля: "))

stop2_count = int(input("Введіть кількість зупинок другого автомобіля: "))
```

Далі програма простить увасти коритувача кількість зупинок першого автомобіля та другого

```python
stop1_duration = 20

stop2_duration = 10
```
Змінни кажуть про тривалість кожної зупинки в хвилинах

```python 
stop1_total_duration = stop1_count * stop1_duration
stop2_total_duration = stop2_count * stop2_duration
```
Далі ця частина коду розраховує загальну тривалость зупинок для кожного автомобіля

```python
distance1 += (stop1_total_duration / 60) * V1
distance2 += (stop2_total_duration / 60) * V2
```

Ця частина рахує додавання часу зупинок до відстаней

```python
distance_between = abs(distance1 - distance2)
```
Ця частина коду обчислює відстань між автомобілями

```python
print(f"Відстань між автомобілями після 2 годин руху та зупинок: {distance_between} км")
```
виводить результата і це все

---
* Завдання №4 файл Lab_4.py: Турист пройшов 8 маршрутів. Три маршрути довжиною по R км, K маршрутів - по R1 км 800 м, а інші по R3 км R2 м. Складіть програму за допомогою якого можна визначити, яку відстань пройшов турист по всіх маршрутах разом. 

```python
R = float(input("Введіть довжину маршрутів типу R (км): "))
R1 = 1.8
R2 = float(input("Введіть довжину маршрутів типу R2 (км): "))

K = int(input("Введіть кількість маршрутів типу R2: "))

R3 = float(input("Введіть довжину маршрутів типу R3 (км): "))
```

Що я наробив, пояснюю: Змінні R R1 R1 R2 та К <br> R, R2, R3 - Довжинна маршруту, К - кількість маршрутів, R1 - це відстань (1 кілометр 800 метрів)


```python
total_distance = 3 * R + K * R1 + R2 * R3
```
Обчислює загальну відстань

```python
print(f"Загальна відстань, пройдена туристом, становить {total_distance} км")
```
Виводить результат

---
# Дякую вам за увагу, і хочу казати що я математичну задачу зробив через ChatGPT що за це вибачаюсь я не настільки розумний
