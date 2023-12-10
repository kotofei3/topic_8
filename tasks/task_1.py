data_types = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]
# for i in data_types:
#     if type(i) != float and type(i) != str:
#         print('Элемент:', i, type(i))


for i in data_types:
    if not isinstance(i, (float, str)):
        print('Элемент:', i, type(i))
