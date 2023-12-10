n = 3
number = 1 # - № дерева
# - бесконечный лес
while True:
    # - числа из нашего рюкзака
    for i in range(1, n + 1):
       if number % i != 0:
           break
    else:
        print(number)
        break
    number += 1 # - переходим к следующиму дереву
