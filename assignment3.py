#1q
total= 0
list=[8,2,3,0,7]
for i in range(0,len(list)):
  total=total+list[i]
print("sum of all elements in given list 8+2+3+0+7:",total)
#2q
txt="1234abcd"[::-1]
print(txt)
#or
b=[]
x=input("enter the input ")
for i in range(len(x)-1,-1,-1):
    b.append(x[i])
b=''.join(b)
print(b)
#3q
x='The quick Brow Fox'
count1=0
count2=0
for i in x:
    if i.isupper():
        count1=count1+1
    elif i.islower():  
        count2=count2+1
    else :
        pass
print ("No. of Upper case characters : ", count1)
print ("No. of Lower case Characters : ", count2)       

