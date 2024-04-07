#zip
lst1 = [ 'a ' , 'b ' , 'c']
lst2 = [ 1 , 2 , 3]
print(list(zip(lst1 , lst2)))

matrix = [ [1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9]]
print([list(row)for row in zip(matrix)])
print([list(row)for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row)for row in zip(*matrix)])])

lst_1 = [1 , 3 , 5 ]
lst_2 = [ 2, 4, 6]
print([i*j for i,j in zip(lst_1, lst_2)])
print(sum([i*j for i,j in zip(lst_1, lst_2)]))


#filter
lst = [ 1 , 3 , 5 , 2,  7, 6 , 89 , 90.0]
def is_even(n):
    return n%2==0
print(list(filter(is_even , lst)))


#lambda
num = lambda x,y: x*y
print(num(5,5))

fun = [ 1 , 3 , 5 , 2,  7, 6 , 89 , 90.0]
print(list(filter(lambda x:x%2==0 , fun)))



#map
lst = [ 1 , 3 , 5 , 2,  7, 6 , 89 , 90.0]
def sqr(n):
    return n**2
print(list(map(sqr , lst)))


names = [ 'manav' , 'diya' , 'anjali' , 'vishal']
print(list(map(lambda x: len(x) , names)))


#ASCII
for i in range(33, 127):
    print( i , chr(i))

text = "MANAV"
ascii_list = [ ord(char) for char in text]
print(ascii_list)

name = "Python"
ascii_name = [ord(x) for x in name]

print(ascii_name)
