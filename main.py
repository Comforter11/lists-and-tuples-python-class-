#List os ages.
list_ages=[2, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
print("highest element is:", max(list_ages))
#Removing duplicates.
list_ages=list(dict.fromkeys(list_ages))
print(list_ages)
#Finding common data.
ages1=[2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages2=[2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
result = True

def common_data(ages1, ages2):
    for x in ages1:
     for y in ages2:
         if x == y:
          result = True
    return result

print(common_data(ages1, ages2))

