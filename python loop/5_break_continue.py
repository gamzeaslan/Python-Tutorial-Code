#break--> döngüyü tamamen kırar

#continue--> döngüyü sadece sağlanan geçerli şart için kırar

#değişken tanımlaması
names="Gamze Aslan"

#for döngüsü ile elemanlarını yazdırma
for name_1 in names:
    print(name_1)

print()

#eğer bu elemanlardan a karakterinin ekrana yazılması istemiyorsak ya break ya da continue kullanacağız


#eğer döngü kırıldıktan sonra devam etmesin istiyorsak break kullanılmalıyız
for name_2 in "Gamze Aslan":
    if(name_2=="a"):
        break 
    print(name_2)    

print()

#eğer döngü kırıldıktan sonra devam etsin istiyorsak continue kullanmalıyız
for name_3 in names:
    if(name_3 =="a"):
        continue 
    print(name_3) 

print()

#1-100 e kadar olan tek sayıların toplamı

number=0
toplam=0

while (number<=100):
    number+=1#sayıyı burada arttırmamızın sebebi sayıyı değiştirmeden döngü kırılır ve sayı arttırılamaz bu yüzden sonsuz döngüye girer
    if(number%2==0):
        continue
    toplam+=number 
print(toplam)   
    
