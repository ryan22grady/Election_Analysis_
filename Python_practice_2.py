counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


#A condition-controlled loop uses a true or false condition to control 
# the number of times that it repeats, 
# like asking a user if they want to continue with their online shopping after 
# they add something to their "basket." This type of loop is also called a while loop.

#A count-controlled loop repeats a specific number of times depending on the conditions, 
# such as getting all the items in a list. 
# This type of loop is also called a for loop.

x = 0
while x <= 5:
    print(x)
    x = x + 1

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

num = 2
for num in range(5)
print(num)