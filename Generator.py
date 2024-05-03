from iterator import values


def topten():

    n=1
    while n<=5:
        sq=n*n
        yield sq
        n+=1


values=topten()
for i in values:
    print(i)

a=5
b=0

try:
    print(a/b)

except Exception as e:
    print("Hey, You cannot divide a number by Zero",e)

finally:
    print("Close the connection")
print('Bye')