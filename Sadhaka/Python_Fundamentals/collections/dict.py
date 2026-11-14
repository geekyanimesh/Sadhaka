
student = {
    "name":"Animesh",
    "age":21,
    "class":"7th Sem"
}

print(student["name"])

student["name"]="Raju"
print(student["name"])

print(student.get("name"))      # get method

student = {"name": "Animesh", "cgpa": 8.0}

# Add
student["branch"] = "CSE"

# Update
student["cgpa"] = 8.2

# Add or update multiple entries
student.update({"year": 4, "city": "Dhanbad"})

removed = student.pop("city")
print(removed)

for name,score in student.items():
    print(f"{name}:{score}")

student.update({"name":"Animesh"})

for i,j in student.items():
    print(i,j)

