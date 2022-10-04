#mevcut dosyaya math modulünün entegrasyonu

import math

#artık math modülüne ait tüm değişkenler ,fonksiyonlar ve metotlar bu proje içerisinde kullanılabilir

"""Eğer math metodunu proje içerinde daha kolay bir ifade ile çağırmak istersek:"""
#import math as islem
#islem.sqrt(36)


#math modulünün yardım dökümantasyonlarına ve mevcut metotlarına erişim için:
value=dir(math)
print(value)

value=help(math)
print(value)

value=help(math.sqrt)#sadece sqrt için doc verir
print(value)


print()
print()

#math modulünün diğer bileşenlerine erişmek için:
value=math.sqrt(36)
print(value)

value=math.factorial(6)
print(value)

value=math.floor(5.9)
print(value)

value=math.ceil(5.9)
print(value)


#math modülünün tüm bileşenlerini import etmek için:from math import* ifadesi kullanılır(2.yöntem)

#eğer math modulundaki belli birkaç şeyi projemizde kullanıcak ise:
#from math import factorial,sqrt,ceil 
