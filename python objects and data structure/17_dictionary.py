"""-----------------DICTIONARY-----------------"""

#1-->Liste tiplerinden biridir



#2-->Bu liste tipi key-value şeklide çalışır:41(value)-->kocaeli(key) şeklindedir yani key değerleri üzeriden value değerlerine ulaşabiliriz
#syntax-->dic={key:value,key:value,..} şeklindedir
dictionary_1={'Kocaeli':41}
#sonrasında key değerini kullanarak value değerine ulaşacağız:
value_değeri=dictionary_1['Kocaeli']
print(f"Kocaeli key değeri ile 41 value değerine ulaşacağız:{value_değeri}\n")





#3-->eğer dictionary listelerdeki key-value durumunu normal liste ile yaparsak:
plaka=[41]
sehir=["Kocaeli"]
value_değeri=plaka[sehir.index('Kocaeli')]
print(f"dic yerine normal list ile key-value gerçekleştirildi:{value_değeri}\n")




#4-->bu listelerde liste ataması yapıldıktan sonra eleman eklemesi yapabiliriz
#list adı[key adı]=value değeri şeklinde eklemeler yapılabilinir
dictionary_1['Ankara']=6
print(f"dic listesine sonrada ankara keyi ile 6 value değerleri eklendi:{dictionary_1}\n")




#5-->bu liste türünde ataması yapılmış key-value değerleri sonradan yapılan atamalarla güncellenebilir
dictionary_1["Kocaeli"]=20
print(f"kocaeli key ne karşılık gelen value değeri 41-->20 şeklinde güncellendi:{dictionary_1}\n")





#6-->dic içinde dic oluşturulabilir
personel_dic={'personel_1':{'age':26,'maas':10000,'ismi':'Ayşe','soyismi':'Nur'},
             'personel_2':{'age':26,'maas':10000,'ismi':'Ayşe','soyismi':'Nur'},
             'personel_3':{'age':26,'maas':10000,'ismi':'Ayşe','soyismi':'Nur'}}
print(f"personel dic içindeki 1.personelin dic bilgileri yazdırma:{personel_dic['personel_1']}")  
print(f"personel dic içindeki 1.personelin yaş bilgisi:{personel_dic['personel_1']['age']}")    





#7-->dic(dic(list)) uygulaması da yapılabilir
personel_dic={'personel_1':{'son 3 ayın maaş geçmişi':[10000,14000,23000]},
               'personel_2':{'son 3 ayın maaş geçmişi':[5000,7000,8000]},
               'personel_3':{'son 3 ayın maaş geçmişi':[8000,9000,10000]}
}
print(f"dic(dic(list)) ile 1.personelin 2.ayda aldığı maaş:{personel_dic['personel_1']['son 3 ayın maaş geçmişi'][1]}")