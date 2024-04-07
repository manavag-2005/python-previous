def great(name):
    return 'hello ' + name
great('ahish')

a = 1
def greet():
    b = 2
    print( a, b)
greet()
print(a)
print("-"*20)


name = input("enter your name: ")
def hi(n):
    print('hello' , n)
hi(name)
print("-"*20)


num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
def sum(a , b):
    return a+b
add = sum(num1 , num2)
print(add)
print("-"*20)


num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
def sum(a , b):
    return a+b , a-b , a*b
add = sum(num1 , num2)
print(add)
print("-"*20)


list = [1 , 2 , 3 , 4]
def sq(list):
    return [i**2 for i in list]
def cu(list):
    return [i**3 for i in list]
def finallist(list):
    lst1 = sq(list)
    lst2 = cu(list)
    return [ lst1[i] + lst2[i] for i in range(len(lst1))]
print(sq(list))
print(cu(list))
print(finallist(list))