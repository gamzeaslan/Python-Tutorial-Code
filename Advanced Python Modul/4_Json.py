#sadace python a özgü bir yepı değildir
#bir databaseden bilgileri mesela bir android uygulamasına verileri json tipinde kolaylıkla taşıyabiliyoruz
#her platformun anlatığı bir data türüdür.yani cihazlar arasında ortak bir veri taşıma objesi olarak adlandırabiliriz
#dic söz dizimine göre yazılmış string veridir

import json
#loads(str)-->string to Dict
person_string='{"name":"Ali", "languages":["python","C#"]}'
person_dic=json.loads(person_string)#load metodunu kullanınca error veriyor
print(person_dic)
print(type(person_dic))

# #dic to str
# person_str=json.dumps(person_dic)
# print(person_str)
# print(type(person_str))



#dic to str
person_str=json.dumps(person_dic,indent=4,sort_keys=True)
print(person_str)
print(type(person_str))