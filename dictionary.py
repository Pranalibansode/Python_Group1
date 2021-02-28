"""Create a dictionary named fruits with key values as 'apple', 'banana', and 'cherry' that have values as 'green', 'yellow' and 'red'.
"""

d={
     'apple':'green', 
    'banana':'yellow', 
    'cherry':'red'
}
"""Change the color of 'apple' from 'green' to 'red'
"""

d['apple']='red'
d['guava']='green'

#Add another fruit 'guava', with it's color as 'green'
#Remove the entry for 'cherry
del(d['cherry'])

#Print out the final dictionary
print(d)

 