my_list = []
for x in range(50, 101):
    my_list.append(str(x) + " years")

for x in my_list:
    print(x)

colors = ["red", "green", "blue"]
birds = ["parrot", "sparrow", "duck"]
for color in colors:
    for bird in birds:
        print(color + " " + bird)
