f=open('myFile.txt','r')
print(f.readline(3),end="")

POS=1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['POS']=i
            return True
        i=i+1

    return False

list=[17,4,34,24,47,93]
n=int(input("Enter any number which you want check in list "))

if search(list,n):
    print("Found at",POS)
else:
    print("Not Found")