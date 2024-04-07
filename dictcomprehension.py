dict = { i : i**2 for i in range(1 , 6)}
print(dict)

lst1 = [ 'a ' , 'b' , 'c', 'd']
lst2 = [ '1' , '2', '3' , '4']
dct = { lst2[i] : lst1[i] for i in range (len(lst1)) }
print(dct)

matrix = [ [1 , 2 , 3 , 4] , [ 5 , 6 , 7 , 8 ] , [ 9 , 10 , 11 , 12]]
final = { (i , j) : matrix[i][j] for i in range(3) for j in range(4)}
print(final)