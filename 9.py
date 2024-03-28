x1, y1, r1, x2, y2, r2 = map(int, input().split())
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
if d > r1 + r2:
    print("Окружности лежат одна вне другой, не касаясь")
elif d == r1 + r2:
    print("Окружности имеют внешнее касание")
elif d < r1 + r2:
    if d + min(r1, r2) == max(r1, r2):
        print("Окружности имеют внутреннее касание")
    elif d < abs(r1 - r2):
        print("Одна окружность лежит внутри другой, не касаясь")
    else:
        print("Окружности пересекаются")
