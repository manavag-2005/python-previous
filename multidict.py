# dict = { 1: {'name': 'ashish' , 'number': '456'} , 2: {'name': 'manav' , 'number': '788652'}}
# for i in dict.keys():
#     print(i , dict[i] ['name'] , dict[i]['number'])

data = { 1: {'name': 'ashish' , 'number': '456' , 'marks': { 'hindi':23 , 'maths':45} },
             2: {'name': 'manav' , 'number': '788652' , 'marks': { 'hindi':93 , 'maths':85}}
             }
    
for i in data.keys():
        print( i , data[i]['name'] , data[i]['marks'])