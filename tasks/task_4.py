number: int = int(input(':'))

if number > 0:

    for i in range(2, number):
        if number % i == 0:
            print('Число', number, 'не является простым')
            break
    else:
        print('Число', number, 'является простым')
else:
    print('Число должно быть положительным')

# number: int = int(input('Введите число: '))
#
# small_prime: int = 2
# if number > 0:
#
#     while small_prime < number:
#
#         if number % small_prime == 0:
#             print('Число', number, 'не является простым')
#             break
#         small_prime += 1
#     else:
#         print('Число', number, 'является простым')
# else:
#     print('Число должно быть положительным')

# small_prime: int = 2
# if number > 0:
#
#     while small_prime < number ** 0.5:
#
#         if number % small_prime == 0:
#             print('не является')
#             break
#         small_prime += 1
#     else:
#         print('простым')
# else:
#     print('Число должно быть положительным')
