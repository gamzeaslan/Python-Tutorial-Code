#liste dışı elemanları döngü kullanarak yazdırmak için while döngüsü kullanırız

#1-->1-100 e kadar olan sayıları ekrana yazdırmak

#ilk atama
x=1

#while döngüsü kullanrak ekrana yazdırma
while (x<=100):
    print(x)
    #sonsuz döngüye girmemesi için değer değişimi
    x+=1


print()

#2-->1-100 e kadar olan sayılardan çift sayıları ekrana yazdır

#yeni değişken tanımlaması x in son değeri 100 dür 
y=1
while (y<=100):
    if(y%2==0):
        print(f"Çift Sayı: {y}")#eğer  arttırma işlemini sadece döngü içinde yaparsak 
    y+=1 

print()

name=''
while not name:
    name=input("isim: ")#isim girişi yapılmadığı sürece sürekli bunu ekranda gösterir
    #eğer isim yerine boşluk tuşuna basarsak-->bu durumda boşluk karakterini bir isim olarak algılar

#bunu engellemek için name karakterinin başındaki boşluk karakterini silerek işlem yapmalıyız bunun için:

name=''
while not name.split():#artık boşluk karakteri isim olarak sayılmıyıcak bu yüzden boşluk tuşuna bassak bile döngü kırılmaz
    name=input("isim: ")

    
       


