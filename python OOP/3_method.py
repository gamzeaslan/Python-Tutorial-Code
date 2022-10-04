class Person:
    adress="no information"

    #constructor
    def __init__(self,name,year):

        #object attributes
        self.name=name
        self.year=year


    #instance method
    def intro(self):
        print("Hello There .I am " + self.name)#bu metot içinden self.name değişkenine erişebiliyormuşuz sanırım sebebi parametre olarak alınan self metodu 


    #instance method
    def calculateAge(self):
        return 2022-self.year


p1=Person("Ayşe",1992)
p2=Person("Fatma",2001) 
print(p1.calculateAge())
print(p1.intro())

#ircel adlı sınıf oluşturuldu
class Circle:
    #class attribute 
    pi=3.14

    #constructor 
    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    # def cevre_hesaplama(self):
    #     return (2*pi*self.yaricap)--->Bu şekilde kod  hata verir pi yüzünden (pi tanımlanmış hatasını)    
    
    def cevre_hesaplama(self):
        return(2*self.pi*self.yaricap)#--->self.pi şeklinde yazıldığında kod hata vermez


    def alan_hesaplama(self):
        return(self.pi*(self.yaricap**2))

    # object_1=Circle()---->Şeklinde bir tanımlama sonucunda error verir


object_1=Circle(3)#object_1 adında Circle türünden bir nesne oluşturuldu
print(object_1.alan_hesaplama())#metotların sonundaki parametre girişi için ayrılmış parantezler yazılmazsa kod hata vermez ama metot bir metot gibi davranmaz bu yüzden bir çıktı üretilmez
print(object_1.cevre_hesaplama())