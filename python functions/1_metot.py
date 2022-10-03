#liste tanımlama
list=[1,2,3]

#metotlar sınıflarla beraber gelen kütüphane içinde dahil olan yapılardır 
#1-->fonk:fonksiyonları class içinde tanımlamıyoruz ancak metotları classlar içerisinde tanımlarız metotlarda classdan türetilen nesneler üzerinden ulaşıyoruz fakat fonksiyonlara fonk isimleri üzerinden ulaşıyoruz

#append() metodu nesne üzerinden erişildiğinden bir metottur fonk değildir
list.append(12)
print(list)

print()

#ya da pop metodu da aynı şekilde nesne üzerinden erişim sağlandığından bir fonk değildir metottur
list.pop()
print(list)

print()

#str değişken türü üzerinden metotları uygularsak
my_string="Hello World"
print(my_string.upper())
print(type(my_string))

