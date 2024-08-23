P=23
G=7
print("the value of the P is :%d"%(P))
print("the value of the G is :%d"%(G))
a=4
print("the private key of the alice is :%d"%(a))
y=int(pow(P,a,G))
b=3
print("the private key of the bob is :%d"%(b))
x=int(pow(P,b,G))
ka=int(pow(x,a,P))
kb=int(pow(y,b,P))
print("the secret key of alice is %d:"%(ka))
print("the secret key of bob is %d:"%(kb))
      


