import json
# Подсчитать общую сумму расходов


import json
with open("task_1.json", encoding='utf-8') as file:
    data = json.load(file)
    print(data)

total_sum = sum([i['сумма'] for i in data])
print(f"Сумма всех затрат составила {total_sum} рублей")

# Найти категорию на которую было потрачено больше всего денег.

new_data = {}
for i in data:
    if i['категория'] not in new_data:
        new_data[i['категория']] = i['сумма']
    else:
        new_data[i['категория']] += i['сумма']
        name_max_category = max(new_data, key=new_data.get)
        max_category = new_data[name_max_category]
print(f"Максимальные затраты в категории '{name_max_category}' на сумму {max_category}")

# Найти самый дорогой день

from collections import defaultdict
days = defaultdict(int)
for i in data:
    days[i['дата']] += i['сумма']
max_day = max(days, key=days.get)
print(f"Самый дорогой день: {max_day} на сумму {days[max_day]}")
