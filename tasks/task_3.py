number: int = int(input())
n: int = 100
count: int = 1

sum_num: int = 0

while count <= number:
    sum_num += count
    count += 1

    if sum_num > n:
        print('Сумма всех чисел в диапазоне от',
              1, 'до', number, 'больше ', n)
        break
else:
    print(sum_num)
