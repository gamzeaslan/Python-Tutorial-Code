#random modulünün import edilmesi
import random

#random doc erişim:
value=dir(random)
print(value)

value=help(random)
print(value)

#random modulündeki bileşenlerin kullanımı
value=random.random()#0.0 -1.0 arasında rastgele bir float değeri değişkene atar
print(value)

print()

value=random.random()*100#0.0-100.0 arasında rastgele float bir değeri değişkene atar
print(value)

print()

value=int(random.uniform(10,100))#10-100 arasındaki int değerlerden rastgele bir int değeri değişkene atar
print(value)

print()

value=random.randint(1,200)#yukarıdaki gibi int değerine dönüştürmek yerine direkt 1 ile 200 arasında ürettiği rastgele sayıyı değişkene atar
print(value)

print()

names=["ayşe","fatma","nur","gül"]
value=names[random.randint(0,len(names)-1)]#bu şekilde names listesi içerinden rasgele bir eleman değişkene atanır
print(value)

print()

value=random.choice(names)
print(value)

my_string="Hello World"
value=random.choice(my_string)
print(value)

print()
print()

liste=list(range(10))#şeklinde bir liste oluşturuldu
random.shuffle(liste)#bu şeklide liste elemanları rastgele bir şekilde dizilir
print(value)

print()

liste=range(100)
value=random.sample(liste,3)#ile liste adlı liste içerisinden rastgele 3 eleman seçilir ve value değerine atanır 
print(value)
print()