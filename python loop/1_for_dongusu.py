#for dizi elemanlarını yazdırmak için kullanılır(?)

#dizi tanımlama
numbers=[1,2,3,4,5,6]

#for döngüsüyle liste elemanlarını ekrana yazdırma
for number in numbers:
    print(number)

#dizi elemanları sayısı kadar döngü döner
for a in numbers:
    print("Hello World")#ekrana 6 tane 'Hello World' yazdırıcak


#yeni dizi tanımlama
names=['çınar','ali','efe']

#dizi elemanları for kullanarak ekrana yazdırma 
for name in names :
    print(f"My name is {names}")

#----------------------------------------------------------------------------------------------------

#eğer dizi olarak bir string ifadenin elemanlarını yazdırmak istersek
string_dizi="Gamze Aslan"
for karakter in string_dizi:
    print(karakter)

#----------------------------------------------------------------------------------------------------
#eğer dizinin elemanları birden fazla karakterden oluşuyorsa ve bu karakterleri ayrı ayrı ekrana yazdırmak istersek
tuple=[(1,2),(2,3),(3,4),(4,5)]
for number in tuple:
    print(number)#(1,2)\n(2,3)... şeklinde çıktı üretti

#elemanların 1.elemanı
for number_1,number_2 in tuple:
    print(number_1)

#elemanların 2.elemanı    
for number_1,number_2 in tuple:
    print(number_2)    

#elemanların 1 ve 2.elemanı fakat ayrı ayrı 
for number_1,number_2 in tuple:
    print(number_1,number_2)

#----------------------------------------------------------------------------------------------------

#eğer dic listeleri for döngüsüyle yazdırırdak key ve value değerlerini berabaer mi yazdırır ya da key ve value değerlerini ayrı ayrı yazdırmak istersek 

#dic list e tanımlıyalım
dic_list={'personel1':'Ahmet','personel2':'ali','personel3':'ayşe','personel4':'fatma'}

for char in dic_list:
    print(char)

print()

for key,value in dic_list.items():#items metodu kulanılmadığında çıktı üretmez bu kod bloku
    print(key)

print()

for key,value in dic_list.items():
    print(value)