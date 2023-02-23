# create  your exception and raise them
class list_handling_exceptions(Exception):
    pass


def pos_num_list(positive_list):
    print("Enter the no. of elements you want to add in the Positive list")
    limit = int(input("No. of elements "))

    for index in range(0, limit):
       check_num = (int(input("please enter a positive no.")))
    if check_num < 0 :
        raise list_handling_exceptions("Oops you have entered a negative number")
    elif check_num>0:
         positive_list.append(check_num)
         print("No added successfully")
    elif len(positive_list) == 0:
         raise list_handling_exceptions
         print("List is Empty!!!!!")
    else:
         print("Bye Bye")


def neg_num_list(negative_list):
      print("Enter the no. of elements you want to add in the Negative list")
      limit = int(input("No. of elements "))
      for index in range(0, limit):
         check_num = (int(input("please enter negative no.")))
      if check_num >= 0 :
         print("Invalid Input, Please Retry!!!")
         raise list_handling_exceptions
      elif check_num<0:
         negative_list.append(check_num)
         print("Negative nos. added successfully")
      elif len(negative_list) == 0:
          print("Empty List")
          raise list_handling_exceptions
      else:
          print("Bye Bye")

def heterogeneous_list(heterogeneous_list):
   limit = int(input("No. of elements "))
   while
    heterogeneous_list
    data_type= int(input(""" Please choose an option from the below list
     1. str
     2. int
     3. float
     4. set
     5. dict
     6. tuple
     7. list
    """)
    member = data_type(input("Enter the member"))
    while True:
       if isinstance(member,(str,int,float, set, dict, tuple )):


   if type(member) == 'str'

def is_element_present():
   option = int(input("""Please choose one of the below list name
    1. positive_list
    2. negative_list
    3. heterogeneos_list
   """))
   if option == 1:
      rcv_no=int(input("please input the element of postive list that you want to check if it is a member"))
      if rcv_no in positive_list:
         print("Exists")
      else:
         raise list_handling_exceptions
         print("Does not exist")
   elif option == 2:
      rcv_no = int(input("please input the element of negative list that you want to check if it is a member"))
      if rcv_no in negative_list:
         print("Exists")
      else:
         raise list_handling_exceptions
         print("Does not exist")







def refresh_list():
def my_exception_store():
    positive_list = []
    negative_list = []
    heterogeneous_list = []

    print("Welcome to my Exception store ! what would you do today")
    print("******Options**********")
    print("""1: Create  a positive  number list 
     2: create a negative number list
     3: create a heterogeneous list
     4: check if element is present in the list 
     5: Refresh the program to start with empty list
     6: Exit
   """)
    choice = int(input("Please enter your choice : "))


while (True):
  if choice == 1:
    pos_num_list(positive_list)
  elif choice == 2:
    negative_num_list(negative_list)
  elif choice == 3:


