class Person(object):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def to_string(self):
        print(f'이름{self.name},나이{self.age},사는곳{self.address}')
