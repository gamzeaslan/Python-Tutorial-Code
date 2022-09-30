x,y,z=2,5,10
#1-->Kullanıcıdan aldığımız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
#kullanıcıdan 2 sayı alma
number_1=int(input("1.sayı= "))
number_2=int(input("2.sayı= "))
carpim=number_1*number_2
toplam=x+y+z
fark=carpim-toplam
print(f"çarpım-toplam={fark}\n")

#--------------------------------

#2-->y'nin x'e kalansız bölümünü hesaplayınız
kalansiz_bolum=y//x
print(f"Kalansiz bölüm:{kalansiz_bolum}\n")

#--------------------------------

#3-->(x,y,z) toplamının mod 3'ü nedir?
toplam_mod=toplam%3
print(f"Toplamın 3 e göre modu:{toplam_mod}\n")

#--------------------------------
#4-->y'nin x.kuvvetini hesaplayınız
kuvvet=y**x
print(f"y nin x.kuvveti:{kuvvet}\n")

#--------------------------------
#5-->x,*y,z=numbers işlemine göre y nin değerleri toplamı
numbers=1,5,7,10,6
x,*y,z=numbers
print(x,y,z)#1,[5,7,10],6
toplam=y[0]+y[1]+y[2]
print(f"y nin elemanları toplamı:{toplam}\n")
 
#--------------------------------
#6-->x,*y,z=numbers işlemine göre z'nin küpü kaçtır
print(f"z nin küpü:{z**3}\n")