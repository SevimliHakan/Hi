yazar="Hakan"
ugurlusayi1="8"
ugurlusayi2="7"
ugurlusayi1sayi=int(ugurlusayi1)
ugurlusayi2sayi=int(ugurlusayi2)
ugurlusayitoplami=ugurlusayi1sayi+ugurlusayi2sayi
#int=say� str=yaz� print(type(d�td�td�t))=d�td�td�t int or str

ugurlusayitoplamiyaziIle=str(ugurlusayitoplami)

#bir�eyi = ile onu farkl� bir�ey olarak i�aretlersen +farkl� bir�ey dersen oto bir�ey yazar
print("hey")
print("Hello "+yazar+" !")
print("")
# print comudu ekrana yazar
print(yazar+"\'in ugurlu sayisi "+ ugurlusayi1 +"\n iki sayinin toplami "+ugurlusayitoplamiyaziIle )



print("Hakan\'in defteri. \nBu da ikinci satir")#\ alt gr  ./, gibi �eyleri yazmam�z� sa�lar
print("\\")
 

#=yazma=uygulama

#\n=new line=alt satuir


isim=input("lutfen adinizi giriniz ")
a=input("Lutfen bir rakam giriniz")
b=input("Lutfen bir rakam daha giriniz")
a2=int(a)
b2=int(b)
c2=a2+b2
c=str(c2)
d=a2*b2
d2=str(d)
e=a2//b2
e3=str(e)
f=a2%b2
f2=str(f)
print("")
print("girilen isim "+isim)
print("girilen rakamlarin toplami "+c)
print("girilen rakamlarin carpimi "+d2)
print("girilen rakamlarin bolumu "+e3)
print("girilen rakamlarin kalani "+f2)
#input=al input ile yap�lacak �ey inpoutdan once olamaz   *=�arpma
#float=k�s�rl� say� /=b�lme %=kalan //= floatsuz b�l�m
