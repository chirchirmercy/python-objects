# fruit
class fruit:
    type="avocado"
    colour="green"
    size="big"
    def __init__ (self,type,colour,size):
        self.type=type
        self.colour=colour
        self.size=size
    def greet_student(self):
    return f"I need{self.type},{self.colour}which is{self.size}"