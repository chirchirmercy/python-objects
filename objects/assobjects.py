# Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials


class Student:
    first_name="mercy"
    last_name="cheptoo"
    age=40
    country="kenya"

def __init__(self,show_full_name,year_of_birth,show_initials):

    self.show_full_name=show_full_name
    self.year_of_birth=year_of_birth
    self.show_initials=show_initials

student=Student()
print(f"Student:{student.first_name[0]} {student.last_name[0]}")
print(f"Student: {20} years old  year of birth {2000}")
print(f"Student:{2000}")










