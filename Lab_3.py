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

print(f"Відстань між автомобілями після 2 годин руху та зупинок: {distance_between} км")