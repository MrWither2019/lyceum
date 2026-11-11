
counts = [0] * 1001
total_numbers = 0

print("Вводите последовательность чисел (0 — конец):")

while True:
    num = int(input())
    if num == 0:
        break
    if 1 <= num <= 1000:
        counts[num] += 1
        total_numbers += 1

X_received = int(input("Введите полученное контрольное значение: "))

X_calculated = 0

unique_numbers = []
for i in range(1, 1001):
    if counts[i] > 0:
        unique_numbers = unique_numbers + [i]

for i in range(len(unique_numbers)):
    a = unique_numbers[i]

    if counts[a] >= 2:
        product = a * a
        if product % 10 == 0 and product > X_calculated:
            X_calculated = product

    for j in range(i + 1, len(unique_numbers)):
        b = unique_numbers[j]
        product = a * b
        if product % 10 == 0 and product > X_calculated:
            X_calculated = product

print(f"Получено {total_numbers} чисел")
print(f"Полученное контрольное значение: {X_received}")
print(f"Вычисленное контрольное значение: {X_calculated}")

if X_received == X_calculated and X_calculated > 0:
    print("Контроль пройден")
else:
    print("Контроль не пройден")