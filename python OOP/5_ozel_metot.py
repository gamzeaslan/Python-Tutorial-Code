#class oluşturma
class Movie:

    #constructor
    def __init__(self,title,director,duraction):

        self.title=title
        self.director=director
        self.duraction=duraction

        """liste oluşturma
        # list=[1,2,3,4,5]
        # object=Movie("film adı","yönetmen adı",120)

        # print(len(list))#listenin uzunluğunu verir
        # print(len(object))#nesnenin uzunluğunu vermez"""

        #listede geçerli olan metotların nesneler için de geçerli olması için bu metotların nesnenin oluşturulduğu class içerisinde özel metot olarak tanımlanması gerekir
        
    def __str__(self):
        return (f"{self.title} by {self.director}")


    def __len__(self):
        return (self.duraction)


    def __del__(self):
        print("Movie classından oluşturulan nesne silindi")        


#oluşturulan özel metorları kullanma
object_movie=Movie("film adı","yönetmen adı",120)

list=[1,2,3,4,5]
print(len(list))
print(len(object_movie))
print(str(list))
print(str(object_movie))#bir süre kullanılmayan nesne kendiliğinden silindiğinden(del nesne adi) bu çıktıdan sonra nesne silinir ve __del__ tanımlanan çıktıyı ekranda gösterir




