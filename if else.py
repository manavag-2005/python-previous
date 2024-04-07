# marks = int(input("enter the number: "))

# if(n%5==0 and n%3==0):
#     print(n , "is divisible by both")

# else:
#     print(n , "is not divisible by both")

# if(n<0):
#     print(n , "is negative")

# if(n>0):
#     print(n, "is positive")
    
marks = int(input("marks: "))

if(marks>=90):
    print("A")
elif(marks >=80 and marks<90):
    print("B")
elif(marks<=70 and marks <80):
    print("C")
else:
    print("D")