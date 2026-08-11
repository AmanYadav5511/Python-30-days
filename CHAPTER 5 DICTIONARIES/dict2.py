def add_key(d, key, value):
    print("Before:", d)
    d[key] = value
    print("After: ", d)


student = {
    "name": "Aman",
    "age": 21
}

add_key(student, "city", "Delhi")

print()

add_key(student, "age", 22)