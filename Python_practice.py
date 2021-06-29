print("Hello World")
type(3)
type("Hello World")
type(True)
5 + 2 * 3
3**3%5
counties = ["Arapahoe","Denver","Jefferson"]
counties
counties[0]
len(counties)
type(3)
ballots = 1,341
type(73.81)
my_list = {}
counties = ["Arapahoe","Denver","Jefferson"]
counties
print(counties[2])
counties[-2]
list[start : end]
counties[:2]
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")
counties.pop(3)
counties[2] = "El Paso"
counties
counties_tuple = ("Arapahoe","Denver","Jefferson")
my_dictionary = ["Arapahoe"] = 422829
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
counties_dict.items()
counties_dict.values()
counties_dict.get("Denver")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data


for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)


    counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

    
  for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")  
    