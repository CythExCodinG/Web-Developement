str="Rohit is bad boy "
list=["","","",""]
strnew=""
a=0
count=0
for i in str:
  count=0
  if(i==' '):
    list[a]=strnew
    a=a+1
    count=count+1
  if count>0:
    strnew=""
  strnew=strnew+i
  
print(list)