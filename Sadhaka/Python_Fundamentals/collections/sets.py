
# set only includes unique elements
nums={10,20,30,10,20,30,40}
print(nums)

b = set()   # empty set

nums.remove(20)
print(nums)

nums.add(99)
nums.update([20,22])

print(nums)

languages = {"Python", "Java", "C++"}

print("Python" in languages)     # True
print("Ruby" not in languages)   # True

for language in languages:
    print(language)

python_students = {'Animesh','Raju','Bheem'}
java_students = {'Ram','Shyam','Aloo'}

# operations

# union    
python_students | java_students
# {'Aman', 'Riya', 'Kabir', 'Neha'}

python_students & java_students
# {'Riya', 'Kabir'}

python_students - java_students
# {'Aman'}

