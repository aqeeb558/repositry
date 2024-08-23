P=23
G=9
print(" the value of p is : %d"%(P))
print(" the value of g is : %d"%(G))

a=4
print("the private key a for alice is :%d"%(a))
x=int(pow(G,a,P))
b=3
print("the private key a for bob is :%d"%(b))
y=int(pow(G,b,P))
ka=int(pow(y,a,P))
kb=int(pow(x,b,P))
print("secret key for the alice is : %d"%(ka))
print("secret key for the bob is : %d" %(kb))
