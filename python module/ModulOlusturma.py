"""
Modül hakkında dökümantasyon
"""

#modül baçka bir projede import edildiğinde ekrana çıkacak bilgilendirme mesajı
print("modül eklendi")

#modül değişkeni
number=10

#modül listesi
numbers=[1,2,3,4]

#modül dic 
person={
    "name":"Ayşe",
    "age":"25",
    "city":"istanbul"
       }

#modül fonksiyonu
def func(x):
    """
    fonksiyon hakkında dökümantasyon
    """
    print(f"x:{x}")

#modül classı
class Person:
    def speak(self):
        print("I am speaking")    