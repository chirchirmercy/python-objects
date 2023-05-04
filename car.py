#  Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account

#Car
class car:
    name="Nissan"
    model="camry"
    colour="black"
    def __init__(self,name,model,colour):
        self.name=name
        self.model=model
        self.colour=colour
    def greet_student(self):
        return f"I need{self.name},{self.model}which is{self.colour}"
    

                                      


