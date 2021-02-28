#Store the values in a list called weights.
print ("\nweights of four family members are ")
weights=[70,80,45,50]
print (weights)

#Save the maximum weight from the list to maximum variable. Print it out.
maximum=max(weights)
print ("\nmaximum weight in list is :", maximum)

#we have wrongly entered 45 and that should be 48.
#So, it's time to replace the wrong weight with the correct one.  
print ("\nreplace the wrong weight 45 with the correct one 48")
weights[2]=48
print(weights)

#count the total weight
print ("\ncount the total weight")
total=sum(weights)
print ("total weight is :",total)