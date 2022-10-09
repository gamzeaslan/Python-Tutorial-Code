"""Dosya Sayfasındaki Güncellemeler"""#-->Güncellemelerin yeri imlecin yerine bağlıdır

"""Dosya Başında Güncellemeler"""

file=open("file.txt","r+",encoding="utf-8")
file.write("Dosya Başında Güncelleme\n")
file.seek(0)
print(file.read())

# # ya da 
# content=file.read()
# content="Dosya Başında Güncelleme" +content#bu değişiklikler değişken bazlıdır bu değişikliği dosyaya aktarmak için:
# file.write(content)

print()
file.close()

"""Sayfa Sonunda Güncelleme"""
file=open("file.txt","a",encoding="utf-8")#append modunda açılmasının sebebi yapılan değişiklikleri sayfa sonuna eklemesidir
file.write("Dosya Sonunda Güncelleme\n")
file.seek(0)
# print(file.read())-->Hata vermesinin sebebi dosyanın append modunda açılmasıdır 

print()
file.close()


"""Sayfa Ortasında Güncelleme"""#sayfa liste haline çevrilir ve liste elemanlarına erişerek yapılan değişikliklerin yeri ayarlanabilir
file=open("file.txt","r+",encoding="utf-8")
list=file.readlines()#sayfa listeye çevrildi
list.insert(0,"Dosya Ortasında Güncelleme\n")
file.writelines(list)
#eğer dosyayı tekrar eski haline getirmek istiyorsak bunu metot kullanarak ya da for döngüsüyle yapabiliriz
# file.seek(0)
# for i in list:
#     file.write(i)
# file.seek(0)
# print(file.read())    




"""Dosya Ortasında Yapılan Güncellemeleri Anladım Fakat Programı Her Çalıştırdığımda Aynı Güncellemeler Tekrar Tekrar Yapılıyor Bu Yüzden Program Çıktısı Karmaşık Bir Hal Alıyor--->Bu Yüzden Kafam Karıştı """




