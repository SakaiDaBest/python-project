class User:
    def __init__(self,id,name):#constructor
        self.id  = id
        self.name = name

    def id_null(self):
        self.id="000"

user_1 = User("001","Sakai")#will always call the constructor

print(user_1.name)