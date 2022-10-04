#class-->Person(parametreler)
#insatance(object)

"""OOP 4 temel ana prensibe dayanır:"""#Encapsulation(Kapsülleme),Inheritence(Kalıtım),Abstaction(Soyutlama),Polymorphism(Çok biçimlilik)

"""1-->Kapsülleme:"""#Bu prensibin kullanım amacı class propertylerini korumaya alamaktır bu işlemi erişim belirteçleri ile sağlar.Korunmaya alınmasındaki amaç her class tarafından propertylerin değiştirilmesini engellemektir.Eğer bir property’i tanımlarken private kullanırsak o class dışında hiçbir yerden erişim sağlanamaz. Protected kullanırsak da yalnızca subclass’lar ve aynı package’da bulunan classlar tarafından erişilir. Propertyler korunmaya alındıktan sonra bu propertylere erişim getter(return) ve setter(atama) metotları ile sağlanır.Erişim bunlar üzerinden sağlandığı için private olamazlar




"""2-->Inheritance(Kalıtım):"""#Herhangi bir class'ın(sub class) üst class'larına(super class) ait olan method ve propertyleri(özellik) kalıtım yoluyla almasıdır.Kalıtım reusability(Tekrar kullanılabilirlik) destekler.Yeni bir sınıf oluşturmak istediğimizde ve ihtiyacımız olan bazı kodlara sahip bir class varsa yeni sınıfımızı bu sınıfın alt sınıfı olarak alabiliriz. Bunu yaparak varolan sınıfın alanlarını(fields) ve metotlarını tekrar tekrar kullanabiliriz.5 çeşit kalıtım türü vardır:
"""2.1-->Single Inheritance(a-->b)okunun gösterdiği uç sup class -okun çıktığı uç super class dır"""

"""2.2-->Multilevel Inheritance(a-->b-->c)"""

"""2.3-->Hierarchical Inheritance(a-->b//a-->c//a-->d"""

"""2.4-->Multiple Inheritance(Interface aracılığıyla)(a-->c //b-->c)"""

"""2.5-->Hybrid Inheritance(Interface aracılığı ile)(a-->b//a-->c///b-->d // c-->d"""




"""3-->Abstraction(Soyutlama):"""#Kodların veya yapıların iç detaylarını saklayarak kullanım kolaylığı sağlar





"""4-->Polymorphism(Çok Biçimlilik)-->Overloading-->Overriding"""#mevcut metodun parametleri üzerinde değişiklikler yaparak tekrar kullanmaktır -->Overloading // Overriding super classda bulunan bir methodun sub class da yeniden oluşturulmasıdır

