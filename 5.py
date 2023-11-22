a=5
b=10
print((a>b and "a>b")or
      (b>a and "b>a"))

#The or operator then returns the first truthy value encountered. 
# If the first condition is true, 
#it prints "a>b". If the first condition is false,
#it prints the result of the second condition, "b>a".
