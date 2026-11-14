tup=(1,2,3,4,5)
print(tup)

for i in tup:
    print(i)

intTup=(10)     # int
tup2=(10,)      # tuple

print(type(intTup))
print(type(tup2))

# tuples support indexing and slicing like strings

# nested tuples

tup3=("Nested tuple: ", (233,123))
print(tup3)

print(tup3[0])
print(tup3[1])

a=(1,2)
b=(3,4)

print(a+b)


t=(1,2,3)
items=list(t)
items[1]=4
t=tuple(items)

print(t)

print(type(t))

tup=('Animesh',21,'Ranchi')
name, age, city=tup

print(name)
print(age)
print(city)

