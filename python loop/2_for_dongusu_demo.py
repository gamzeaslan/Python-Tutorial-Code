#liste tanımlama
sayilar=[1,3,5,7,9,12,19,21]

#1-->Sayılar listesindeki hangi sayılar 3 ün katıdır?
for sayi in sayilar:
    if(sayi%3==0):
        print(f"3 ün katı sayılar:{sayi}")

print()

#2-->Sayılar listesinde sayıların toplamı kaçtır
toplam=0
for sayi in sayilar:
    toplam +=sayi
print(f"Sayıların toplamı:{toplam}")

print()

#3-->Sayilar listesindeki tek sayıların karesini alınız
for sayi in sayilar:
    if(sayi%2==1):
        print(f"{sayi} karesi:{sayi**2}")

print()

#yeni dizi tanımlama
sehirler=['kocaeli','istanbul','ankara','izmir','rize']

#4-->Şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if(len(sehir)<=5):
        print(f"en fazla 5 karakterli şehirler:{sehir}")

print()

#yeni liste tanımlama
urunler=[
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]

#5-->Ürünlerin fiyatları toplamı
toplam=0
for urun in urunler:
    print(urun)

for urun in urunler:
    toplam+=int(urun['price'])
    
print(f"Ürünlerin fiyatları toplamı: {toplam}")

print()

#6-->Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(f"fiyatı max 5000 olan ürünler: {urun['name']}")

print()