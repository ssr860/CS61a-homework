""" class User:
    
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.species="human"
        self.login_attempts=0

    def recognize_user(self):
        print(f"Here is a {self.species}!")

    def full_name(self):
        full_name=f"{self.last_name} {self.first_name}"
        return full_name
        
    def describe_user(self):
        print(f"The user's name is {self.full_name()}.")

    def greet_user(self):
        if self.gender=="female":
            print(f"Hello,madam!")
        else :
            print(f"Hello,sir!")

    def update_age(self,age):
        self.age=age
        if age>=18:
            print('Congragulations,you are an adult!')
        else :
            print('What a pity! Wait for some time......')

    def incremnt_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)

one_user = User("Alenxender","Henry",10,'male')
one_user.greet_user()
one_user.describe_user()
one_user.update_age(18)
one_user.incremnt_login_attempts()
one_user.incremnt_login_attempts()
one_user.reset_login_attempts()

another_user=User('Chat',"gpt",5,"nonsex")
another_user.species='robots'
another_user.recognize_user()

class Child(User):

    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)

one_more=Child("Amy","Green",8,"female")
one_more.describe_user()
one_more.incremnt_login_attempts()

class Admin(User):
    
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.previledges={
            'can add post','can delete post','can ban user'}
    
    def print_previledges(self):
        for i in self.previledges:
            print(i)

admin=Admin("a","b",50,"male")
admin.print_previledges()

from random import randint
randint(10,14)

from random import choice
choice(admin.previledges) """
# class Base:
#     value=10

#     # def __init__(self,value:int=4) -> None:
#     #     self.value=4

# # class follow(Base):
# #     # value=1

# #     def __init__(self) -> None:
# #         # self.value=2
# #         super().__init__()

# # f=follow()
# # print(f.value) 
# # g=follow()
# # print(g.value)
# # f.value=3
# # print(f.value)
# # print(g.value)

# f=Base()
# print(f.value)
# Base.value=3
# g=Base()
# print(g.value)