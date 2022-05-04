# Можно писать код под каждым заданием

# 1) при помощи for вывести на экран числа от -100 до 100 (включительно)

for number in range(-100, 101):
    print(number)


# 2) при помощи while вывести на экран числа от -25 до 120 (включительно)

 x = -25
 while x < 121:
    print(x)
    x += 1

# 3) при помощи for вывести на экран
# только четные числа от 2 до 20 (включительно), использовать continue
for item in range(1, 22):
    if item % 2 != 0:
        item += 1
        continue
    if item % 2 == 0:
        print(item)


# 4) при помощи while вывести на экран
# только нечетные числа от 3 до 30 (включительно), использовать continue

x = 3
while x < 31:
    if x % 3 != 0:
        x += 1
        continue
    if x % 3 == 0:
        print(x)
        x += 1


# 5) создать лист с пятью именами, при помощи for пройтись
# по списку и сделать break на имени Ivan (сделать так, чтобы это имя было не в конце)

names = ["Masha", "Gosha", "Ivan", "Dasha", "Vova"]
for name in names:
    print(name)
    if name == "Ivan":
        break

# 6) при помощи while бесконечно просить пользователя вводить числа
# и выйти из цикла при помощи break только если пользователь ввёл 13
# не получилось((

# 7) использая двойной for и 2 листа adjectives, nouns (добавить по 4 штуки в каждый)
# вывести на экран каждое существительное со всеми прилагательными

adjectives = ["pretty", "ugly", "nice", "gorgeous"]
nouns = ["dress", "trousers", "shorts", "shirt"]

for adjective in adjectives:
    for noun in nouns:
        print(adjective + " " + noun)
