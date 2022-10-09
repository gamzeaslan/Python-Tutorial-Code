"""Herhangi bir dosyaya okuma işlemi gerçekleştirmeden önce dosyanın mevcut olması gerekir eğer mevcut olmayan bir dosya üzerinde okuma işlemi gerçekleştirilirse kod error verir bu yüzden önce dosya oluşturulmalı daha sonra okuma işlemi gerçekleştirilmeli """

#open("file.txt","r")--->şeklinde mevcut olmayan dosya üzerinde okuma yapmak istersek error alırız

#önce dosya oluşturulmalı daha sonra okuma işlemi gerçekleştirilmeli-->eğer create modunda oluşturulursa sadece 1 kez çalıştırabilirsin programı çünkğ oluşturulan dosya tekrar oluşturulmaya çalışılırsa kod hata verir
file=open("file.txt","w",encoding="utf-8")#utf-8 olarak değiştirilmesinin sebebi dosyadaki türkçe karakterleri geçerli kılmaktır
file.write("Hello World")
file.close()
#eğer dosya tekrar okuma modunda açılırsa error vermez
file=open("file.txt")#--->default olarak read ayarlıdır yani eğer herhangi bir mod belirtilmezse read modunda açılır dosya 
print(file.read())#dosya içeriğini yazdırmak için read metodundan yararlanılır


#mevcut olmayan bir dosyayı read modunda çalıştırdığımızda aldığımız hatayı try except ile belirtirsek
try:
    file2=open("file2.txt","r",encoding="utf-8")
    print(file2.read())
except FileNotFoundError as error:
    print(f"Read modunda çalıştırılan dosyanın mevcut olması gerekir : {error}")    
finally:
    """file2.close()#dosya var olmadığından read modu ile açılamaz bu yüzden açılmayan bir dosya kapatılamaz"""
    print("Dosya kapatıldı")



"""-----------------Dosya Okumanın Birden Fazla Yolu Vardır-----------------"""

#1.YOL:FOR DÖNGÜSÜ
file=open("file.txt")
for i in file:
    print(i)
#şeklinde dosyanın tüm elemanlarına for döngüsüyle ulaşılarak ekrana yazdırılır


#2.YOL:READ METODU 
file=open("file.txt")
print("1.okuma")
print(file.read())
print("2.okuma")
print(file.read())#--->2.okumada hiçbir şey ekrana yazdırılmaz sebebi ise imlecin dosyanın sonunda olmasından kaynaklıdır.Bu metot imleç bazlı çalışır ve eğer imleç sonda ise imleçten sonra okunacak bir şey olmadığından ekrana hiçbir şey yazdırmaz 

#Dosyanın iki kere üst üste okunması için 1.okumadan sonra dosyanın kapatılıp tekrar açılması  açıldıktan sonra 2.okumanın gerçekleştirilmesi gerekiyor

file.close()
file=open("file.txt")
print(file.read())#şeklinde dosya tekrar okunabilir

file.close()
#imleci başa alma
file=open("file.txt")
#şuan imleç dosyanın başında
 
#eğer okuma işlemini en baştan en sona yapmak istemiyorsak sadece belli bir kısmını okumak istiyorsak:
print(file.read(5))#ilk 5 karakter okunur ve ekrana yazdırılır
print(file.read(4))#ilk 5 karakterden sonraki 4 karakter okunur ve ekrana yazdırılır


print()


"""readline() fonksiyonu"""
#önce dosyaya birkaç satır daha ekleyelim burada yapmamızın sebebi direkt dosya üzerinde  değişiklik yapınca bu değişikliklerin kalıcı olamamasından kaynaklı
file=open("file.txt","r+",encoding="utf-8")#buradaki r+ -->hem okuma hem yazma işlemini gerçekleştirme modudur
file.write("Hello World\n")
file.write("Gamze Aslan\n")
file.write("Yazılım\n")
file.close()

#artık dosyamız birden fazla satırdan oluştuğuna göre readline metodunu kullanabiliriz
file=open("file.txt")
#readline metodunun çalışma mantığı şu şekilde : readline metodu satır bazlı okuma yapar 
print(file.readline(),end="")#çıktı:Hello World
print(file.readline(),end="")#çıktı:Gamze Aslan


print()

"""readlines() metodu her satırı dizinin bir elemanı haline getirir"""
file=open("file.txt")
liste=file.readlines()#şu an imleç dosyanın sonunda önce imleç dosyanın başına getirilmeli yoksa error alırız

#oluşturulan dizinin elemanlarını ekrana yazdırma
print(liste[0],end="")
print(liste[1],end="")
print(liste[2],end="")

file.close()