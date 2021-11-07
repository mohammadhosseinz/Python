##############################################
"""
    1
"""
# a = float(input("a <=== "))
# b = float(input("b <=== "))
# c = float(input("c <=== "))
# d = float(input("d <=== "))
# e = float(input("e <=== "))

# if(a>=b and a>=c and a>=d and a>=e):
#     print(a) #max is a
# elif(b>=a and b>=c and b>=d and b>=e):
#     print(b) #max is b
# elif(c>=a and c>=b and c>=d and c>=e):
#     print(c) #max is c
# elif(d>=a and d>=b and d>=c and d>=e):
#     print(d) #max is d
# elif(e>=a and e>=b and e>=c and e>=d):
#     print(e) #max is e
#########end###################################


##############################################
"""
    2
"""
# a = float(input("a <=== "))
# b = float(input("b <=== "))
# c = float(input("c <=== "))
# d = float(input("d <=== "))
# e = float(input("e <=== "))

# maxNumber = max(a,b,c,d,e)
# print(maxNumber)
#########end###################################


##############################################
"""
    3
"""
# n = 5
# maxNumber = 0
# for i in range(1,n+1):
#     nomre = float(input("nomre "+str(i)+" <=== "))
#     if(nomre>maxNumber):
#         maxNumber = nomre
# print(maxNumber)
#########end###################################


##############################################
"""
    4
"""
# n = 5
# maxNumber = 0
# for i in range(1,n+1):
#     nomre = float(input("nomre "+str(i)+" <=== "))
#     maxNumber = max(maxNumber,nomre)
# print(maxNumber)
#########end###################################

##############################################
"""
    5
"""
# n = 5
# maxNumber =  float(input("nomre 1 <=== "))
# for i in range(2,n+1):
#     nomre = float(input("nomre "+str(i)+" <=== "))
#     maxNumber = max(maxNumber,nomre)
# print(maxNumber)
#########end###################################


##############################################
"""
    6
"""
a = float(input("a <=== "))
b = float(input("b <=== "))
c = float(input("c <=== "))
d = float(input("d <=== "))
e = float(input("e <=== "))
maxNumber = b
if(a>maxNumber):
    maxNumber = a
if(c>maxNumber):
    maxNumber = c
if(d>maxNumber):
    maxNumber = d
if(e>maxNumber):
    maxNumber = e

print(maxNumber)

#########end###################################