#!/usr/bin/python3

def scope_function():
  global var_1
  var_1 = "I say hello"
  var_2 = "You say good-bye"
  print("var_1 (inside function block):", var_1)
  print("var_2 (inside function block):", var_2)

var_1 = "Hello, hello"
var_2 = "Good-Bye"
print("var_1 (outside function block before function call):", var_1)
print("var_2 (outside function block before function call):", var_2)
scope_function()
print("var_1 (outside function block after function call):", var_1)
print("var_2 (outside function block after function call):", var_2)

