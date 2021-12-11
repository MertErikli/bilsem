#kullanıcıdan 10 sayı isteyerek bunları bir listeye atıp küçükten büyüğe sıralayınız
sayilar=[]
for i in range(10):
    sayi=int(input("10 sayı giriniz"))
    sayilar.append(sayi)
sayilar.sort()
print(sayilar)
siralama=input("A-Z, Z-A")
if siralama=="A-Z":
    sayilar.sort()
    print(sayilar)
elif siralama=="Z-A":
    sayilar.sort()
    print(sayilar)
else:
    print("Hatalı giriş")
