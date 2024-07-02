def creat_profile(name, age, occupation="student"):
    print(f"Name: {name}, Age: {age}, Occupation: {occupation}", end="")


print(creat_profile("Alice", 25))
print(creat_profile("Bob", 30, "engineer"))
print(creat_profile(age=22, name="Charlie", occupation="designer"))
