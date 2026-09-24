x=float(input('what is the cost price'))
if x>10000:
    print('your tax amount is',x*0.15,)
elif (x<10000)and(x>5000):
    print('your tax amount is',x*0.10,)
elif (x<5000):
    print('your tax amount is',x*0.05,)
 
