#1-->range(başlangıç,bitiş,artış miktarı) metodu hem for hem while içinde hem de döngü dışında kullanılabilir.for içindeki kullanımı javadaki for döngüsü mantığına çok benzer

for item in range(10):
    print(item)

print()

for item in range(10,20):
    print(item)

print()

for item in range(10,20,2):
    print(item)

print()
print()

#2-->enumerate metodu:listeyi karakterler ve bu karakterlere denk gelen indexler olarak oluşturur

#enumerate metodu kullanmadan karakterlere denk gelen index değerlerini yazdırma
index=0
greeting="Hello"
for item in greeting:
    print(f"index:{index} letter:{item}")
    index +=1

print()

#bunun yerine enumerate metodu kullanılır
for index,item in enumerate(greeting):
    print(f"index: {index} letter:{item}")

print()
print()

#3-->eğer listelerdeki aynı indexdeki elemanlar yeni oluşturulucak listede de aynı indexe karşılık gelecek şekilde birleştirilmek istenirse zip metdo kullanılır

list_1=[1,2,3,4,5]
list_2=['G','A','M','Z','E']
list_3=[100,200,300,400,500]

for zip_item in zip(list_1,list_2,list_3):
    print(zip_item)
    #çıktı:
    """ 
(1, 'G', 100)
(2, 'A', 200)
(3, 'M', 300)
(4, 'Z', 400)
(5, 'E', 500)
    """
