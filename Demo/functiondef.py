# function that perform a task
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard.")


greet("Josh", "Smith")

# function that return value


def get_greeting(name):
    return f"Hello {name}"


message = get_greeting("Hillary")
print(message)
