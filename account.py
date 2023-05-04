# account
class car:
    name="equity"
    accountNumber=334455
    location="nairobi"
    def __init__(self,name,model,colour):
        self.name=name
        self.accountNumber=accountNumber
        self.location=location
    def greet_car(self):
        return (f"I need{self.name},{self.accountNumber}which is{self.location}")