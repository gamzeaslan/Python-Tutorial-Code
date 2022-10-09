#traversing=çapraz geçiş
#burada dosya kapatmanın close metodundan başka bir tane daha yolu var onu göreceğiz

#aşağıdaki yapı bir döngüye benzetilebilir eğer döngüden çıkarsak dosya kapanır peki döngü içinde dosya üzerinde yaptığımız değişiklikler döngü dışında da geçerli olur mu 

with open("file.txt","r+",encoding="utf-8") as file:# dosya üzerinde değişiklikler yapabilmemiz için bu dosyayı bir değişkene atamamız lazım file bu değişkendir

    file.write("Yazılım")#eğer r modunda açarsam yazılabilir değil hatası verir bu yüzden r+ modunda açtım
    print(file.read())

    print()

    #imleci en başa atmamız lazım bunun için sürekli dosyayı açmamız gerek yok onun yerine seek metodunu kullanırız
    file.seek(0)#bu metoda parametre olarak girdiğimiz değer imlecin yerine verir .Şu an imleç dosyanın en başındadır

    content=file.read(10)
    print(content)

    print()

    content=file.read(14)
    print(content)

    print()


file=open("file.txt","r")
print(file.read())
file.close()

"""Döngü içinde dosya üzerinde yapılan değişiklik döngü dışında da geçerli oluyormuş"""