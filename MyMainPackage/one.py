#this is a Basic example of how __main__ can be used

def func():
    print("Hello")
print("Top Level")

if __name__ == '__main__': # this line of code helps us to know if our script is run directly or being imported 
    print("This script is running directly")
else:
    print("This script has been imported")