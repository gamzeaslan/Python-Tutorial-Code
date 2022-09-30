#bu programlama dilinde değişken tanımlanırken değişken tipi belirtilmez
 
#brüt maaşdan vergi kesintisini hesaplayan program yapalım

#değişken tanımlama
ali_maas=6000
ahmet_maas=10000
vergi_orani=0.27

#net maaşları ekrana yazdırma
print(ali_maas - (ali_maas * vergi_orani))
print( ahmet_maas - (ahmet_maas * vergi_orani))

#-----------------Değişken Tanımlama Kuralları---------------------- 

       #1-->rakam ile başlayamaz 

#1number şeklinde bir değişken tanımlanamaz
number1=10
print(number1)#10

#bu değişkenin değeri değiştirilebilir yeni atama yapılarak

       #2-->python da değişkenin tanımlandığı satırda atama yapmak zorunludur

number1=20
print(number1)#20

number1 += 30
print(number1)#20+30=50

       #3-->Python ın büyük küçük harf duyalılığı vardır değişken tanımlaması yapılırken buna dikkat edilmelidir

age=20
print(age)#20

Age=40
print(Age)#40

AGE=30
print(AGE)#30

        #4-->Değişken tanımlaması yaparken Türkçe karakter kullanmayalım
        
#yaş=20
yas=20
print(yas)#20

#değişken türlerine göre atama şekilleri
tam_sayi=12
kesirli_sayi=12.2
metinsel_ifade="Gamze"
mantıksal_ifade=True
#mantıksal_ifade=true olsaydı hata veriyor

first_name="Gamze"
last_name=" Aslan"
print(first_name + last_name)#Gamze Aslan

number1=10
number2=20
print(number1 + number2)#30

number_1='10'
number_2='20'
print(number_1 + number_2)#1020




