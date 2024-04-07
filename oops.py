class person:
    name = 'ashish'
    age = 18
p1 = person()
print(p1.name)
print("_"*30)

p2 = person()
p2.name = 'manav'
p2.age = 19
print(p2.name)
print(p2.age)


class mathematics:
    def greet(self):
        print('hello')
        return 'hi'
    
    def factorial( self , n):
        s = 1
        for i in range( 1, n+1):
            s*=i
        return s
        
    def lst(self , lst):
        s=1
        for i in lst:
            s*=i
        return s
    
    def mul_lst( self, lst1 , lst2):
        return( [ lst1[i]*lst2[i] for i in range(len(lst1))])
    
math = mathematics()
print(math.greet())
print(math.factorial(5))
print(math.lst([1 , 3 , 5]))
print(math.mul_lst( [ 1 , 2 , 3 , 4],  [ 5 , 6 , 7, 8]))
