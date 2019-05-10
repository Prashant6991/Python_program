#program to convert no. to word
n=int(input("Enter a no : "))
unit=['zero','one','two','three','four','five','six','seven','eight','nine']
ele=['eleven','twelve','thirthteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tenplace=['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
if 999<n<10000 and n%100!=0:
  h1=n//1000
  t2=n%1000
  if 99<t2<1000 and t2%100!=0:
    h=t2//100
    t1=t2%100
    if 20<t1<100 and t1%10!=0:
      n1=(t1//10)-1
      n2=t1%10
      print(unit[h1],"thousand",unit[h],"hundred and ",tenplace[n1],unit[n2])
    elif t1%10==0:
      t=(t1//10)-1
      print(unit[h1],"thousand",unit[h],"hundred and ",tenplace[t])
elif n%1000==0:
  n1=n//1000
  print(unit[n1],"thousand")
elif 99<n<1000 and n%100!=0:
  h=n//100
  t1=n%100
  if 20<t1<100 and t1%10!=0:
    n1=(t1//10)-1
    n2=t1%10
    print(unit[h],"hundred and ",tenplace[n1],unit[n2])
  elif t1%100==0:
    t=(t1//10)-1
    print(unit[h],"hundred and ",tenplace[t])
elif n%100==0:
  n1=n//100
  print(unit[n1],"hundred") 
elif 20<n<100 and n%10!=0:
  n1=(n//10)-1
  n2=n%10
  print(tenplace[n1],unit[n2])
elif n%10==0:
  t=(n//10)-1
  print(tenplace[t])
elif 10<n<20:
  r=n%10
  print(ele[r-1])
elif n<10:
    print(unit[n])



        

  

