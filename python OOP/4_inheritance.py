#inheritance-->Kalıtım
#Kalıtım alırken:sub class(super class) şeklinde alınır

"""Super Class Oluşturma"""
class Person:

    #constructor
    def __init__(self,fname,lname):
        print("Persondan nesne oluşturuldu")
        self.fname=fname
        self.lname=lname
        
    #başka bir metot oluşturma(nesne üzerinden erişim)
    def who_I_am(self):
        print("I am a person")

    #başka bir metot oluşturma
    def eat(self):
        print("I am eating")



"""Student Sub Class Oluşturma"""

class Student(Person):

    #constructor///super classda bu parametreler tanımlı olduğu için burada da(sub class) tanımlandı ama atama işlemi super class da gerçekleştirildiği için burada yapılmaz
    def __init__(self,fname,lname,number):
        self.number=number
        #eğer burada cons tanımlanmasaydı super class cons u geçerli olurdu

        #super class consunu subb class consu içerisinde çalıştırmak için:

        Person.__init__(self,fname,lname) 
        print("Student nesnesi oluşturuldu")

    #overriding
    def who_I_am(self):
        print("I am a teacher")

    #student sınıfına özel metot tanımlama
    def say_hello(self):
        print("Hello I am a student")





"""Teacher Sub Class Oluşturma"""

class Teacher(Person):

    #constructor
    def __init__(self,fname,lname,branch):
        self.branch=branch

        #sub consu içerisinde super consu çağırma
        super().__init__(fname,lname)
        print("Teacher nesnesi oluşturuldu")


    #overriding 
    def who_I_am(self):
        print(super().who_I_am()) #I am a Person çıktısını verir
        print(f"I am a {self.branch} teacher")   


"""Nesneleri Oluşturma"""
object_person=Person("Ayşe","Nur")
object_student=Student("Elif","Gül",1234)
object_teacher=Teacher("İlk","Nur","Math")


"""Nesneler Üzerinden Metotlara Erişim"""
object_person.who_I_am()
print()
object_student.say_hello()
print()
object_teacher.who_I_am()
print()


"""Nesneler Üzerinden Değişkenlere Erişim"""
print(f"Person:{object_person.fname} and {object_person.lname}")
print(f"Student:{object_student.fname} and {object_student.lname}")
print(f"Teacher:{object_teacher.fname} and {object_teacher.lname}")





"""Girintilere dikkat et tanımladığını düşündüğün bir metot farklı bir kod bloku içerisinde kalabilir"""