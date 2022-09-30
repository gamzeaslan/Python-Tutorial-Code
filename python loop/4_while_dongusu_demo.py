#liste tanımlama
sayilar=[1,3,5,7,9,12,19,21]

#1-->Sayılar listesini while ile ekrana yazdırın
number=len(sayilar)
number-=1
while (number>=0):
    print(f"{number+1}.eleman:{sayilar[number]}")
    number-=1

print()

#2-->Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
baslangic=int(input("Başlangıç değeri: "))
bitis=int(input("bitiş değeri: "))
while (baslangic <=bitis):
    if(baslangic %2==1):
        print(baslangic)
    baslangic+=1    
    
print()

#3-->1-100 arasındaki sayıları azalan şeklide yazdırın
number=100
while(number>=1):
    print(number)
    number-=1

print()

#4-->Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
# number_1=int(input("1.sayı: "))
# number_2=int(input("2.sayı: "))
# number_3=int(input("3.sayı: "))
# number_4=int(input("4.sayı: "))
# number_5=int(input("5.sayı: "))
numbers=[]
i=0
while(i<5):
    numbers.append(int(input("sayı: ")))#IndexError: list assignment index out of range in Python hata mesajı:listede olmayan bir dizine bir değer atamaya çalıştığımızda ortaya çıkar. 
    i+=1

i=0
while(i<5):
    print(numbers[i])
    i+=1
 
    

print()
#5-->kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız 
#****Ürün sayısını kullanıcıya sorun
#****dictionary listesi yapısı (name,price)
#****ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin
urun_sayisi=int(input("ürün sayısı: "))
i=1
dic=[]
while (i<=urun_sayisi):
    name=input("ürün ismi: ")
    price=input("ürün fiyatı: ")
    dic.append({
        'name':name,
        'price':price}
      )
    i+=1  

for urun in dic:
    print(f"ürün adı:{urun['name']}\n urun fiyatı:{urun['price']}")

