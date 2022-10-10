#burada herhangi bir fonksiyona başka bir fonksiyonu özellik olarak nasıl ekleyebileceğimizi göreceğiz

#fonksiyon içinde fonksiyon tanımalaması
def outer(func):
    def inner(name):
        print("fonk öncesi")
        func(name)
        print("fonksiyon sonrası")
    return inner(input("Name: "))#parametreli fonk eklenirken parametre ataması inner fonk return edilirken gerçekleştirilir

# #eklenicek fonksiyon
# def sayHello():
#     print("Hello")        

# #ekleme işlemi
# sayHello=outer(sayHello)
# print(sayHello)

#eğer eklemek istediğimiz fonksiyon parametre alıyorsa

#paramatreli eklenilecek fonksiyon
def nameHello(name):
    print(f"Hello {name}")

#ekleme işlemi
nameHello=outer(nameHello)



"""Fonksiyona fonksiyonu özellik olarak ekleme ile ilgili başka bir örnek"""
import time
def outer(func):
    def inner(*args_1, **args_2):#iki tane tuple parametresine izin vermiyor bu yüzden 1 tuple bir de dic parametre girişi alındı 
        start=time.time()
        time.sleep(1)
        func(*args_1,**args_2)
        finish=time.time()
        print(f"fonk adı:{func.__name__} ve işlem süresi:{finish-start}")
    return inner    

import math
#addition---->fonksiyonları eklemek için daha kısa bir yol var o da 
@outer
def usAlma(taban,kuvvet):
    print(math.pow(taban,kuvvet))

@outer
def faktoriyel(number):
    print(math.factorial(number))

print(usAlma(2,3))
print(faktoriyel(5))