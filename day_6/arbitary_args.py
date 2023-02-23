def my_addition_arbitary_positional(*numbers):
    """
    1) receives two numbers from the invoking application and returns 
        a) addition 
    """
    sum = 0 
    for num in numbers:
        sum = sum+ num
    return sum 


def my_addition_arbitary_keyword(**numbers_dict):
    """"
      1) receives two numbers from the invoking application and returns 
        a) addition 
 
    """
    sum = 0 
    for num in numbers_dict.values():
        sum = sum+ num
        return sum 