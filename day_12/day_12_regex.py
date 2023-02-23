import re


"""
1) provide me the list of emails that do have special characters of #~`!
2) provide me the list of emails that start with numbers
3) provide me the list of emails that start with numbers followed by an underscore
4) provide me the list of emails that start with numbers followed by an underscore or small case characters
5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
6) Provide me list of emails with only numbers before the @
7) Provide me list of emails with numbers anywhere before the @

"""


def search(pattern, my_string_list):
    for elem in my_string_list:
        my_string = elem
        result = re.search(pattern, my_string)  
        if result:
            print("Group 0 result " , result.group(0))
        


my_string_list=["gaurav1234@gmail.com",
"pratik190900234@gmail.com",
"2009_rocking_person@yahoo.com","GodFather2022@yahoo.com",
"Brocklesner_89_WWE@yahoo.com",
"TheRock_WWE@yahoo.com",
"JohnCena_WWE@yahoo.com",
"Undertaker_Roman_reigns@outlook.com",
"6789764666@rediffmail.com",
"Kane#6789@gmail.com",
]

#1) provide me the list of emails that do have special characters of #~`!
pattern = '(.)*[#~`!](.)*'
search(pattern,my_string_list)

#2) provide me the list of emails that start with numbers
pattern = '^[\d](.)*'
search(pattern,my_string_list)

#