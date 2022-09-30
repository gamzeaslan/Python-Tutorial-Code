#boş liste tanımlama sonra for döngüsündeki değerleri bu listeye eleman olarak ekliyeceğiz
numbers=[]

#0 dan 10 a kadar olan sayılar number değişkenine atanır
for number in range(10):

    #her number değeri numbers listesinin sonuna eleman olarak eklenir
    numbers.append(number)

#oluşturulan listeyi ekrana yazdırma
print(numbers)

print()
print()

#hem döngü için hem atama için bu kadar fazla kod satırı kullanmak yerine :

numbers=[number for number in range(10)]#şeklinde de listeye atama yapılabilinir
print(numbers)

print()

#1 den 10 kadar olan sayıların kareleri listeye eleman olarak atandı
numbers=[number**2 for number in range(10)]
print(numbers)

#eğer 1 den 10 a kadar olan sayılardan sadece çift olanlarını listeye eleman olarak eklemek istersek
numbers=[number for number in range(10) if number%2==0 ]#burada else ifadesini kullanınca hata veriyor 
print(numbers)#çıktısı:[0, 2, 4, 6, 8]

print()

#eğer koşul ifadesinin yerine daha ileriye taşırsak
numbers=[number if number%2==0 else "TEK" for number in range(10)]
print(numbers)#çıktısı:[0, 'TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK'] şeklindedir 

print()

#eğer yukarıdaki ifadeleri str bir ifade için uygularsak
my_string="Hello"
my_list=[]

for letter in my_string:
    my_list.append(letter)
print(my_list)    

my_list=[letter for letter in my_string]
print(my_list)

print()

#doğum yılları listesindeki yılları kullanarak hesaplanan yaşları yeni bir listeye eklersek
years=[1999,2002,2001,1980,1973]
age=[2019-year for year in years]
print(age)

print()

result=[]

#iç içe for döngüsünde
for x in range(3):
    for y in range(3):
        result.append((x,y))#ek parantez şart--->(x,y)

print(result)

print()

numbers=[(x,y) for x in range(3) for y in range(3)]#ek parantez şart--->(x,y)
print(numbers)
        