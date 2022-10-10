# #bu fonkiyonu kullanmamızın sebebi herhangi bir fonksiyona başka bir fonksiyonu özellik olarak eklemek için

# #iç içe fonksiyonlar


# from ast import main


# def main_outer(func):#dış fonksiyon parametre olarak fonksiyonu alır
#     def main_inner():#iç fonksiyon ise parametre olarak dış fonksiyonda parametre olarak alınan fonksiyona parametre alır 
#         print("addition öncesi") #addition:eklenti
#         func()
#         print("addition sonrası")
#     return main_inner

# #additions
# def addition_1():
#     print(f"addition 1")

# def addition_2():
#     print(f"addition 2 ")    


# #main_outer parametre olarak additionları gönderme
# print(main_outer(addition_1()))#burada yapılan ekleme ile fonksiyona yeni bir özellik eklenmez sadece fonksiyon parametre olarak başka bir fonksiyona gönderilir


# #fonksiyonu fonksiyona özellik olarak eklemek için:

# addition_1=main_outer(addition_1)#eğer fonksiyon içindeki fonksiyonu return etmezse çıktı sadece bir sonuçtur fonksiyon değildir bu yüzden addition_1 e atanan fonksiyon değil değer olur bu yüzden bir fonksiyon gibi davranış gösteremez
# #fonksiyonu fonksiyona özellik olarak eklemek additiona main eklendi
# addition_1()#eğer yukarıdaki atmada bir fonksiyon yerine değer atanırsa yaptığımız bu işlem error verir


"""islem"""
import math
import time
def outer(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)#fonksiyonu uyutamyınca sonuç  0 çıkıyor ama uyutunca 1 küsür çıkıyor ????
        func(*args,**kwargs)#zamanı bir süre uyutmak için time.sleep()kullanılır parametre olarak uyutma süresini alır
        finish=time.time()
        print(f"Fonk adı :{func.__name__} fonksiyonun işlem süresi: {(finish-start)} ")
    return inner    

#addition
@outer
def us_alma(number1,number2):
    print(math.pow(number1,number2))


@outer
def faktoriyel(number):
    print(math.factorial(number))

 #fonksiyona fonksiyon özelliği ekleme
us_alma(2,5)
