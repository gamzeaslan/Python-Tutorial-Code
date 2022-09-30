#1-->ptyhon da kulanıcı girişi:input(açıklama ifadesi) şeklinde yazılır

#2-->python ve c# da inputtan girilen bir değer otomatik olarak string olarak kabul edilir

#3-->eğer giirlen değer üzerinde herhangi bir  matematiksel işlem gerçekleştirmek istiyorsak tür dönüşümü yapmalıyız

#4-->Python da herhangi bir değişkenin türünü ekrana yazdırmak için :print(type(değişkenin adı))  şeklinde yazılır 

#-----------TÜR DÖNÜŞÜMLERİ(TYPE CONVERSION)-------------

#kullanıcı girişi--
from turtle import st
from xmlrpc.client import boolean


kullanici_girisi=input("kullanıcı girişi: ")

#kullanıcı tarafından girilen değerin veri tipini bulma
print(type(kullanici_girisi))#string(str) tipindedir
print()

#---------------string to int(stringden int e dönüşüm)---------------
string_degisken="12"
string_to_int_donusumu=int(string_degisken)#stringden int e tür dönüşümü
#ekrana yazdırma
print("string-->int:",string_to_int_donusumu)
#veri tipini ekrana yazdırma
print(type(string_to_int_donusumu))
print()


#---------------int to string(str)---------------
int_degisken=10
int_to_string_donusum=str(int_degisken)
#ekrana yazdırma
print("int-->string:",int_to_string_donusum)
#veri tipini ekrana yazdırma
print(type(int_to_string_donusum))
print()


#---------------int to float---------------
int_to_float_donusum=float(int_degisken)
#ekrana yazdırma
print("int-->float:",int_to_float_donusum)
#veri tipini ekrana yazdırma 
print(type(int_to_float_donusum))
print()

#---------------float to int---------------Dönüşüm yuvarlamayla mı yoksa sadece tam kısmın alınmasıyla mı yapılıyor--->tam kısımla dönüşüm yapılır

float_degisken_1=12.3
float_degisken_2=12.8
#tür dönüşümü
float_to_int_donusum_1=int(float_degisken_1)
float_to_int_donusum_2=int(float_degisken_2)
#ekrana yazdırma
print("float-->int -tama yakın dönüşüm:",float_to_int_donusum_1)
print("float-->int-bir fazlasına yakın dönüşüm:",float_to_int_donusum_2)
#veri tipini ekrana yazdırma
print(type(float_degisken_1))
print(type(float_degisken_2))
print()


#---------------boolean to string---------------
#değişken tanımlama
boolean_degisken=True
#tür dönüşümü
boolean_to_string_donusum=str(boolean_degisken)
#ekrana yazdırma
print("boolean-->string:",boolean_to_string_donusum)
#veri tipini yazdırma
print(type(boolean_to_string_donusum))
print()


#---------------boolean to int---------------true:1 // false:0
#tür dönüşümü
boolean_to_int_donusum=int(boolean_degisken)
#ekrana yazdırma
print("boolean-->int :",boolean_to_int_donusum)
#veri tipini ekrana yazdırma
print(type(boolean_to_int_donusum))
print()






 


