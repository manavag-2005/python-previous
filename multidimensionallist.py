list = [ [1 , 2  ,3], [ 4 , 56 , 343 ], [ 45 , 56 , 778]]

# for i in list:
#     for j in i:
#         print(j)

# list[0].reverse()
# print(list)

# maxvalue = find max value(list)
# print(maxvalue)

print([j for i in list for j in i])