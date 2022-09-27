S=str(input("Введите строку: "))
rez=max(S.split(";"),key=len)
print(rez)