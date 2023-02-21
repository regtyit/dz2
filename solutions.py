class Solution:
    def __init__(self) -> None:
        self.name ="Ivan"
        self.surname ="Ivanov"
        self.age = 14
        
    def attr(self,setting,i):
        attr=[self.name,self.surname,self.age]
        attr[i] = setting
        self.name = attr[0]
        self.surname = attr[1]
        self.age = attr[2]


    def hello(self,*settings):
        for i in range(3):
            try:
                self.attr(settings[i],i)
            except IndexError:
                pass


        print('Hello', self.name, self.surname, str(self.age),'years old')
        self.name ="Ivan"
        self.surname ="Ivanov"
        self.age = 14


a=Solution()
a.hello('Dima','Petrov', 20)
a.hello('Dima','Petrov')
a.hello('Dima')
a.hello()