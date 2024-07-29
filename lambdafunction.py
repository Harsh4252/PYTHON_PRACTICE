x= lambda a : a+10
print(x(5)) #lambda function ko call nii karna padta 

x=lambda a,b:a*b
print(x(5,6)) #lambda function m kitne bhi parameter pass kar skte hai 


def myfunc(n):
    return lambda a:a*n #lambda inside function 
mydoubler=myfunc(2)
print(mydoubler(11))

