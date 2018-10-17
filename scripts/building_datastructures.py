#!/usr/bin/env python3

####   double ## indicate output of print

print("create a list called new_data: new_data = []")
new_data = []        
print(new_data)         ## []
print("append a list to list new_data: new_data.append([1,2,3])")
new_data.append([1,2,3])  
print(new_data)         ## [[1, 2, 3]]
print("the value of new_data[0] is a list")
print(new_data[0])      ## [1, 2, 3]         

print("append another list to the list new_data: new_data.append([4,5,6])")
print("now list new_data has a list as a value for index 0 and index 1")
new_data.append([4,5,6])
print(new_data)         ## [[1, 2, 3], [4, 5, 6]]  
print("the value of new_data[1] is a list")
print(new_data[1])      ## [4, 5, 6]
print("the value of new_data[1][6] is an int")
print (new_data[1][2])  ## 6

print("append a dictionary to the list new_data: new_data.append({})")
print("check out the index 2 of new_data")
new_data.append({})
print(new_data)         ## [[1, 2, 3], [4, 5, 6], {}]

print("add a key and value to the dictionary new_data[2]: new_data[2]['key']='value'")
print("check out the index 2 of new_data now") 
new_data[2]['key']='value'
print(new_data)         ## [[1, 2, 3], [4, 5, 6], {'key': 'value'}]

print("add another key and value to the dictionary new_data[2]: new_data[2]['key2']={}")
print("the key is 'key2' and the value is a dictionary")
new_data[2]['key2']={}
print(new_data)
print("add a key to the dictionary new_data[2]['key2']")
print("the key is 'key2' and the value is 'Yay'")
new_data[2]['key2']['something_new']='Yay'
print(new_data)  
    ## [[1, 2, 3], [4, 5, 6], {'key2': {'something_new': 'Yay'}, 'key': 'value'}]



