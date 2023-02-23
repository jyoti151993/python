# 1) Create a class that captures students. 
# 	Each student has a first name, last name, class year, and major. Create two examples of students.

class Students:
    def __init__(self, first_name, last_name, class_year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.class_year  = class_year
        self.major = major


students1 = Students("Jyoti", "Choudhary", 2015, "Mechanical Engineering")
students1 = Students("Deepak", "singh", 2016, "Electrical Engineering")
