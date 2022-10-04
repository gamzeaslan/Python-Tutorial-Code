"""CLASS OLUŞTURMA"""

class Person_1:
    pass
#şeklinde yeniden düzenlenmek üzere tasarlanmış içi boş bir class oluşturuabilirz


"""class-->methods and attributes(class or object)"""


class Person_2:

    #class attributes
    name="User"

    #constructor tanımlama
    #iki alt çizgi eklenir sağa ve sola
    def __init__(self,name,age):#burada self daha doğrusu ilk parametre oluşturulan nesneyi temsil eder
        
        """object attributes"""
        self.name=name#girilen argümanları nesnenin değişkenlerine atama
        self.age=age
        print("Nesne oluşturuldu ve Constructor çalıştırıldı")


"""NESNE OLUŞTURMA"""        
object_1=Person_2("Ayşe",20)#self=object_1
object_2=Person_2("Nur",25)#self=object_2

#Ekrana yazdırma
print(f"object_1 name={object_1.name}--age={object_1.age}")
print(f"object_2 name={object_2.name}--age={object_2.age}")

#updating
object_1.age=22
object_2.name="Elif"


#updating sonradı ekrana yazdırma
print(f"object_1 name={object_1.name}--age={object_1.age}")
print(f"object_2 name={object_2.name}--age={object_2.age}")

#oluşturulan nesnelerin tipini ekrana yazdırma
print(type(object_1))
print(type(object_2))

#oluşturulan bu iki nesnenin eşitliğini sorgulatma
print(object_1==object_2)#False