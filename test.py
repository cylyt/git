people={}

for x in range(1,31):
    people[x]=1
#print(people)

check=1
i=1
j=0

while i<=31:
    if i==31:
        i=1
        continue
    elif j==15:
        break
    
    if people[i]==0:
        i+=1
        continue
    else:
        if check==9:
            people[i]=0
            print('第%d个人下船' %i)
            check=0
            j+=1
        check+=1
        i+=1
    
print(people)
        