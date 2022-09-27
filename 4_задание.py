print("Введите строку: ")
S=str(input())
S1=S.split()
Zn=str(input("Введите слово для поиска: "))
i=0
for sl in S1:
    if(sl==Zn):
        print("Индекс: "+str(i)+ " >>- " + str(sl))
    i+=1