##############################################
"""
    1
"""
# a = float(input("a <=== "))
# b = float(input("b <=== "))
# c = float(input("c <=== "))

# if(a<=b and a<=c):
#     print(a) #min is a
# if(b<=a and b<=c):
#     print(b) #min is b
# if(c<=a and c<=b):
#     print(c) #min is c
#########end###################################

##############################################
"""
    2
"""
# a = float(input("a <=== "))
# b = float(input("b <=== "))
# c = float(input("c <=== "))

# minNumber = min(a,b,c)
# print(minNumber)
#########end###################################

##############################################
"""
    3
"""
a = float(input("a <=== "))
b = float(input("b <=== "))
c = float(input("c <=== "))

minNumber = a
if(b<minNumber):
    minNumber = b
if(c<minNumber):
    minNumber = c

print(minNumber)
#########end###################################
