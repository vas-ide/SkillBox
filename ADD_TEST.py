

lst = [6, 24, 19, 8, 18, 24, 23]
lst_upd = [23, 24, 18, 8, 19, 24, 6]
tottal = 0
for i in lst:
    if tottal == 0:
        tottal += i
    else:
        tottal += 26 ** i
print(tottal)
print((6*26**6)+(24*26**5)+(19*26**4)+(8*26**3)+(18*26**2)+(24*26)+23)