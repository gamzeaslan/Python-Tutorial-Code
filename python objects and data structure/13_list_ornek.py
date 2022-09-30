#                         --------------SORULAR-------------

#1-->"Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
cars_list=["Bmw","Mercedes","Opel","Mazda"]#liste oluşturuldu
#diziyi ekrana yazdırma
print(f"Arabalar listesinin elemanları: {cars_list}\n")




#2-->Liste kaç elemanlıdır
liste_eleman_sayisi=len(cars_list)#eleman sayısı hesaplandı
#listenin eleman sayısını ekrana yazdırma
print(f"Arabalar listesinin eleman sayısı:{liste_eleman_sayisi}\n")





#3-->Listenin ilk ve son elemanı nedir?
#listenin ilk elemanı:
list_ilk_eleman=cars_list[0]
#listenin son elemanı:
list_son_eleman=cars_list[-1]# ya da len(cars_list)-1 de yazılabilir
#ilk ve son değerleri ekrana yazdırma(formatlayarak)
print(f"arabalar listesinin ilk eleman:{list_ilk_eleman}\narabalar dizisinin son elemanı:{list_son_eleman}\n")






#4-->Mazda değerini Toyota ile değiştirin
cars_list[-1]="Toyota"
#yeni listeyi ekrana yazdırma
print(f"Mazda-->Toyota:{cars_list}\n")






#5-->Mercedes listenin bir elemanı mıdır?
# bunu öğrenmenin 2 yolu var
#------------------1.yol-------------------
is_mercedes="Mercedes" in cars_list#boolean değer döndürür
print(f"Mercedes ifadesi liste de var mı(in):{is_mercedes}")
#------------------2.yol-------------------
mercedes_sayisi=cars_list.count('Mercedes')
print(f"Mercedes ifadesi listede  kaç tane var:{mercedes_sayisi}\n")






#6-->Listenin -2 indeksindeki değer 
print(f"Arabalar listesinin -2 indeksindeki değer :{cars_list[-2]}\n") # ya da len(cars_list)-2 de kullanılabilir







#7-->Listenin ilk 3 elemanını alın
liste_ilk_3_eleman=cars_list[0:3]
print(f"Arabalar listesini ilk 3 elemanı:{liste_ilk_3_eleman}\n")







#8-->Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
#liste içine liste eklenebilir
cars_list[len(cars_list)-2:len(cars_list)-1]=["Toyota","Renault"]
#yeni listeyi ekrana yazdırma
print(f"yeni arabalar listesi:{cars_list}\n")







#9-->Listenin üzerine "Audi" ve "Renault" değerlerini ekleyin
cars_list=cars_list+["Audi","Renault"]
#ekrana yazdırma
print(f"üstüne ek yapılmış yeni liste:{cars_list}\n")







#10-->Listenin son elemanını silin
del cars_list[-1]
print(f"son elemanı silinen liste:{cars_list}\n")






#11-->Listenin elemanlarını tersten yazdırın
ters_cars=cars_list[::-1]
#ekrana yazdırma
print(f"listeyi tersten ekrana yazdırma:{ters_cars}\n")








#12-->Aşağıdaki verileri bir liste içinde saklayınız 
"""
student_A: Yiğit Bilgi 2010,(70,60,70)
student_B:Sena Turan 1999,(80,80,70)
student_C:Ahmet Turan 1998 ,(80,70,90)
"""
student_A=["Yiğit","Bilgi",2010,[70,60,70]]
student_B=["Sena","Turan",1999,[80,80,70]]
student_C=["Ahmet","Turan",1998,[80,70,90]]






#13-->Liste elemanlarını ekrana yazdırınız
print(f"a:{student_A}\nb:{student_B}\nc:{student_C}\n")
