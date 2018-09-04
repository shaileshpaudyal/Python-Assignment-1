"""
Write a class in which its one method accepts a string from console and 
another method to print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

"""


class TextFilter:

    def __init__(self):
        self.text = ""
    
    def stringInput(self):
        self.text = input("Enter the string: ")

    def filterText(self):
        x = self.text
        length = len(x)
        new = []
        y = list(x)
        # b
        
        # for a in range(0,length+1,2):
        for a in range(0,length,2):
            new.append(y[a])

        final = "".join(str(a) for a in new)
        print(final)

filter=TextFilter()
filter.stringInput()
filter.filterText()