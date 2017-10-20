#!/usr/bin/end python3
print('Before if block')
x = 100
print('x=',x)
if True:  # this if condition will always be True 
  # we want to make sure the block gets executed
  # so we can show you what happens
  print('Inside if block')
  y = 10
  x = 30
  print("x=", x)
  print("y=", y)

print('After if block')
print("x=", x)
print("y=", y)
