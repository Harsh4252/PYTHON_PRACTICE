#wap to count no of even and odd no btw 1 to 20 using function
def harsh():
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   
    n=len(arr)
    counteven=0
    countodd=0
    for i in range(0,n):
        if arr[i]%2==0:
            counteven+=1
        else:
            countodd+=1
    print("total no of even numbers are",counteven)
    print("total no of odd numbers are",countodd)

harsh()
