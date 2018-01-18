class Parent():

    def print_last_name(self):
        print("Roberts")
    def print_middle_name(self):
        print("rose")

#in function braces write the name of class to inherit
class Child(Parent):

    def print_first_name(self):
        print("bucky")
#overriding
    def print_last_name(self):
        print("luther")


bucky = Child()

bucky.print_first_name()
bucky.print_last_name()
bucky.print_middle_name()
