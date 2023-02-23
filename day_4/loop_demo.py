# with break
num=1
while(num<10):
    print(num, end=",")
    num+=1
    break

# with continue
num=1
while(num<10):
    print(num, end=" ")
    num+=1
    continue

# infinite loop
num=1
while(num<10):
      print(num,end="")
      continue
      num+=1

# while loop with if
num=1
while(num<10):
     if num<6:      
        print(num,end="")
        num+=1

# while with else and if
num=1
while(num<10):
     if num<6:      
        print(num,end="")
else:
        print(num,end="") 
        num+=1

# another ex
num=6
while(num<10):
    if num>6:
      print(num,end="")
      num+=1

# next ex
num=1
while(num<10):
    if num>6:
      print(" ",end="")
      num+=1
    print(num,end="")


# ex with pass
num=1
while(num<10):
    if num>6:
      pass
      num+=1
    print(num,end="")


