import ModulOlusturma as modul
#modül isiminin başında sayı olduğunda error veriyor

#doc erişim
print(help(modul))
print(help(modul.func))

#modül değişkenine erişim
print(modul.number)

#modül listesine erişim
print(modul.numbers)

#modül dic erişim
print(modul.person["age"])

#modül fonksiyonuna erişim
print(modul.func(10))


#modül classından nesne oluşturma
object=modul.Person()

#oluşturulan bu nesnenin sınıf fonksiyonlarına erişimi
object.speak()
