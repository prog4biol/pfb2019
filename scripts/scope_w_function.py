#!/usr/bin/python3

def scope_function(x):
  x = 5
  print("x (inside function block):", x)
  print("y (inside function block):", y)
  print("z (inside function block):", z)

x = 100
y = 20;
if x > y: 
  z = 10
  x = 30
  print("x (inside if block):", x) 
  print("y (inside if block):", y)
  print("z (inside if block):", z)

print("x (outside if block):)", x)
print("y (outside if block):", y)
print("z (outside if block):", z)

scope_function(500)

print("x (outside if block after function call):)", x)
