f=open("1.txt","w")
s=int(input("How Many Lines : "))
for i in range(s):
    s=input("Enter Your Name : ")
    f.write(s+"\n")
f.close()

#######
f=open("2.txt","w")
s=int(input("How Many Lines : "))
L=[]
for i in range(s):
    s=input("Enter Your Name : ")
    L.append(s+"\n")
f.writelines(L)
f.close()
