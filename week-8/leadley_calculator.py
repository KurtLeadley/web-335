## Title: leadley_hello_world.py
## Author: Kurt Leadley, Professor Krasso
## Date: 12/4/2019
## Description: Add, Subtract, Divide example, using functions and variables. 

##print out our name function
fn = "Kurt"
ln = "Leadley"
assignment = "Exercise 8.2"
def header(fn,ln,assignment):
    return print(fn+' '+ln+' '+assignment)

## add function (note the : at the end)
def add(n1,n2):
    # you need to indent here or it throws a syntax error
    # try to add
    try:
        return n1 + n2
    except:
        return "Type Error"
def subtract(n1,n2):
    # try to subtract
    try:
        return n1 - n2
    except:
        return "Type Error"
def divide(n1,n2):
    ## make sure n2 does not equal zero
    if n2 == 0:
        return "Cannot divide by zero"
    else:
        # try to divide
        try:
            return n1 / n2
        except:
            return "Type Error"
## print everything out by calling our functions
header(fn,ln,assignment)
print(add(1,"duck"))
print(add(5,10))
print(subtract(30,5))
print(divide(10,0))
print(divide(10,2))