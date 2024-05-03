pos=1

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid






list=[17,4,34,24,47,93]
print(list)
n=int(input("Enter any number which you want check in list "))

if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")


