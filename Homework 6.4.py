N = int(input("Введите ширину треугольника: "))
row = 1
space = " "
symbol = "*"

while 0 < N:
    E = N - 1
    print(space * E + symbol * row)
    N -= 1
    row += 1
