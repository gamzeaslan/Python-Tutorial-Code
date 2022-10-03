"""Javada olduğu gibi burada da class içerisinde tanımlanan değişkenleri global ve heryerden bu değişkenlere ulaşılabilinir .Bir metot ,fonksiyon ya da classın altında bulunan bir kod bloku içerisinde tanımlanan değişkenler local değişkenlerdir ve bu değişkenlere heryerden erişilemez"""



#sınıf içerisinde herhangi bir kod bloku içinde tanımlanmadığından global değişkendir
name="global değişken"

def string_toplama(name_1,name_2):
    #fonksiyon içerisinde tanımlanan name değişkeni local bir değişkendir
    name=name_1 + name_2
    #eğer bu local değişkeni tanımlı olduğu blok içerisinde yazdırırsak son atanan değeri verir
    print(f"local değişken:{name}")


string_toplama("a","b")# local değişken:ab
print(name)#global değişken
#eğer local değişkeni kapsamı dışında ekrana yazdırmak istersek bu sefer devreye global değişken girer

#eğer blok içinde de blok açarsak:
print(name)#global değişken
def say_name(name):#argüman
    print(name)#eğer süslü parantez içine alırsak name tırnak içinde ekrana yazdırır

    def say_hello():
        name="Ayşe"
        print(name)#ayşe

say_name("Elif")  


#eğer local bir değişken üzerinde yaptığımız değişiklikleri global alanda da kaydetmek istersek-->bunun için global keyword kullanılır:
x=50
def test():
    global x#yapılan değişiklikler sınıf değişkeni olan x değişkeni üzerinden gerçekleştirilir
    print(x)
    x+=10
    print(x)


test()
