N = int(input("Введите ширину треугольника: "))
space = " "
row = 0
print("*" * N)

while N > 0:
    N -= 1
    row += 1
    print(space * row + ("*" * N))
