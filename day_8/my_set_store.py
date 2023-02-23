""""Create a program named "my_set_store" which support following operations on two sets
    provided by user 

for ex: 
	A = {1,2,3,4,5}
	B = {18,19,20,21}
is provided by the user

Operations supported by our program are :
	1: Union
	2: Intersection 
	3: A-B
	4: B-A
	5: Take a element from user and Display if that element is a member of set B 
	6: Display number of elements in the set A
    7: Display number of elements in the set B
	8: Add an element taken from the user to the set A
	9: Add multiple elements taken from the user to the set A
	10: Remove an element taken from the user from set A	


"""




A=set()
B=set()
C=set()
size=int(input("Enter the no. of elements to be added in A : "))
for i in range(size):
  A.add(input("Enter the element : "))
print(A) 
size=int(input("Enter the no. of elements to be added in B : "))
for i in range(size):
  B.add(input("Enter the element : "))
print(B)
size=int(input("Enter the no. to be added in set C: "))
for i in range(size):
  C.add(input("Enter the elemnent : "))
print(C) 
while True: 
    option=int(input(("""---Welcome,to my_set_store App-----
    __________choose an option no. for performing listed operations___________
    1: Union
	2: Intersection 
	3: A-B
	4: B-A
	5: Take a element from user and Display if that element is a member of set B 
	6: Display number of elements in the set A
    7: Display number of elements in the set B
	8: Add an element taken from the user to the set A
	9: Add multiple elements taken from the user to the set A
	10: Remove an element taken from the user from set A

    """)))
    if option == 1:
        print(A.union(B))
    elif option==2:
        print(B.intersection(B))
    elif option == 3:
        print(A.difference(B))
    elif option == 4:
        print(B.intersection(A))
    elif option == 5:
        element=int(input("Enter an element to verify if it a member of set B:  "))
        if (element in B)==True:
            print(B)
    elif option ==6:
        print(len(A))
    elif option == 7:
        print(len(B))
    elif option==8: 
        print(A.add(int(input("Enter the element to be added in set A: "))))
    elif option==9:
        print(A.update(C))
    elif option==10:
        print(A.remove(int(input("Enter the element to removed from set B"))))
    else:
        break
       
      
