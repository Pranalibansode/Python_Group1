#Creating list named as class_1
class_1=['Amit Sharma', 'Jaspal Singh', 'Shekhar Kumar', 'Yashodha Naik']

#Creating list named as class_2
class_2=['Hiten Patel', 'Gauri Sharma', 'Chetan Nitave']

#Concat the list class_1 and class_2 and storing in new_class
new_class=class_1+class_2
print(f"\nStudents in the class :\n{new_class}\n")

#Append a new element in new_class
new_class.append('Priti Patil')
print(f"\nnew student is added in our claas her name is:'Priti Patil'\n")
print(f"\nNew member added\n\n{new_class}\n")

#Remove an element from new_class
new_class.remove('Yashodha Naik')
print(f"\nYashodha is removed from class\n")
print(f"\n{new_class}\n")

#creating dictionary named jaspal_singh
jaspal_singh={
               'Math'    :65,
               'English' :70,
               'History' :80,
               'Hindi'   :70,
               'Science' :60
             }
value=jaspal_singh.values()             
total=sum(value)
#print(total)

#calculate the percentage of jaspal_singh
percentage=(total/500)*100
print(f"\nThe percentage of Jaspal Singh is {percentage}\n")

mathematics={
               'Amit Sharma'  :78, 
               'Jaspal Singh' :90, 
               'Shekhar Kumar':65, 
               'Hiten Patel'  :50, 
               'Gauri Sharma' :70, 
               'Chetan Nitave':66,
               'Priti Patil'  :75
            }
    
topper=max(mathematics, key=mathematics.get)
#print(topper)

t=topper.split(' ')
#print(t)
first_name,last_name=t
#print(first_name)
#print(last_name)


full_name=first_name+' '+last_name
certificate=full_name.upper()
print(f"""\n      This certificate is awarded to
                  {certificate}
        to obtain highest score in subject
          mathematics""")



