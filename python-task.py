print("hello world")

# Dictionaries


thisdict = {"name":"John Doe", "age":26, "city":"New York","list":["hello","world","!"]}

thisdict["first name"] = "Ali Raza"
print(thisdict["name"])

x = thisdict.get("name")
print(x)
thisdict.update({"last name":"Hello Arsln"})
print( thisdict.values())
print(thisdict.keys())
print(thisdict) 
# --------------------------------
# one parent are added multiple child 

prnt = {
    "child1":{
        "name":"ashutosh",
        "age":24,
    },
    "child2":{
        "name":"Aslam",
        "age":30,
    },
    "child":{
        "name":"afaq",
        "age":12
    }
}

prnt["child1"] = "Ashutosh Khan"
prnt2 = prnt.copy()
print(prnt)
print(prnt2)

dic1 = {"name":"John Doe", "age":26, "city":"New York"}
dic2 = dic1.copy()
dic1["name"] = "Arslan"
print(dic1)
print(dic2)


print(prnt)
print(prnt2)
print(prnt)
print(prnt2)
print(prnt)
print(prnt["child1"]["name"])
prnt["child1"]["name"] = "Ashutosh Khan"
print(prnt)
