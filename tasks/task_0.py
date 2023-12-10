count: int = 0
count_otr: int = 0
number_count: int = 0

while True:
    user_input = int(input())

    if user_input > 0:
        number_count += user_input
    elif user_input < 0:
        count_otr += user_input
        count += 1
    if count >= 3:
        break

print('Сумма положительных чисел:',number_count)
print('Сумма отрицательных чисел:', count_otr)
