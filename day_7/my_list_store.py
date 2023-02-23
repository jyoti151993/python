while(True):
    print("Do you wish to manage the members?")
    store = input("::: Choose (Y/N):::").upper()
    if(store == "Y"):
        members=[]
        no_Of_mem=int(input("Enter the number of members "))
        for i in range(no_Of_mem):
            members.append(input("Enter the member name::: "))
        print(members)



        print(len(members))
        members.append(input("Add one member:: "))
        print(members)
        add_list=[]
        for i in range(3):
            add_list.append(input("Enter 3 new member names::: "))
        members.extend(add_list) 
        print(members)

        rm_mem =input("Enter the member name to be removed  ")
        if rm_mem in members:
            members.remove(rm_mem)
        print(members)
        members.pop()
        print(members)

        print(members[2],members[3],members[4])
 

    else:
        break
