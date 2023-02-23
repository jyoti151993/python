
# 28: Write a program that keeps name and birthday in a dictionary as key-value pairs. The program should display a menu that lets the user search a person’s birthday, add a new name and birthday, change an existing birthday, and delete an existing name and birthday
flag=True
name_birthday=dict()
while(flag):
    print("""Choose the option from below:
          1.Add a new name and birthday
          2.Search a person's birthday using name
          3.Change an existing birthday
          4.Delete an existing birthday
          5.Exit""")
    choice=int(input("Enter choice :"))
    if choice==1:
        name=input("Enter name :")
        birthday=input("Enter birthday (yyyy-mm-dd):")
        name_birthday[name]=birthday
        print("Name and birthday added!!")
        print(name_birthday)
    elif choice==2:
        name=input("Enter name :")
        if name in name_birthday.keys():
            print(f"The birthday of {name} is on : ",name_birthday[name])
        else:
            print("Name not present!!")
    elif choice==3:
        name=input("Enter name :")
        birthday=input("Enter new birthday (yyyy-mm-dd):")
        if name in name_birthday.keys():
            name_birthday[name]=birthday
            print("Birthday updated!!")
            print(name_birthday)
        else:
            print("Name not present!!")
    elif choice==4:
        name=input("Enter name to be deleted:")
        del name_birthday[name]
        print("Birthday deleted!!")
        print(name_birthday)
    elif choice==5:
        flag=False
    else:
        print("Enter valid choice!!")