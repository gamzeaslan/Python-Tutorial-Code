#encoding=utf-8

#w modunda dosya açma
file_1=open("file.txt","w")#aynı dizinde açılır
file_1.write("---------------")
#mevcut dosyanın kapatılaması
file_1.close()

#eğer mevcut dosya write modunda tekrar açılırsa
file_2=open("file.txt","w")#mevcut dosya içeriği silinir
file_2.write("**************")#siline dosya içeriği yenidan yazılır
file_2.close()

#eğer mevcut dosyaya ekleme yaparken dosya içeriğinin silinmesini istemiyorsak dosyayı a(append) modunda açmalıyız
file_3=open("file.txt","a")
file_3.write("-------------------------")#yaptığımız değişiklikler mevcut dosya üzerine eklenir


#eğer sadece dosya oluşturmak amacıyla açmak istiyorsak x(create) modunda açarız .Eğer belirtilen dosya mevcut ise error verir
file_4=open("file_1.py","x")
#file_4=open("file.txt","x") şeklinde bir uygulama yapmaya çalışırsak kod error verir
#eğer bu kodu 2 kere çalıştırırsak bu dosyanın 2 kere oluşturulacağı anlamına geliyor eğer oluşturulmaya çalışılan dosya mevcut ise kod error verir .Yani eğer bir program içerinde dosya oluşturma işlemi varsa o program sadece bir kere çalıştırılabilir


#eğer dosya açılırken herhangi bir mod belirtmezssek default değer olarak r(read) değerini atar ve dosya read modunda açılır
