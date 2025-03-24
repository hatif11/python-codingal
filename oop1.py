class Animal:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def details(self):
        print(f'hello guys this is me and my dog name is {self.name} and the breed of the dog is {self.breed}')

dog = Animal('Ash','Rotweiller')
dog.details()
