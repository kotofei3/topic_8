print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

user_name: str = input("введите свое имя:")
user_name_2: str = input("введите свое имя:")


while True:
    a = user_name
    b = user_name_2
    a = input("Анна:")
    b = input("Макс:")
    if a == "бумага" and b == "камень":
        print("Поздравляем! Победитель - Анна!")
        answer = input("Хотите сыграть еще раз? (да/нет):")
        if answer == "нет":
            break
    elif a == "камень" and b == "камень":
        print("Ничья! Продолжайте играть")

    elif a == "бумага" and b == "ножницы":
        print("Поздравляем! Победитель - Макс!")

    elif a == "ножницы" and b == "бумага":
        print("Поздравляем! Победитель - Анна!")
