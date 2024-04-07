class person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age= age

#     def run(self):
#         print(self.name)
#         print("run!")

# p1 = person('manav' , 19)
# print(p1)
    
    def __init__(self , name , age):
        print('welcome to the game')
        self.name = name
        self.age = age
        self.health = 100
        self.alive = 1

    def curr_health (self):
        print('current health of ' + self.name + " is " + self.health)

    def punched(self):
        self.health -=10

    def shooted(self):
        self.health-=50

    def is_alive(self):
        if self.health <=0:
            alive = 0

    def get_healtha(self):
        return self.health

    def info(self):
        print( 'Name   :' , self.name)
        print( 'age    :' , self.age )
        print( 'health :' , self.health)
        print( 'Alive   :' , self.alive)

p1 = person ('manav' , 19)
p1.shooted()
p1.punched()
p1.info()
print("_"*30)
p2 = person("diya" , 19)
p2.shooted()
p2.shooted()
p2.info()





