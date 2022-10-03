#value değerlerini parametre olarak alan bir fonksiyonda bu değerler üzerinde yapılam değişiklikler geçerli değildir

def change_name (name):#bu fonksiyonla girilen value değerinin değiştirilemesi amaçlanıyor
    name="fatma"

name="Ayşe"
change_name(name)#bu bir işlem fonksiyonu

#burada ayşe isminin fatma ile değiştirilmesi amaçlanıyor ancak değişken bir value değeri olduğu için yapılan değişikliler kaydedilmez
print(name)#çıktı yine ayşe olur







#yukarıdaki işlemlerin aynısını referans tipler için gerçekleştirirsek yapılan değişiklikler kaydedilir çünkü yapılan değişikilikler birbirine bağlıdır
list=["istanbul","ankara","izmir","antalya"]
print(list)
def change_name_2 (list):
    list[0]="elazığ"

change_name_2(list)
print(list)    







#eğer yeni bir referans liste tanımalamak istersek  (orijinalinin değişmesini istemiyorsak)
list_2=list[:]#list elemanlarını referans göstermek yerine bellekte yeni bir referans oluşturuldu bu yüzden list ve list_2 üzerinde yapılacak değişiklikler birbirinden bağımsızdır






#eğer parametre olarak bir tuple türünde liste alırsak


def toplama(*list):
    print(type(list))
    toplam=0
    for item in list:
        toplam=toplam+item
    return toplam

print(toplama(12, 23, 34))#bir çift parantez daha kullanılırsa kod error verir -->hata:TypeError: unsupported operand type(s) for -: tuple and int(TypeError: - için desteklenmeyen işlenen türleri: tuple ve int)-->hata fazladan demet oluşturmak ??
print(toplama(12, 23, 34, 35, 45))







#eğer tuple liste yerine dic listeyi parametre olarak almak istersek 


def display_user(**args):
    print(type(args))
    for key,value in args.items():
        print(f"key: {key} - value:{value}")

display_user(name="Ayşe" , age="12",city="ankara")







#eğer hem value hem tuple list hem de dic list i parametre olarak beraber alırsak

def my_func(a,b,c,*tuple,**dic):
    print(a)
    print(b)
    print(c)
    print(tuple)
    print(dic)


my_func(12,3,34,32,24,123,12,key1="value1",key2="value2")