def print_info(name, age, city, job):
    print("Positional arguments:")
    print(f"-{name}")
    print(f"-{age}\n")
    print("Keyword arguments:")
    print(f"- city: {city}")
    print(f"- job: {job}")


print_info("Alice", 25, city="New York", job="Developer")
