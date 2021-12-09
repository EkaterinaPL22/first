figure_name = input("введи фигуру(прямоугольник/треугольник/круг):")
while figure_name != "прямоугольник" and figure_name != "треугольник" and figure_name != "круг":
    figure_name = input("введи фигуру(прямоугольник/треугольник/круг):")

if figure_name == "прямоугольник":
    leng = int(input("введи длину:"))
    while leng <= 0:
        leng = int(input("введи длину:"))
    wid = int(input("введи ширину:"))
    while wid <= 0:
         wid = int(input("введи ширину:"))
    print(2*leng+wid*2)
elif figure_name == "треугольник":
    leng = int(input("введи длину:"))
    while leng <= 0:
        leng = int(input("введи длину:"))
    print(3*leng)
elif figure_name == "круг":
    rad = int(input("введи радиус:"))
    while rad <= 0:
        rad = int(input("введи радиус:"))
    print(2*rad)
