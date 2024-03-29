import random
n=10
p=float(input("the error probability"))
m=int((2**n)*p)
print(m)
message=str(input("enter the message"))
if (m==0):
    print("message is",message)
    exit()

no_of_errors=random.randrange(m)
#no_of_errors=1
print(no_of_errors)
position_of_error=[]
for i in range(no_of_errors):
    k=random.randrange(2**n)
    print(k,type(k))
    position_of_error.append(k)


def func(x,a):

   if(len(x)+1 != len(a)):
       print("invalid input")
   output=int(a[0])
   for i in range(len(x)):
       output=((int(x[n-i-1])*int(a[i+1]))+output)%2
   print(x,a,output)

   return(output)



def encoding(message):
    codeword=''

    for i in range(2**n):
        if(len(bin(i)[2:])<n):
            pad=n-len(bin(i)[2:])
            x=('0'*pad)+bin(i)[2:]
        else:
            x=bin(i)[2:]

        codeword=codeword+str(func(x,message))

    return codeword
print(encoding(message))
#inducing errors
encode=encoding(message)
for i in (position_of_error):
    if(encode[i]=='0'):
        encode=encode[:i]+'1'+encode[i+1:]
    else:
        encode=encode[:i]+'0'+encode[i+1:]
print(encode)
def walsh(encode):
    a1=[]
    a2=[0 for i in range(2**n)]
    for i in range(2**n):
        a1.append((-1)**(int(encode[i])))
    print(a1)
    i=0
    for j in range(0, (2 ** n) - (2 ** i), (2 ** i) + 1):
        a2[j] = a1[j] + a1[j + (2 ** i)]
        a2[j + (2 ** i)] = a1[j] - a1[j + (2 ** i)]
        print(j, j + (2 ** i))
    a1 = a2
    a2 = [0 for i in range(2 ** n)]
    print(i, ":", a1)
    for i in range(1,n):
        for p in range(2**(n-i-1)):
            for j in range(0,2**i):
                k=j+p*(2**(i+1))
                a2[k]=a1[k]+a1[k+(2**i)]
                a2[k+(2**i)] = a1[k] - a1[k + (2**i)]
                print(k,k+(2**i))
        a1=a2
        a2 = [0 for i in range(2 ** n)]
        print(i,":",a1)
    a3=[]
    output=''
    for i in a1:
        a3.append(abs(i))
    k=max(a3)
    print(k)
    index=a3.index(k)
    print(index)
    if(a1[index]>0):
        pad = n - len(bin(index)[2:])
        m=('0' * pad) + bin(index)[2:]
        output ='0'+ m[::-1]
    if (a1[index] <0):
        pad = n - len(bin(index)[2:])
        output = '1' + m[::-1]
    print(m)

    return output

print("decoded message is",walsh(encode))
