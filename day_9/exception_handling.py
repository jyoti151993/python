#create your exception and raise them
def check_age_greater_than_18(age):
    if age < 18:
        raise ValueError("Oops, A word of caution from me !!!")
    print("All Good mate , Please proceed !!!")


check_age_greater_than_18(int(input("Please enter age which is greater than 18")))