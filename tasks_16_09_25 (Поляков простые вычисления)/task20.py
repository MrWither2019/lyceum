print("ведите стоимость в рублях и копейках через запятую")
rub, cop = map(int, input().split(","))
print("ведите число пирожков")
num = int(input())
rub = rub * num + (cop * num // 100)
cop = (cop*num) % 100
print(f"Итоговая стоимость: {rub} рублей, {cop} копеек")

