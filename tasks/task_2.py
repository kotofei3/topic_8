numbers: list = ["21", "85", "150", "190", "135", "515", "80"]

for i in numbers:

    res = int(i)
    if res > 500:
        break
    elif res > 150:
        continue
    if res % 5 == 0:
        print(res)
