sum=0
i=1
j=1
lst=[i,j]
numberget=int(input('请输入斐波那契数列上限：'))
print('\n---------------打印斐波那契数列-------------------\n')
while sum<numberget:
    sum=i+j
    lst.append(sum)
    i=j
    j=sum
lst.pop(-1)
print(lst,"\n")
print('总数：',lst.index(lst[-1])+1,'\n')
num1=0
for item in lst:
    fir=str(item)
    if fir[0]=='1':
        num1+=1
gl1=num1/(lst.index(lst[-1])+1)*100
print('1出现的次数：',num1,'\t\t1出现的概率：','%.2f'%gl1,'%')
num2=0
for item in lst:
    fir=str(item)
    if fir[0]=='2':
        num2+=1
gl2=num2/(lst.index(lst[-1])+1)*100
print('2出现的次数：',num2,'\t\t2出现的概率：','%.2f'%gl2,'%')
num3=0
for item in lst:
    fir=str(item)
    if fir[0]=='3':
        num3+=1
gl3=num3/(lst.index(lst[-1])+1)*100
print('3出现的次数：',num3,'\t\t3出现的概率：','%.2f'%gl3,'%')
hjfgl=lst[-2]/lst[-1]
print('\n黄金分割近似值：','%.3f'%hjfgl,'\n')    
   